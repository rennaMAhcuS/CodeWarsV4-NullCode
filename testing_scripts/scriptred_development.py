from random import randint

name = 'scriptred_development'


def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1



def checkfriends(pirate, quad):
    sum_friend_quadrants = 0
    up = pirate.investigate_up()[1]
    print(up)
    down = pirate.investigate_down()[1]
    left = pirate.investigate_left()[1]
    right = pirate.investigate_right()[1]
    ne = pirate.investigate_ne()[1]
    nw = pirate.investigate_nw()[1]
    se = pirate.investigate_se()[1]
    sw = pirate.investigate_sw()[1]

    if quad == 'ne':
        if up == 'friend':
            sum_friend_quadrants += 1
        if ne == 'friend':
            sum_friend_quadrants += 1
        if right == 'friend':
            sum_friend_quadrants += 1
    if quad == 'se':
        if down == 'friend':
            sum_friend_quadrants += 1
        if right == 'friend':
            sum_friend_quadrants += 1
        if se == 'friend':
            sum_friend_quadrants += 1
    if quad == 'sw':
        if down == 'friend':
            sum_friend_quadrants += 1
        if sw == 'friend':
            sum_friend_quadrants += 1
        if left == 'friend':
            sum_friend_quadrants += 1
    if quad == 'nw':
        if up == 'friend':
            sum_friend_quadrants += 1
        if nw == 'friend':
            sum_friend_quadrants += 1
        if left == 'friend':
            sum_friend_quadrants += 1

    return sum_friend_quadrants


# try checkenemies also.

def spread(pirate):
    sw = checkfriends(pirate, 'sw')
    se = checkfriends(pirate, 'se')
    ne = checkfriends(pirate, 'ne')
    nw = checkfriends(pirate, 'nw')

    my_dict = {'sw': sw, 'se': se, 'ne': ne, 'nw': nw}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    x, y = pirate.getPosition()

    if sorted_dict[list(sorted_dict.keys())[-1]] == 0:
        return randint(1, 4)

    if list(sorted_dict.keys())[0] == 'sw':
        return moveTo(x - 1, y + 1, pirate)
    elif list(sorted_dict.keys())[0] == 'se':
        return moveTo(x + 1, y + 1, pirate)
    elif list(sorted_dict.keys())[0] == 'ne':
        return moveTo(x + 1, y - 1, pirate)
    elif list(sorted_dict.keys())[0] == 'nw':
        return moveTo(x - 1, y - 1, pirate)


def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()

    if (
            (up == "island1" and s[0] != "myCaptured")
            or (up == "island2" and s[1] != "myCaptured")
            or (up == "island3" and s[2] != "myCaptured")
    ):
        s = up[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(s)

    if (
            (down == "island1" and s[0] != "myCaptured")
            or (down == "island2" and s[1] != "myCaptured")
            or (down == "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(x) + "," + str(y + 1)
        pirate.setTeamSignal(s)

    if (
            (left == "island1" and s[0] != "myCaptured")
            or (left == "island2" and s[1] != "myCaptured")
            or (left == "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(x - 1) + "," + str(y)
        pirate.setTeamSignal(s)

    if (
            (right == "island1" and s[0] != "myCaptured")
            or (right == "island2" and s[1] != "myCaptured")
            or (right == "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(x + 1) + "," + str(y)
        pirate.setTeamSignal(s)

    if pirate.getTeamSignal() != "" and int(pirate.getID()) % 2 == 0:
        s = pirate.getTeamSignal()
        tokenized_s = s.split(",")
        x = int(tokenized_s[0][1:])
        y = int(tokenized_s[1])

        return moveTo(x, y, pirate)

    else:
        return spread(pirate)


def ActTeam(team):
    team_track_players = team.trackPlayers()
    s = team.getTeamSignal()

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)

    if s:
        island_no = int(s[0])
        signal = team_track_players[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")
