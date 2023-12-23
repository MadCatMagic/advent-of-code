from vec import v2
from util import pprintMatrix
import heapq

directions = {
    v2(1, 0): ">",
    v2(0, 1): "v",
    v2(-1, 0): "<",
    v2(0, -1): "^"
}

def dijkstrussy(data: dict[v2, str], start: v2, end: v2, size: v2):
    q = [(0, start, v2())]
    searched = {}
    # searching for longest path so every step should 'decrease' the distance
    while len(q) > 0:
        d, pos, prevDir = heapq.heappop(q)
        searched[pos] = d
        
        for dp in (v2(1, 0), v2(0, 1), v2(-1, 0), v2(0, -1)):
            if dp == -prevDir:
                continue
            newPos = pos + dp
            if newPos not in data or newPos in searched and searched[newPos] <= d - 1:
                continue
            if data[newPos] != "." and directions[dp] != data[newPos]:
                continue
            heapq.heappush(q, (d - 1, newPos, dp))
    
    pprintMatrix([["O" if v2(x, y) in searched else(data[v2(x, y)] if v2(x, y) in data else "#") for x in range(size.x)] for y in range(size.y)])
    return -searched[end]

                

with open("2023/day23-input.txt", "r") as f:
    dataraw = f.read().split("\n")
    data = {v2(x, y): c for y, l in enumerate(dataraw) for x, c in enumerate(l) if c != "#"}
    start = dataraw[0].index(".")
    end = dataraw[-1].index(".")
    # part 1
    s1 = dijkstrussy(data, v2(start, 0), v2(end, len(dataraw) - 1), v2(len(dataraw[0]), len(dataraw)))
    print(s1)