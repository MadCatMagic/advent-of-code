def fopen():
    with open("day3/day3-input.txt", "r") as f:
        data = f.read().split("\n")
        return [(a[:len(a) // 2], a[len(a) // 2:]) for a in data]

def similar(a, b):
    s = []
    for i in a:
        for j in b:
            if i == j:
                if i not in s:
                    s.append(i)
    if len(s) > 1:
        return s
    return s[0]

# part 1
priority = {c: i + 1 for i, c in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")}
data = fopen()
print(sum([priority[similar(a, b)] for a, b in data]))

# part 2
data = [a + b for a, b in data]
ss = []
for i in range(len(data) // 3):
    s1 = similar(data[i * 3], data[i * 3 + 1])
    s2 = similar(s1, data[i * 3 + 2])
    ss.append(priority[s2])
print(sum(ss))