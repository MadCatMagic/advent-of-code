
def fopen():
    with open("day12/day12-input.txt", "r") as f:
        data = f.read().strip().split("\n")
        s = None
        e = None
        for x, l in enumerate(data):
            for y, c in enumerate(l):
                if c == "S":
                    s = (x, y)
                    data[x] = data[x].replace("S", "a")
                if c == "E":
                    e = (x, y)
                    data[x] = data[x].replace("E", "z")
        return data, s, e

# part 1
data, s, e = fopen()
minMap = [[10000 for _ in i] for i in data]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
size = (len(data), len(data[0]))

def outOfBounds(x, y):
    global size
    return not (0 <= x < size[0] and 0 <= y < size[1])

# original algorithm
# used recursion:
# would look through each neighbours of the inputed coordinates to see whether they could be traversed more efficiently
# inversion is for part two so instead of checking for walkable up terrain, it checks in reverse
# slow, works for part one but part two causes a recursion error for exceeding the stack limit
def checkOLD(x, y, v, invert):
    minMap[x][y] = v
    for dir in dirs:
        nx = x + dir[0]
        ny = y + dir[1]
        if outOfBounds(nx, ny):
            continue
        if minMap[nx][ny] > v + 1:
            # part 2
            if invert:
                if ord(data[x][y]) <= ord(data[nx][ny]) + 1:
                    check(nx, ny, v + 1, invert)
            # part 1
            else:
                if ord(data[x][y]) >= ord(data[nx][ny]) - 1:
                    check(nx, ny, v + 1, invert)

# better version
# instead of using recursion, uses a list of 'items' to be processed
# much faster as does not need to iterate over the same position many times to get the minimum value
# works for part 2
def check(x, y, v, invert):
    toProcess = [(x, y, v)]
    while True:
        new = []
        for item in toProcess:
            if minMap[item[0]][item[1]] <= item[2]:
                continue
            minMap[item[0]][item[1]] = item[2]
            for dir in dirs:
                nx = item[0] + dir[0]
                ny = item[1] + dir[1]
                if outOfBounds(nx, ny):
                    continue
                if minMap[nx][ny] > item[2] + 1:
                    # part 2
                    if invert:
                        if ord(data[item[0]][item[1]]) <= ord(data[nx][ny]) + 1:
                            new.append((nx, ny, item[2] + 1))
                    # part 1
                    else:
                        if ord(data[item[0]][item[1]]) >= ord(data[nx][ny]) - 1:
                            new.append((nx, ny, item[2] + 1))
        if len(new) == 0:
            return
        toProcess = new

check(s[0], s[1], 0, False)
print(minMap[e[0]][e[1]])
# f = open("day12/test.txt", "w")
# f.write("\n".join([" ".join([str(x) + " " * (3 - len(str(x))) if x != 10000 else "   " for x in line]) for line in minMap]))
# f.close()

# part 2
minMap = [[10000 for _ in i] for i in data]
check(e[0], e[1], 0, True)

best = 100000
for y, r in enumerate(minMap):
    for x, v in enumerate(r):
        if data[y][x] == "a" and v < best:
            best = v
print(best)