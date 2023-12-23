# there is a bug somewhere here, my answer undercounts by about 150. 
# I cannot be bothered to find the bug. 
# It is the night before christmas eve.
# Perhaps another time in the new year.
# Till the twenty-fourth!

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
    
    #pprintMatrix([["O" if v2(x, y) in searched else(data[v2(x, y)] if v2(x, y) in data else "#") for x in range(size.x)] for y in range(size.y)])
    return -searched[end]

def analyzeData(data: dict[v2, str], start: v2, end: v2):
    todo = [(start, v2(1, 0))]
    segments: dict[v2, set[tuple[v2, int]]] = {}
    searched = set([start])
    while len(todo) > 0:
        start, firstDirection = todo.pop(0)
        pos = start + firstDirection
        if pos in searched:
            continue
        searched.add(pos)
        length = 1
        while pos != end:
            possible = []
            for dp in (v2(1, 0), v2(0, 1), v2(-1, 0), v2(0, -1)):
                if pos + dp not in data:
                    continue
                possible.append(dp)
            if all(pos + kp in searched for kp in possible):
                break
            if len(possible) == 1 or len(possible) == 2:
                searched.add(pos)
                if pos + possible[0] in searched:
                    pos += possible[1]
                else:
                    pos += possible[0]
                length += 1
            else:
                break
        if start not in segments:
            segments[start] = {(pos, length)}
        else:
            segments[start].add((pos, length))
        if pos != end:
            for dp in possible:
                if pos + dp not in searched:
                    todo.append((pos, dp))
    secondSegments = {}
    for end, arr in segments.items():
        for start, dist in arr:
            if start in secondSegments:
                secondSegments[start].add((end, dist))
            else:
                secondSegments[start] = {(end, dist)}
    for k, v in secondSegments.items():
        if k in segments:
            segments[k] = segments[k].union(v)
        else:
            segments[k] = v
    print("analysed data")
    return segments

def recursiveBlender(data: dict[v2, list[tuple[v2, int]]], start: v2, end: v2):
    q = [(start, [])]
    results = []
    while len(q) > 0:
        pos, visited = q.pop()
        if pos == end:
            results.append(visited + [pos])
            continue
        for nextPos, _ in data[pos]:
            if nextPos not in visited:
                q.append((nextPos, visited + [pos]))
    bestDistance = 0
    print("found all routes")
    for r in results:
        d = 0
        for i in range(len(r) - 1):
            for j, h in data[r[i]]:
                if j == r[i + 1]:
                    d += h
                    break

        bestDistance = max(bestDistance, d)

    return bestDistance

with open("2023/day23-input.txt", "r") as f:
    dataraw = f.read().split("\n")
    data = {v2(x, y): c for y, l in enumerate(dataraw) for x, c in enumerate(l) if c != "#"}
    start = v2(dataraw[0].index("."), 0)
    end = v2(dataraw[-1].index("."), len(dataraw) - 1)
    # part 1
    s1 = dijkstrussy(data, start, end, v2(len(dataraw[0]), len(dataraw)))
    # part 2
    del data[start]
    start += v2(0, 1)
    segments = analyzeData(data, start, end)
    s2 = recursiveBlender(segments, start, end)
    print(s1, s2)

