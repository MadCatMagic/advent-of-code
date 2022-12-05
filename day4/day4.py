
def fopen():
    with open("day4/day4-input.txt", "r") as f:
        data = f.read().split("\n")
        # data structures amiright
        return [[[int(n) for n in s.split("-")] for s in l.split(",")] for l in data]

# part 1
def contains(pair1, pair2):
    return 1 if \
        pair1[0] >= pair2[0] and pair1[1] <= pair2[1] or \
        pair1[0] <= pair2[0] and pair1[1] >= pair2[1] else 0

data = fopen()
print(sum([contains(a, b) for a, b in data]))

# part 2
def overlap(pair1, pair2):
    for i in range(pair2[0], pair2[1] + 1):
        if pair1[0] <= i <= pair1[1]:
            return 1
    return 0

print(sum([overlap(a, b) for a, b in data]))