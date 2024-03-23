import random

name = "NullCode!"


def PirateInvestigate(pirate):
    return {"O": pirate.investigate_current(),
            "N": pirate.investigate_up(),
            "S": pirate.investigate_down(),
            "W": pirate.investigate_left(),
            "E": pirate.investigate_right(),
            "NW": pirate.investigate_nw(),
            "NE": pirate.investigate_ne(),
            "SW": pirate.investigate_sw(),
            "SE": pirate.investigate_se()}


def MoveTowards(x, y, Pirate):
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


def MoveAway(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return random.randint(1, 4)
    if random.randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1


def circleAround(x, y, radius, Pirate, initial="abc", clockwise=True):
    position = Pirate.getPosition()
    rx = position[0]
    ry = position[1]
    pos = [[x + i, y + radius] for i in range(-1 * radius, radius + 1)]
    pos.extend([[x + radius, y + i] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x + i, y - radius] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x - radius, y + i] for i in range(-1 * radius + 1, radius)])
    if [rx, ry] not in pos:
        if initial != "abc":
            return MoveTowards(initial[0], initial[1], Pirate)
        if rx in [x + i for i in range(-1 * radius, radius + 1)] and ry in [
            y + i for i in range(-1 * radius, radius + 1)
        ]:
            return MoveAway(x, y, Pirate)
        else:
            return MoveTowards(x, y, Pirate)
    else:
        index = pos.index([rx, ry])
        return MoveTowards(
            pos[(index + (clockwise * 2) - 1) % len(pos)][0],
            pos[(index + (clockwise * 2) - 1) % len(pos)][1],
            Pirate,
        )


def OppDiagonalPoints(x1, y0, x0, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    if dx > dy:
        err = dx / 2.0
        while x != x1:
            points.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            points.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    points.append((x, y))
    return points


def map_to_midpoint(n):
    sequence = list(range(1, n + 1))
    midpoint_index = (n - 1) // 2
    result = [sequence[midpoint_index]]
    for i in range(1, midpoint_index + 1):
        if midpoint_index + i < n:
            result.append(sequence[midpoint_index + i])
        result.append(sequence[midpoint_index - i])
    if n % 2 == 0:
        result.append(sequence[-1])
    return result


def select_using_binsearch_pattern(arr, start, end, result):
    if start > end:
        return
    if start == end:
        result.append(arr[start])
        return

    mid = (start + end) // 2
    result.append(arr[mid])

    # Recursively apply the same logic to the left and right halves
    select_using_binsearch_pattern(arr, start, mid - 1, result)
    select_using_binsearch_pattern(arr, mid + 1, end, result)


def map_with_binsearch_algorithm(n):
    sequence = list(range(1, n + 1))
    result = []
    select_using_binsearch_pattern(sequence, 0, n - 1, result)
    return result


def ActPirate(pirate):
    Investigate = PirateInvestigate(pirate)


    spawn = pirate.getDeployPoint()
    spawn = (round(spawn[0] / pirate.getDimensionX()) * pirate.getDimensionX(), round(spawn[1] / pirate.getDimensionY()) * pirate.getDimensionY())
    if spawn[0] == 0:
        spawn = (1, spawn[1])
    else:
        spawn = (spawn[0] - 1, spawn[1])

    if spawn[1] == 0:
        spawn = (spawn[0], 1)
    else:
        spawn = (spawn[0], spawn[1] - 1)

    opponent_spawn = (pirate.getDimensionX() - spawn[0], pirate.getDimensionY() - spawn[1])

    TargetDiagonal = OppDiagonalPoints(spawn[0], spawn[1], opponent_spawn[0], opponent_spawn[1])
    MappingDiagPoints = map_to_midpoint(len(TargetDiagonal))
    if pirate.getPosition() == pirate.getDeployPoint():
        pirate.setSignal("01")  # First number abt Reached Diag, second number abt towards opponent_spawn

    TargetDiagonalX = TargetDiagonal[MappingDiagPoints[int(int(pirate.getID()) % len(TargetDiagonal))] - 1][0]
    TargetDiagonalY = TargetDiagonal[MappingDiagPoints[int(int(pirate.getID()) % len(TargetDiagonal))] - 1][1]

    MoveNumber = 0
    # if int(pirate.getID()) % 10 in range(10):
    if True:
        if (pirate.getSignal() == "01") and (pirate.getPosition() != (TargetDiagonalX, TargetDiagonalY)):
            MoveNumber = MoveTowards(TargetDiagonalX, TargetDiagonalY, pirate)
        elif (pirate.getSignal() == "01") and (pirate.getPosition() == (TargetDiagonalX, TargetDiagonalY)):
            pirate.setSignal("11")
        elif (pirate.getSignal() == "11") and pirate.getPosition() != opponent_spawn:
            MoveNumber = MoveTowards(opponent_spawn[0], opponent_spawn[1], pirate)
        elif (pirate.getSignal() == "11") and pirate.getPosition() == opponent_spawn:
            pirate.setSignal("00")
        elif (pirate.getSignal() == "00") and (pirate.getPosition() != (TargetDiagonalX, TargetDiagonalY)):
            MoveNumber = MoveTowards(TargetDiagonalX, TargetDiagonalY, pirate)
        elif (pirate.getSignal() == "00") and (pirate.getPosition() == (TargetDiagonalX, TargetDiagonalY)):
            pirate.setSignal("10")
        elif (pirate.getSignal() == "10") and (pirate.getPosition() != spawn):
            MoveNumber = MoveTowards(spawn[0], spawn[1], pirate)
        else:
            pirate.setSignal("01")

    return MoveNumber
    pass

    # A function that takes a team as an argument, and is not expected to return anything.
    # Ran on your team, to change team signals and to build walls.


def ActTeam(team):
    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
    pass
