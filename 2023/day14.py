
from util import rotateMatrixCW, rotateMatrixCCW

def tiltLeft(data: list[list[str]]):
    n = []
    for r in data:
        empty = 0
        roll = 0
        newr = ""
        for c in r:
            if c == "#":
                newr += "O" * roll + "." * empty + "#"
                empty, roll = 0, 0
            elif c == "O":
                roll += 1
            else:
                empty += 1
        newr += "O" * roll + "." * empty
        n.append(list(newr))
    return n

def countNorthSide(arr: list[list[str]]) -> int:
    s = 0
    for i, r in enumerate(arr):
        for c in r:
            if c == "O":
                s += len(data) - i
    return s

with open("2023/day14-input.txt", "r") as f:
    data = [list(s) for s in f.read().split("\n")]

    # part 1
    tilted = tiltLeft(rotateMatrixCCW(data))
    s1 = countNorthSide(rotateMatrixCW(tilted))
    
    # part 2
    arr = [rotateMatrixCCW(data)]
    i = 0
    s2 = 0
    while True:
        # perform an iteration
        tilted = tiltLeft(arr[-1])
        tilted = tiltLeft(rotateMatrixCW(tilted))
        tilted = tiltLeft(rotateMatrixCW(tilted))
        tilted = tiltLeft(rotateMatrixCW(tilted))
        last = rotateMatrixCW(tilted)
        
        # test for a cycle
        for j, el in enumerate(arr):
            if el == last:
                # cycle found, work out result and exit loop
                cycleLength = i + 1 - j
                iterationsLeft = 1_000_000_000 - i - 1
                target = iterationsLeft % cycleLength
                index = j + target
                s2 = countNorthSide(rotateMatrixCW(arr[index]))
        
        if s2 != 0:
            break
        arr.append(last)
        i += 1
    
    print(s1, s2)