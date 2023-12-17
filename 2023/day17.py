from v2 import v2, pprintMatrix
import heapq


def dijkstrussy(data: dict[v2, int], minSteps: int, maxSteps: int) -> int:

    heap = [(data[v2(1, 0)], v2(1, 0), v2(1, 0), 0), (data[v2(0, 1)], v2(0, 1), v2(0, 1), 0)]
    visited = set()
    target = max(data)

    while len(heap) > 0:
        value, pos, direction, sameDir = heapq.heappop(heap)
        if pos == target and sameDir >= minSteps:
            return value
        if (pos, direction, sameDir) in visited:
            continue
        visited.add((pos, direction, sameDir))
        forward = pos + direction
        if sameDir < maxSteps - 1 and forward in data:
            heapq.heappush(heap, (value + data[forward], forward, direction, sameDir + 1))
        if sameDir >= minSteps:
            perp = v2(direction.y, -direction.x)
            left, right = pos + perp, pos - perp
            if left in data:
                heapq.heappush(heap, (value + data[left], left, perp, 0))
            if right in data:
                heapq.heappush(heap, (value + data[right], right, -perp, 0))

        

with open("2023/day17-input.txt", "r") as f:
    data = {v2(x, y): int(c) for y, r in enumerate(f.read().split("\n")) for x, c in enumerate(r)}
    
    print(dijkstrussy(data, 0, 3), dijkstrussy(data, 3, 10))
    