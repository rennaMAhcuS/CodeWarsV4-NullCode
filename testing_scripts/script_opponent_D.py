import random

name = "QuadraCoders"


def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1


def quad1(pirate, d):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    nw = pirate.investigate_nw()[0]
    sw = pirate.investigate_sw()[0]
    ne = pirate.investigate_ne()[0]
    se = pirate.investigate_se()[0]
    s = pirate.trackPlayers()

    command = 0

    if (int(pirate.getID()) > 0 and int(pirate.getID()) < 9):
        command = random.randint(1, 4)

    if ((s[0] != "myCaptured" and s[1] != "myCaptured") or (s[1] != "myCaptured" and s[2] != "myCaptured") or (
            s[0] != "myCaptured" and s[2] != "myCaptured") or pirate.getCurrentFrame() < 900):
        # in quad 2 and trying to go to opp
        if pirate.getPosition()[1] == d / 2 - 1 and pirate.getPosition()[0] < d / 2 and command == 3:
            command = random.randint(1, 2)
        # in quad 4 and trying to go to opp
        elif pirate.getPosition()[1] > d / 2 - 1 and pirate.getPosition()[0] == d / 2 and command == 4:
            command = random.randint(1, 3)
    else:
        command = random.randint(1, 4)

    if (
            (up == "island1" and s[0] != "myCaptured")
            or (up == "island2" and s[1] != "myCaptured")
            or (up == "island3")
    ):
        s = up[-1] + str(pirate.getPosition()[0]) + "," + str(pirate.getPosition()[1] - 1)
        pirate.setTeamSignal(s)

    if (
            (down == "island1" and s[0] != "myCaptured")
            or (down == "island2" and s[1] != "myCaptured")
            or (down == "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(pirate.getPosition()[0]) + "," + str(pirate.getPosition()[1] + 1)
        pirate.setTeamSignal(s)

    if (
            (left == "island1" and s[0] != "myCaptured")
            or (left == "island2" and s[1] != "myCaptured")
            or (left == "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(pirate.getPosition()[0] - 1) + "," + str(pirate.getPosition()[1])
        pirate.setTeamSignal(s)

    if (
            (right == "island1" and s[0] != "myCaptured")
            or (right == "island2" and s[1] != "myCaptured")
            or (right == "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(pirate.getPosition()[0] + 1) + "," + str(pirate.getPosition()[1])
        pirate.setTeamSignal(s)

    if int(pirate.getID()) > 8:
        if pirate.getTeamSignal() != "":
            s = pirate.getTeamSignal()
            l = s.split(",")
            x = int(l[0][1:])
            y = int(l[1])

            if (random.randint(1, 20) < 18):
                command = moveTo(x, y, pirate)
            else:
                command = random.randint(1, 4)
        elif (right[0] == "i" and down[0] == "i"):
            command = random.randint(2, 3)
        elif (left[0] == "i" and down[0] == "i"):
            command = random.randint(3, 4)
        elif (up[0] == "i" and right[0] == "i"):
            command = random.randint(1, 2)
        elif (up[0] == "i" and left[0] == "i"):
            command = 1
        else:
            command = random.randint(1, 4)

    return command


def quad2(pirate, d):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    s = pirate.trackPlayers()

    command = 0

    if (int(pirate.getID()) > 0 and int(pirate.getID()) < 9):
        command = random.randint(1, 4)

    if ((s[0] != "myCaptured" and s[1] != "myCaptured") or (s[1] != "myCaptured" and s[2] != "myCaptured") or (
            s[0] != "myCaptured" and s[2] != "myCaptured") or pirate.getCurrentFrame() < 900):
        # in quad 1 and trying to go to opp
        if pirate.getPosition()[1] == d / 2 - 1 and pirate.getPosition()[0] > d / 2 - 1 and command == 3:
            command = random.randint(1, 2)
        # in quad 3 and trying to go to opp
        elif pirate.getPosition()[1] > d / 2 - 1 and pirate.getPosition()[0] == d / 2 - 1 and command == 2:
            command = random.randint(3, 4)
    else:
        command = random.randint(1, 4)

    if (
            (up == "island1" and s[0] != "myCaptured")
            or (up == "island2" and s[1] != "myCaptured")
            or (up == "island3")
    ):
        s = up[-1] + str(pirate.getPosition()[0]) + "," + str(pirate.getPosition()[1] - 1)
        pirate.setTeamSignal(s)

    if (
            (down == "island1" and s[0] != "myCaptured")
            or (down == "island2" and s[1] != "myCaptured")
            or (down == "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(pirate.getPosition()[0]) + "," + str(pirate.getPosition()[1] + 1)
        pirate.setTeamSignal(s)

    if (
            (left == "island1" and s[0] != "myCaptured")
            or (left == "island2" and s[1] != "myCaptured")
            or (left == "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(pirate.getPosition()[0] - 1) + "," + str(pirate.getPosition()[1])
        pirate.setTeamSignal(s)

    if (
            (right == "island1" and s[0] != "myCaptured")
            or (right == "island2" and s[1] != "myCaptured")
            or (right == "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(pirate.getPosition()[0] + 1) + "," + str(pirate.getPosition()[1])
        pirate.setTeamSignal(s)

    if int(pirate.getID()) > 8:
        if pirate.getTeamSignal() != "":
            s = pirate.getTeamSignal()
            l = s.split(",")
            x = int(l[0][1:])
            y = int(l[1])

            if (random.randint(1, 20) < 18):
                command = moveTo(x, y, pirate)
            else:
                command = random.randint(1, 4)

        elif (right[0] == "i" and down[0] == "i"):
            command = random.randint(2, 3)
        elif (left[0] == "i" and down[0] == "i"):
            command = random.randint(3, 4)
        elif (up[0] == "i" and right[0] == "i"):
            command = random.randint(1, 2)
        elif (up[0] == "i" and left[0] == "i"):
            command = 1
        else:
            command = random.randint(1, 4)

    return command


def quad3(pirate, d):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    s = pirate.trackPlayers()

    command = 0

    if (int(pirate.getID()) > 0 and int(pirate.getID()) < 9):
        command = random.randint(1, 4)

    if ((s[0] != "myCaptured" and s[1] != "myCaptured") or (s[1] != "myCaptured" and s[2] != "myCaptured") or (
            s[0] != "myCaptured" and s[2] != "myCaptured") or pirate.getCurrentFrame() < 1900):
        # in quad 2 and trying to go to opp
        if pirate.getPosition()[1] < d / 2 and pirate.getPosition()[0] == d / 2 - 1 and command == 2:
            command = random.randint(3, 4)
        # in quad 4 and trying to go to opp
        elif pirate.getPosition()[1] == d / 2 and pirate.getPosition()[0] > d / 2 - 1 and command == 1:
            command = random.randint(2, 4)
    else:
        command = random.randint(1, 4)

    if (
            (up == "island1" and s[0] != "myCaptured")
            or (up == "island2" and s[1] != "myCaptured")
            or (up == "island3")
    ):
        s = up[-1] + str(pirate.getPosition()[0]) + "," + str(pirate.getPosition()[1] - 1)
        pirate.setTeamSignal(s)

    if (
            (down == "island1" and s[0] != "myCaptured")
            or (down == "island2" and s[1] != "myCaptured")
            or (down == "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(pirate.getPosition()[0]) + "," + str(pirate.getPosition()[1] + 1)
        pirate.setTeamSignal(s)

    if (
            (left == "island1" and s[0] != "myCaptured")
            or (left == "island2" and s[1] != "myCaptured")
            or (left == "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(pirate.getPosition()[0] - 1) + "," + str(pirate.getPosition()[1])
        pirate.setTeamSignal(s)

    if (
            (right == "island1" and s[0] != "myCaptured")
            or (right == "island2" and s[1] != "myCaptured")
            or (right == "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(pirate.getPosition()[0] + 1) + "," + str(pirate.getPosition()[1])
        pirate.setTeamSignal(s)

    if int(pirate.getID()) > 8:
        if pirate.getTeamSignal() != "":
            s = pirate.getTeamSignal()
            l = s.split(",")
            x = int(l[0][1:])
            y = int(l[1])

            if (random.randint(1, 20) < 18):
                command = moveTo(x, y, pirate)
            else:
                command = random.randint(1, 4)
        elif (right[0] == "i" and down[0] == "i"):
            command = random.randint(2, 3)
        elif (left[0] == "i" and down[0] == "i"):
            command = random.randint(3, 4)
        elif (up[0] == "i" and right[0] == "i"):
            command = random.randint(1, 2)
        elif (up[0] == "i" and left[0] == "i"):
            command = 1
        else:
            command = random.randint(1, 4)

    return command


def quad4(pirate, d):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    s = pirate.trackPlayers()

    command = 0

    if (int(pirate.getID()) > 0 and int(pirate.getID()) < 9):
        command = random.randint(1, 4)

    if ((s[0] != "myCaptured" and s[1] != "myCaptured") or (s[1] != "myCaptured" and s[2] != "myCaptured") or (
            s[0] != "myCaptured" and s[2] != "myCaptured") or pirate.getCurrentFrame() < 1900):
        # in quad 1 and trying to go to opp
        if pirate.getPosition()[1] < d / 2 and pirate.getPosition()[0] == d / 2 and command == 4:
            command = random.randint(1, 3)
        # in quad 3 and trying to go to opp
        elif pirate.getPosition()[1] == d / 2 and pirate.getPosition()[0] < d / 2 and command == 1:
            command = random.randint(2, 4)
    else:
        command = random.randint(1, 4)

    if (
            (up == "island1" and s[0] != "myCaptured")
            or (up == "island2" and s[1] != "myCaptured")
            or (up == "island3")
    ):
        s = up[-1] + str(pirate.getPosition()[0]) + "," + str(pirate.getPosition()[1] - 1)
        pirate.setTeamSignal(s)

    if (
            (down == "island1" and s[0] != "myCaptured")
            or (down == "island2" and s[1] != "myCaptured")
            or (down == "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(pirate.getPosition()[0]) + "," + str(pirate.getPosition()[1] + 1)
        pirate.setTeamSignal(s)

    if (
            (left == "island1" and s[0] != "myCaptured")
            or (left == "island2" and s[1] != "myCaptured")
            or (left == "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(pirate.getPosition()[0] - 1) + "," + str(pirate.getPosition()[1])
        pirate.setTeamSignal(s)

    if (
            (right == "island1" and s[0] != "myCaptured")
            or (right == "island2" and s[1] != "myCaptured")
            or (right == "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(pirate.getPosition()[0] + 1) + "," + str(pirate.getPosition()[1])
        pirate.setTeamSignal(s)

    if int(pirate.getID()) > 8:
        if pirate.getTeamSignal() != "":
            s = pirate.getTeamSignal()
            l = s.split(",")
            x = int(l[0][1:])
            y = int(l[1])

            if (random.randint(1, 20) < 18):
                command = moveTo(x, y, pirate)
            else:
                command = random.randint(1, 4)

        elif (right[0] == "i" and down[0] == "i"):
            command = random.randint(2, 3)
        elif (left[0] == "i" and down[0] == "i"):
            command = random.randint(3, 4)
        elif (up[0] == "i" and right[0] == "i"):
            command = random.randint(1, 2)
        elif (up[0] == "i" and left[0] == "i"):
            command = 1
        else:
            command = random.randint(1, 4)

    return command


def ActPirate(pirate):
    d = pirate.getDimensionX()

    originX = pirate.getDeployPoint()[0]
    originY = pirate.getDeployPoint()[1]

    # Quad 1
    if (originX == d - 1 and originY == 0):
        return quad1(pirate, d)

    # Quad 2
    elif (originX == 0 and originY == 0):
        return quad2(pirate, d)

    # Quad 3
    elif (originX == 0 and originY == d - 1):
        return quad3(pirate, d)

    # Quad 4
    elif (originX == d - 1 and originY == d - 1):
        return quad4(pirate, d)


def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)

    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")