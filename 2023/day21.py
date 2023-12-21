from v2 import v2, pprintMatrix, reverseLookup
import heapq

def dijkstrussy(data: dict[v2, str], start: v2, stepsNeeded: int):
    dirs = (v2(1, 0), v2(0, 1), v2(-1, 0), v2(0, -1))
    q = [(0, start)]
    visited = set()
    while len(q) > 0:
        stepsTaken, pos = heapq.heappop(q)
        if (pos, stepsTaken) in visited:
            continue
        visited.add((pos, stepsTaken))
        if stepsTaken + 1 > stepsNeeded:
            continue
        for step in dirs:
            newPos = pos + step
            if newPos in data:
                heapq.heappush(q, (stepsTaken + 1, newPos))
    s = 0
    for pos in data.keys():
        if (pos, stepsTaken) in visited:
            s += 1
    return s

with open("2023/day21-input.txt", "r") as f:
    data = {v2(x, y): c for y, line in enumerate(f.read().split()) for x, c in enumerate(line) if c != "#"}
    start = reverseLookup(data, "S")
    # part 1
    s1 = dijkstrussy(data, start, 64)

    # part 2
    # how...
    

    print(s1)
