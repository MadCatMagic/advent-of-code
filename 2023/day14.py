
from v2 import pprintMatrix, rotateMatrixCW

def tiltNorth(data):
    while True:
        changed = False
        for y, el in enumerate(data):
            if y == 0:
                continue
            for x, c in enumerate(el):
                if c == "O" and data[y - 1][x] == ".":
                    data[y - 1][x] = "O"
                    data[y][x] = "."
                    changed = True
        if not changed:
            return data

from copy import deepcopy

with open("2023/day14-input.txt", "r") as f:
    data = [list(s) for s in f.read().split("\n")]

    # part 1
    tilted = tiltNorth(deepcopy(data))
    s1 = 0
    for i, r in enumerate(tilted):
        for c in r:
            if c == "O":
                s1 += len(data) - i
    
    # part 2
        
    print(s1)