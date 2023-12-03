
def fopen():
    with open("day8/day8-input.txt", "r") as f:
        data = f.read().strip().split("\n")
        return data

def seeHoriz(data, y, a, b):
    dist = 0
    for dx in range(a, b, 1 if a <= b else -1):
        dist += 1
        if data[y][dx] >= h:
            return False, dist
    return True, dist

def seeVert(data, x, a, b):
    dist = 0
    for dy in range(a, b, 1 if a <= b else -1):
        dist += 1
        if data[dy][x] >= h:
            return False, dist
    return True, dist

data = fopen()
count = 0
scenic = 0
for y, row in enumerate(data):
    for x, h in enumerate(row):
        
        horizRight, hr = seeHoriz(data, y, x - 1, -1)
        horizLeft, hl = seeHoriz(data, y, x + 1, len(row))
        vertTop, vt = seeVert(data, x, y - 1, -1)
        vertBottom, vb = seeVert(data, x, y + 1, len(data))

        if True in (horizRight, horizLeft, vertTop, vertBottom):
            count += 1
            scenic = max(scenic, hr * hl * vt * vb)
        
# part 1
print(count)
# part 2
print(scenic)