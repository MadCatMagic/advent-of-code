from v2 import v2, pprintMatrix, reverseLookup
from numpy import polyfit, polyval
import heapq

def dijkstrussy(data: dict[v2, str], start: v2, stepsNeeded: int, mod: bool = True, size: int = 0):
    dirs = (v2(1, 0), v2(0, 1), v2(-1, 0), v2(0, -1))
    q = [(0, start)]
    visited = {}
    last = 0
    while len(q) > 0:
        stepsTaken, pos = heapq.heappop(q)
        if pos in visited and stepsTaken >= visited[pos]:
            continue
        visited[pos] = stepsTaken
        if stepsTaken + 1 > stepsNeeded:
            continue
        for step in dirs:
            newPos = pos + step
            if newPos in visited and visited[newPos] <= stepsTaken + 1:
                continue
            if mod and v2(newPos.x % size, newPos.y % size) in data or not mod and newPos in data:
                heapq.heappush(q, (stepsTaken + 1, newPos))
    s = 0
    for p, v in visited.items():
        if v % 2 == stepsNeeded % 2:
            s += 1
    return s

with open("2023/day21-input.txt", "r") as f:
    rawdata = f.read().split("\n")
    data = {v2(x, y): c for y, line in enumerate(rawdata) for x, c in enumerate(line) if c != "#"}
    start = reverseLookup(data, "S")
    # part 1
    print("doing part 1")
    s1 = dijkstrussy(data, start, 64, False)
    print("part 1 =", s1)

    # part 2
    size = len(rawdata)
    firstStep = 26501365 % size
    print("part two\ndoing n1...")
    n1 = dijkstrussy(data, start, firstStep, size=size)
    print("doing n2...")
    n2 = dijkstrussy(data, start, firstStep + size, size=size)
    print("doing n3...")
    n3 = dijkstrussy(data, start, firstStep + size * 2, size=size)
    print("calculating poly...")
    poly = polyfit((firstStep, firstStep + size, firstStep + size * 2), (n1, n2, n3), 2)
    print(n1, n2, n3, poly)
    s2 = polyval(poly, 26501365)
    # this is fucking crazy
    print("part 2 =", round(s2))
