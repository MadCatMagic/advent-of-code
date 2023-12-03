def fopen():
    with open("day10/day10-input.txt", "r") as f:
        data = f.read().strip().split("\n")
        return [line.split(" ") for line in data]

data = fopen()

# part 1
def check(x, c):
    if (c + 20) % 40 == 0:
        return x * c
    return 0
x = 1
c = 0
s = 0
for i in data:
    if i[0] == "noop":
        c += 1
        s += check(x, c)
    elif i[0] == "addx":
        c += 1
        s += check(x, c)
        c += 1
        s += check(x, c)
        x += int(i[1])
print(s)

# part 2
x = 1
c = 0
d = []
def tick():
    global c, d, x
    c += 1
    if abs(x - (c - 1) % 40) <= 1:
        d.append("#")
    else:
        d.append(" ")
    if c % 40 == 0:
        d.append("\n")
for i in data:
    if i[0] == "noop":
        tick()
    elif i[0] == "addx":
        tick()
        tick()
        x += int(i[1])
print("".join(d))