from util import transposeMatrix

def findMirror(arr):
    vals = []
    for i in range(1, len(arr)):
        for j in range(1, len(arr)):
            if i - j < 0 or i + j - 1 >= len(arr):
                vals.append(i)
                break
            if arr[i - j] != arr[i + j - 1]:
                break
    if vals == []:
        return [-1]
    return vals

from copy import deepcopy
def findSmudge(k):
    r = findMirror(k)[0]
    c = findMirror(transposeMatrix(k))[0]
    summ = r * 100 if r != -1 else c
    for i, el in enumerate(k):
        for j, c in enumerate(el):
            newk = deepcopy(k)
            newk[i] = newk[i][:j] + {".": "#", "#": "."}[c] + newk[i][j+1:]
            row = findMirror(newk)
            col = findMirror(transposeMatrix(newk))
            for rp in row:
                for cp in col:
                    if rp != -1 or cp != -1:
                        vk = rp * 100 if rp != -1 else cp
                        if vk != summ:
                            return vk
                        if rp != -1 and cp != -1:
                            if r != rp:
                                return rp * 100
                            else:
                                return cp

with open("2023/day13-input.txt", "r") as f:
    data = [k.split("\n") for k in f.read().split("\n\n")]

    # part 1
    s1 = 0
    for k in data:
        row = findMirror(k)[0]
        col = findMirror(transposeMatrix(k))[0]
        s1 += row * 100 if row != -1 else col

    s2 = 0
    o = 0
    for k in data:
        s2 += findSmudge(k)
        print(s2 - o)
        o = s2

    print(s1, s2)