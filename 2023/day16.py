from v2 import v2, pprintMatrix

dirs = {
    0: v2(1, 0),
    1: v2(0, 1),
    2: v2(-1, 0),
    3: v2(0, -1)
}
results = {
    (0, "\\"): (-1, 1),
    (0, "/"):  (-1, 3),
    (0, "|"):  (-1, 1, 3),
    (1, "\\"): (-1, 0),
    (1, "/"):  (-1, 2),
    (1, "-"):  (-1, 0, 2),
    (2, "\\"): (-1, 3),
    (2, "/"):  (-1, 1),
    (2, "|"):  (-1, 1, 3),
    (3, "\\"): (-1, 2),
    (3, "/"):  (-1, 0),
    (3, "-"):  (-1, 0, 2)
}
def propagateBeam(data: list[str], map: list[list[list[int]]], start: v2, dir: int):

    left = 0
    if dir == 0:   left = len(map[0]) - start.x
    elif dir == 1: left = len(map) - start.y
    elif dir == 2: left = start.x + 1
    elif dir == 3: left = start.y + 1

    for i in range(1, left):
        p = start + dirs[dir] * i
        c = data[p.y][p.x]
        if (dir, c) in results:
            newDirs = results[(dir, c)]

            for d in newDirs:
                if d == -1:
                    continue
                if d not in map[p.y][p.x]:
                    map[p.y][p.x].append(d)
                    propagateBeam(data, map, p, d)

            return
        map[p.y][p.x].append(dir)



#  3
#2 # 0
#  1
with open("2023/day16-input.txt") as f:
    data = f.read().split("\n")

    # part 1
    secondMap = [[[] for _ in r] for r in data]
    try:
        secondMap[0][0] = list(results[(0, data[0][0])][1:])
    except KeyError:
        secondMap[0][0] = [0]
    propagateBeam(data, secondMap, v2(0, 0), secondMap[0][0][0])
    s1 = sum([len(el) > 0 for el in row].count(True) for row in secondMap)

    # part 2
    s2 = 0
    for y in range(len(data)):
        # going ->
        secondMap = [[[] for _ in r] for r in data]
        try:
            secondMap[y][0] = list(results[(0, data[y][0])][1:])
        except KeyError:
            secondMap[y][0] = [0]
        propagateBeam(data, secondMap, v2(0, y), secondMap[y][0][0])
        s2 = max(s2, sum([len(el) > 0 for el in row].count(True) for row in secondMap))
    for y in range(len(data)):
        # going <-
        secondMap = [[[] for _ in r] for r in data]
        try:
            secondMap[y][-1] = list(results[(2, data[y][-1])][1:])
        except KeyError:
            secondMap[y][-1] = [2]
        propagateBeam(data, secondMap, v2(len(data[0]) - 1, y), secondMap[y][-1][0] if secondMap[y][-1][0] != 0 else 2)
        s2 = max(s2, sum([len(el) > 0 for el in row].count(True) for row in secondMap))
    for x in range(len(data[0])):
        # going \/
        secondMap = [[[] for _ in r] for r in data]
        try:
            secondMap[0][x] = list(results[(1, data[0][x])][1:])
        except KeyError:
            secondMap[0][x] = [1]
        propagateBeam(data, secondMap, v2(x, 0), secondMap[0][x][0])
        s2 = max(s2, sum([len(el) > 0 for el in row].count(True) for row in secondMap))
    for x in range(len(data[0])):
        # going /\
        secondMap = [[[] for _ in r] for r in data]
        try:
            secondMap[-1][x] = list(results[(3, data[-1][x])][1:])
        except KeyError:
            secondMap[-1][x] = [3]
        propagateBeam(data, secondMap, v2(x, len(data) - 1), secondMap[-1][x][0] if secondMap[-1][x][0] != 1 else 3)
        s2 = max(s2, sum([len(el) > 0 for el in row].count(True) for row in secondMap))
    
    print(s1, s2)