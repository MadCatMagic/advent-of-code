def findNext(arr):
    summed = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    if summed.count(0) == len(summed):
        return arr[-1]
    return arr[-1] + findNext(summed)

def findPrev(arr):
    summed = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    if summed.count(0) == len(summed):
        return arr[0]
    return arr[0] - findPrev(summed)

with open("2023/day9-input.txt", "r") as f:
    data = [[int(k) for k in l.split()] for l in f.read().split("\n")]

    # part 1
    s1 = sum(findNext(l) for l in data)

    # part 2
    s2 = sum(findPrev(l) for l in data)

    print(s1, s2)
