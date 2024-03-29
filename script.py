import random
# import math

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


def IslandCenter_and_Number(pirate):
    Investigate = PirateInvestigate(pirate)

    IslandTiles = ""
    IslandNo = 0

    for key, value in Investigate.items():
        if value[0][0:-1] == "island":
            IslandTiles += "1"
            if IslandNo != 0:
                continue
            else:
                IslandNo = int(value[0][-1])
        else:
            IslandTiles += "0"

    IslandCenterPoint = (0, 0)

    # 1
    if IslandTiles == "000000001":
        IslandCenterPoint = (pirate.getPosition()[0] + 2, pirate.getPosition()[1] + 2)

    # 2
    if IslandTiles == "001000001":
        IslandCenterPoint = (pirate.getPosition()[0] + 1, pirate.getPosition()[1] + 2)

    # 3
    if IslandTiles == "001000011":
        IslandCenterPoint = (pirate.getPosition()[0], pirate.getPosition()[1] + 2)

    # 4
    if IslandTiles == "0010000010":
        IslandCenterPoint = (pirate.getPosition()[0] - 1, pirate.getPosition()[1] + 2)

    # 5
    if IslandTiles == "000000010":
        IslandCenterPoint = (pirate.getPosition()[0] - 2, pirate.getPosition()[1] + 2)

    # 6
    if IslandTiles == "000100010":
        IslandCenterPoint = (pirate.getPosition()[0] - 2, pirate.getPosition()[1] + 1)

    # 7
    if IslandTiles == "000101010":
        IslandCenterPoint = (pirate.getPosition()[0] - 2, pirate.getPosition()[1])

    # 8
    if IslandTiles == "000101000":
        IslandCenterPoint = (pirate.getPosition()[0] - 2, pirate.getPosition()[1] - 1)

    # 9
    if IslandTiles == "000001000":
        IslandCenterPoint = (pirate.getPosition()[0] - 2, pirate.getPosition()[1] - 2)

    # 10
    if IslandTiles == "010001000":
        IslandCenterPoint = (pirate.getPosition()[0] - 1, pirate.getPosition()[1] - 2)

    # 11
    if IslandTiles == "010001100":
        IslandCenterPoint = (pirate.getPosition()[0], pirate.getPosition()[1] - 2)

    # 12
    if IslandTiles == "010000100":
        IslandCenterPoint = (pirate.getPosition()[0] + 1, pirate.getPosition()[1] - 2)

    # 13
    if IslandTiles == "000000100":
        IslandCenterPoint = (pirate.getPosition()[0] + 2, pirate.getPosition()[1] - 2)

    # 14
    if IslandTiles == "000010100":
        IslandCenterPoint = (pirate.getPosition()[0] + 2, pirate.getPosition()[1] - 1)

    # 15
    if IslandTiles == "000010101":
        IslandCenterPoint = (pirate.getPosition()[0] + 2, pirate.getPosition()[1])

    # 16
    if IslandTiles == "000010001":
        IslandCenterPoint = (pirate.getPosition()[0] + 2, pirate.getPosition()[1] + 1)

    return IslandCenterPoint, IslandNo


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


# def MoveAway(x, y, Pirate):
#     position = Pirate.getPosition()
#     if position[0] == x and position[1] == y:
#         return random.randint(1, 4)
#     if random.randint(1, 2) == 1:
#         return (position[0] < x) * 2 + 2
#     else:
#         return (position[1] > y) * 2 + 1


# def CircleAround(x, y, radius, Pirate, initial="abc", clockwise=True):
#     position = Pirate.getPosition()
#     rx = position[0]
#     ry = position[1]
#     pos = [[x + i, y + radius] for i in range(-1 * radius, radius + 1)]
#     pos.extend([[x + radius, y + i] for i in range(radius - 1, -1 * radius - 1, -1)])
#     pos.extend([[x + i, y - radius] for i in range(radius - 1, -1 * radius - 1, -1)])
#     pos.extend([[x - radius, y + i] for i in range(-1 * radius + 1, radius)])
#     if [rx, ry] not in pos:
#         if initial != "abc":
#             return MoveTowards(initial[0], initial[1], Pirate)
#         if rx in [x + i for i in range(-1 * radius, radius + 1)] and ry in [
#             y + i for i in range(-1 * radius, radius + 1)
#         ]:
#             return MoveAway(x, y, Pirate)
#         else:
#             return MoveTowards(x, y, Pirate)
#     else:
#         index = pos.index([rx, ry])
#         return MoveTowards(
#             pos[(index + (clockwise * 2) - 1) % len(pos)][0],
#             pos[(index + (clockwise * 2) - 1) % len(pos)][1],
#             Pirate,
#         )


