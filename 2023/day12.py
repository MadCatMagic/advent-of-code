from functools import cache

@cache
def matchIt(line: str, values: tuple[int]) -> int:
    count = 0

    if len(values) > 1:
        # create a 'moving selection' of values[0] chars and if they are valid,
        # recur, removing those particular values and one extra character
        # (provided that extra character is not '#')
        for i in range(len(line) - values[0] + 1):
            char = line[i:i + values[0]]
            if char.count('.') == 0 and line[i + values[0]] != "#" and (line[:i].count("#") == 0):
                count += matchIt(line[i + values[0] + 1:], values[1:])
    else:
        # work out smallest set that could fit here
        # if it is larger than values[0], return 0
        # else, return how many ways it can be contained in the larger set
        # first = 3, last = 5, smallest = 3, len = 6, lenl = 8
        first = line.find("#")
        if first != -1:
            last = len(line) - line[::-1].find("#") - 1
            smallest = last - first + 1
            if smallest > values[0]:
                return 0
            # i think works
            for i in range(max(0, last - values[0] + 1), min(len(line) - values[0] + 1, first + 1)):
                if line[i:i + values[0]].count('.') == 0:
                    count += 1
        else:
            for i in range(len(line) - values[0] + 1):
                if line[i:i + values[0]].count('.') == 0:
                    count += 1

    return count

with open("2023/day12-input.txt", "r") as f:
    data = [k.split() for k in f.read().split("\n")]
    data = [(a, tuple(int(c) for c in b.split(","))) for a, b in data]
    
    # part 1
    s1 = 0
    for line, values in data:
        s1 += matchIt(line + ".", values)

    # part 2
    s2 = 0
    for line, values in data:
        s2 += matchIt("?".join(line for _ in range(5)) + ".", values * 5)
    print(s1, s2)