def fopen():
    with open("day9/day9-input.txt", "r") as f:
        data = f.read().strip().split("\n")
        return [({"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}[d], int(n)) for d, n in [line.split(" ") for line in data]]

data = fopen()
# part 1
hx = 0
hy = 0
tx = 0
ty = 0
visited = {(0, 0)}
for i in data:
    for j in range(i[1]):
        prevx, prevy = hx, hy
        hx += i[0][0]
        hy += i[0][1]
        if not (hx - 1 <= tx <= hx + 1 and hy - 1 <= ty <= hy + 1):
            tx = prevx
            ty = prevy
        visited.add((tx, ty))
print(len(visited))

# part 2
segments = [(0, 0) for _ in range(10)]
visited = {(0, 0)}
for i in data:
    for j in range(i[1]):
        # move first head
        segments[0] = (segments[0][0] + i[0][0], segments[0][1] + i[0][1])
        # ripple back through knots
        for k in range(len(segments) - 1):
            if not (segments[k][0] - 1 <= segments[k + 1][0] <= segments[k][0] + 1 and 
                    segments[k][1] - 1 <= segments[k + 1][1] <= segments[k][1] + 1):
                # took me ages
                # because the movement is always the difference scaled to ones e.g. (-2, 1) -> (-1, 1), (0, 2) -> (0, 1)
                diff = (segments[k][0] - segments[k + 1][0], segments[k][1] - segments[k + 1][1])
                diff = (diff[0] // 2 if abs(diff[0]) > 1 else diff[0], diff[1] // 2 if abs(diff[1]) > 1 else diff[1])
                segments[k + 1] = (segments[k + 1][0] + diff[0], segments[k + 1][1] + diff[1])
        visited.add(segments[-1])
print(len(visited))