############################################################################################


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


############################################################################################


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_balanced_bst(start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = TreeNode(mid + 1)
    root.left = build_balanced_bst(start, mid - 1)
    root.right = build_balanced_bst(mid + 1, end)
    return root


def level_order_traversal(root):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


def BinSearchTree_sequence(Num):
    bst_root = build_balanced_bst(0, Num - 1)
    return level_order_traversal(bst_root)


############################################################################################


def MovementBin(pirate):
    spawn = pirate.getDeployPoint()
    spawn = (round(spawn[0] / pirate.getDimensionX()) * pirate.getDimensionX(),
             round(spawn[1] / pirate.getDimensionY()) * pirate.getDimensionY())
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
    # MappingDiagPoints = map_to_midpoint(len(TargetDiagonal))
    MappingDiagPoints = BinSearchTree_sequence(len(TargetDiagonal))
    # MappingDiagPoints = MappingFunction(len(TargetDiagonal))

    if pirate.getPosition() == pirate.getDeployPoint():
        pirate.setSignal("01")  # First number abt Reached Diag, second number abt towards opponent_spawn

    TargetDiagonalX = TargetDiagonal[MappingDiagPoints[int(int(pirate.getID()) % len(TargetDiagonal))] - 1][0]
    TargetDiagonalY = TargetDiagonal[MappingDiagPoints[int(int(pirate.getID()) % len(TargetDiagonal))] - 1][1]

    MoveNumber = 0

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


def MovementRevBin(pirate):
    spawn = pirate.getDeployPoint()
    spawn = (round(spawn[0] / pirate.getDimensionX()) * pirate.getDimensionX(),
             round(spawn[1] / pirate.getDimensionY()) * pirate.getDimensionY())
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
    # MappingDiagPoints = map_to_midpoint(len(TargetDiagonal))
    MappingDiagPoints = BinSearchTree_sequence(len(TargetDiagonal))
    MappingDiagPoints.reverse()
    # MappingDiagPoints = MappingFunction(len(TargetDiagonal))

    if pirate.getPosition() == pirate.getDeployPoint():
        pirate.setSignal("01")  # First number abt Reached Diag, second number abt towards opponent_spawn

    TargetDiagonalX = TargetDiagonal[MappingDiagPoints[int(int(pirate.getID()) % len(TargetDiagonal))] - 1][0]
    TargetDiagonalY = TargetDiagonal[MappingDiagPoints[int(int(pirate.getID()) % len(TargetDiagonal))] - 1][1]

    MoveNumber = 0

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


'''
def MovementMid(pirate):
    spawn = pirate.getDeployPoint()
    spawn = (round(spawn[0] / pirate.getDimensionX()) * pirate.getDimensionX(),
             round(spawn[1] / pirate.getDimensionY()) * pirate.getDimensionY())
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
    # MappingDiagPoints = generate_sequence(len(TargetDiagonal))
    # MappingDiagPoints = MappingFunction(len(TargetDiagonal))

    if pirate.getPosition() == pirate.getDeployPoint():
        pirate.setSignal("01")  # First number abt Reached Diag, second number abt towards opponent_spawn

    TargetDiagonalX = TargetDiagonal[MappingDiagPoints[int(int(pirate.getID()) % len(TargetDiagonal))] - 1][0]
    TargetDiagonalY = TargetDiagonal[MappingDiagPoints[int(int(pirate.getID()) % len(TargetDiagonal))] - 1][1]

    MoveNumber = 0

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
'''


# Inspiration from MovementMid function
def MovementEnd(pirate):
    spawn = pirate.getDeployPoint()
    spawn = (round(spawn[0] / pirate.getDimensionX()) * pirate.getDimensionX(),
             round(spawn[1] / pirate.getDimensionY()) * pirate.getDimensionY())
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
    MappingDiagPoints.reverse()
    # MappingDiagPoints = generate_sequence(len(TargetDiagonal))
    # MappingDiagPoints = MappingFunction(len(TargetDiagonal))

    if pirate.getPosition() == pirate.getDeployPoint():
        pirate.setSignal("01")  # First number abt Reached Diag, second number abt towards opponent_spawn

    TargetDiagonalX = TargetDiagonal[MappingDiagPoints[int(int(pirate.getID()) % len(TargetDiagonal))] - 1][0]
    TargetDiagonalY = TargetDiagonal[MappingDiagPoints[int(int(pirate.getID()) % len(TargetDiagonal))] - 1][1]

    MoveNumber = 0

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


# EndA and EndB
# def MovementEndA(pirate):
#     spawn = pirate.getDeployPoint()
#     spawn = (round(spawn[0] / pirate.getDimensionX()) * pirate.getDimensionX(),
#              round(spawn[1] / pirate.getDimensionY()) * pirate.getDimensionY())
#     if spawn[0] == 0:
#         spawn = (1, spawn[1])
#     else:
#         spawn = (spawn[0] - 1, spawn[1])
#
#     if spawn[1] == 0:
#         spawn = (spawn[0], 1)
#     else:
#         spawn = (spawn[0], spawn[1] - 1)
#
#     opponent_spawn = (pirate.getDimensionX() - spawn[0], pirate.getDimensionY() - spawn[1])
#
#     TargetDiagonal = OppDiagonalPoints(spawn[0], spawn[1], opponent_spawn[0], opponent_spawn[1])
#     MappingDiagPoints = range(len(TargetDiagonal), 0, -1)
#     # MappingDiagPoints = generate_sequence(len(TargetDiagonal))
#     # MappingDiagPoints = MappingFunction(len(TargetDiagonal))
#
#     if pirate.getPosition() == pirate.getDeployPoint():
#         pirate.setSignal("01")  # First number abt Reached Diag, second number abt towards opponent_spawn
#
#     TargetDiagonalX = TargetDiagonal[MappingDiagPoints[int(int(pirate.getID()) % len(TargetDiagonal))] - 1][0]
#     TargetDiagonalY = TargetDiagonal[MappingDiagPoints[int(int(pirate.getID()) % len(TargetDiagonal))] - 1][1]
#
#     MoveNumber = 0
#
#     if (pirate.getSignal() == "01") and (pirate.getPosition() != (TargetDiagonalX, TargetDiagonalY)):
#         MoveNumber = MoveTowards(TargetDiagonalX, TargetDiagonalY, pirate)
#     elif (pirate.getSignal() == "01") and (pirate.getPosition() == (TargetDiagonalX, TargetDiagonalY)):
#         pirate.setSignal("11")
#     elif (pirate.getSignal() == "11") and pirate.getPosition() != opponent_spawn:
#         MoveNumber = MoveTowards(opponent_spawn[0], opponent_spawn[1], pirate)
#     elif (pirate.getSignal() == "11") and pirate.getPosition() == opponent_spawn:
#         pirate.setSignal("00")
#     elif (pirate.getSignal() == "00") and (pirate.getPosition() != (TargetDiagonalX, TargetDiagonalY)):
#         MoveNumber = MoveTowards(TargetDiagonalX, TargetDiagonalY, pirate)
#     elif (pirate.getSignal() == "00") and (pirate.getPosition() == (TargetDiagonalX, TargetDiagonalY)):
#         pirate.setSignal("10")
#     elif (pirate.getSignal() == "10") and (pirate.getPosition() != spawn):
#         MoveNumber = MoveTowards(spawn[0], spawn[1], pirate)
#     else:
#         pirate.setSignal("01")
#
#     return MoveNumber
#
#
# def MovementEndB(pirate):
#     spawn = pirate.getDeployPoint()
#     spawn = (round(spawn[0] / pirate.getDimensionX()) * pirate.getDimensionX(),
#              round(spawn[1] / pirate.getDimensionY()) * pirate.getDimensionY())
#     if spawn[0] == 0:
#         spawn = (1, spawn[1])
#     else:
#         spawn = (spawn[0] - 1, spawn[1])
#
#     if spawn[1] == 0:
#         spawn = (spawn[0], 1)
#     else:
#         spawn = (spawn[0], spawn[1] - 1)
#
#     opponent_spawn = (pirate.getDimensionX() - spawn[0], pirate.getDimensionY() - spawn[1])
#
#     TargetDiagonal = OppDiagonalPoints(spawn[0], spawn[1], opponent_spawn[0], opponent_spawn[1])
#     MappingDiagPoints = range(1, len(TargetDiagonal) + 1)
#     # MappingDiagPoints = generate_sequence(len(TargetDiagonal))
#     # MappingDiagPoints = MappingFunction(len(TargetDiagonal))
#
#     if pirate.getPosition() == pirate.getDeployPoint():
#         pirate.setSignal("01")  # First number abt Reached Diag, second number abt towards opponent_spawn
#
#     TargetDiagonalX = TargetDiagonal[MappingDiagPoints[int(int(pirate.getID()) % len(TargetDiagonal))] - 1][0]
#     TargetDiagonalY = TargetDiagonal[MappingDiagPoints[int(int(pirate.getID()) % len(TargetDiagonal))] - 1][1]
#
#     MoveNumber = 0
#
#     if (pirate.getSignal() == "01") and (pirate.getPosition() != (TargetDiagonalX, TargetDiagonalY)):
#         MoveNumber = MoveTowards(TargetDiagonalX, TargetDiagonalY, pirate)
#     elif (pirate.getSignal() == "01") and (pirate.getPosition() == (TargetDiagonalX, TargetDiagonalY)):
#         pirate.setSignal("11")
#     elif (pirate.getSignal() == "11") and pirate.getPosition() != opponent_spawn:
#         MoveNumber = MoveTowards(opponent_spawn[0], opponent_spawn[1], pirate)
#     elif (pirate.getSignal() == "11") and pirate.getPosition() == opponent_spawn:
#         pirate.setSignal("00")
#     elif (pirate.getSignal() == "00") and (pirate.getPosition() != (TargetDiagonalX, TargetDiagonalY)):
#         MoveNumber = MoveTowards(TargetDiagonalX, TargetDiagonalY, pirate)
#     elif (pirate.getSignal() == "00") and (pirate.getPosition() == (TargetDiagonalX, TargetDiagonalY)):
#         pirate.setSignal("10")
#     elif (pirate.getSignal() == "10") and (pirate.getPosition() != spawn):
#         MoveNumber = MoveTowards(spawn[0], spawn[1], pirate)
#     else:
#         pirate.setSignal("01")
#
#     return MoveNumber


def ActPirate(pirate):
    dim = pirate.getDimensionX()  # = pirate.getDimensionY()

    IslandData = IslandCenter_and_Number(pirate)
    IslandData = ((str(IslandData[0][0]), str(IslandData[0][1])), str(IslandData[1]))

    TeamSignal = str(pirate.getTeamSignal())
    TeamSignalParsed = TeamSignal.split(".")

    FoundIslands = []
    for i in TeamSignalParsed:
        if i != "":
            FoundIslands.append(str(i[0]))

    # Setting and Appending TeamSignal
    if IslandData[1] != "0" and IslandData[1] not in FoundIslands:
        NewSignal = pirate.getTeamSignal() + IslandData[1] + ":" + IslandData[0][0] + "," + IslandData[0][1] + "."
        pirate.setTeamSignal(NewSignal)
        FoundIslands.append(IslandData[1])
        # print(TeamSignalParsed)

    if (int(pirate.getID()) % 11 in range(8)) or pirate.getCurrentFrame() < int(dim * 2.25):
        # if int(pirate.getID()) % 5 == 0:
        #     return MovementMid(pirate)
        # elif int(pirate.getID()) % 5 == 1:
        #     return MovementEndA(pirate)
        # elif int(pirate.getID()) % 5 == 2:
        #     return MovementEndB(pirate)
        # elif int(pirate.getID()) % 5 == 3:
        #     # return CircleAround(dimX / 2, dimY / 2, int(dimX / 2), pirate)
        #     return MovementMid(pirate)
        # elif int(pirate.getID()) % 5 == 4:
        #     # return CircleAround(dimX / 2, dimY / 2, int(dimX / 2), pirate, clockwise=False)
        #     return MovementBin(pirate)
        if pirate.getCurrentFrame() < int(dim * 0.69):
            return MovementEnd(pirate)
        elif pirate.getCurrentFrame() < int(dim * 1.6):
            return MovementRevBin(pirate)
        else:
            return MovementBin(pirate)
    else:
        if str(int(pirate.getID()) % 11 - 7) in FoundIslands:

            PirateIslandData = ""

            for IslandCoordinates in TeamSignalParsed:
                if IslandCoordinates != "":
                    if IslandCoordinates[0] == str(int(pirate.getID()) % 11 - 7):
                        PirateIslandData += IslandCoordinates
                        break

            if PirateIslandData != "":
                PirateIslandCoordinateX = int(PirateIslandData.split(":")[1].split(",")[0]) + random.choice([1, 0, -1])
                PirateIslandCoordinateY = int(PirateIslandData.split(":")[1].split(",")[1]) + random.choice([1, 0, -1])

                return MoveTowards(PirateIslandCoordinateX, PirateIslandCoordinateY, pirate)
        else:
            return MovementBin(pirate)

    pass


# A function that takes a team as an argument, and is not expected to return anything.
# Ran on your team, to change team signals and to build walls.
def ActTeam(team):
    dim = team.getDimensionX()  # = team.getDimensionY()
    if team.getCurrentFrame() > int(dim * 2):
        team.buildWalls(1)
        team.buildWalls(2)
        team.buildWalls(3)
    pass
