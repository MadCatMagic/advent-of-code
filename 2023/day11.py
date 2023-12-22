from vec import v2
from util import pprintMatrix
from itertools import combinations
from copy import deepcopy

with open("2023/day11-input.txt", "r") as f:
    data = f.read().split("\n")
    data2 = deepcopy(data)

    # time dilation
    e = 0
    for i in range(len(data[0])):
        add = True
        for j in range(len(data)):
            if data[j][i + e] == "#":
                add = False
        if add:
            for j, l in enumerate(data):
                data[j] = l[:i + e] + "|" + l[i + e:]
                data2[j] = data2[j][:i] + "|" + data2[j][i + 1:]
            e += 1
    e = 0
    for i in range(len(data)):
        if data[i + e].find("#") == -1:
            line = "".join("+" if c == "|" else "-" for j, c in enumerate(data2[0]))
            data.insert(i + e + 1, "." * len(data[0]))
            data2[i] = line
            e += 1

    # part 1
    stars = []
    for y, l in enumerate(data):
        for x, c in enumerate(l):
            if c == "#":
                stars.append(v2(x, y))

    s1 = 0
    for a, b in combinations(stars, 2):
        s1 += abs(a.x - b.x) + abs(a.y - b.y)

    # part 2
    stars = []
    mul = 1000000
    yextra = 0
    pprintMatrix(data2, 0)
    for y, l in enumerate(data2):
        xextra = 0
        if l[0] == "-":
            yextra += mul - 1
            continue

        for x, c in enumerate(l):
            if c == "|":
                xextra += mul - 1
                continue
            elif c == "#":
                stars.append(v2(x + xextra, y + yextra))

    s2 = 0
    for a, b in combinations(stars, 2):
        s2 += abs(a.x - b.x) + abs(a.y - b.y)
    
    print(s1, s2)
    # part 2
