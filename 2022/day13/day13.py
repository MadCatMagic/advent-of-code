import json
def fopen():
    with open("day13/day13-input.txt", "r") as f:
        data = f.read().strip().split("\n\n")
        data = [[json.loads(l) for l in pair.split("\n")] for pair in data]
        return data

# part 1
sum = 0
data = fopen()
def correct(a, b):
    for i, j in zip(a, b):
        if type(i) == int and type(j) == int:
            if i != j:
                return i < j, True
            continue
        elif type(i) == int:
            i = [i]
        elif type(j) == int:
            j = [j]
        result, definite = correct(i, j)
        if definite:
            return result, True
    if len(a) > len(b):
        return False, True
    elif len(a) < len(b):
        return True, True
    return True, False
for i, pair in enumerate(data):
    if correct(pair[0], pair[1])[0]:
        sum += i + 1

print(sum)

# part 2
# insertion sort
data = [l[0] for l in data] + [l[1] for l in data]
data.append([[2]])
data.append([[6]])
for i in range(len(data) - 1):
    if not correct(data[i], data[i + 1])[0]:
        for j in range(i + 1):
            if correct(data[i - j], data[i - j + 1])[0]:
                break
            else:
                temp = data[i - j + 1]
                data[i - j + 1] = data[i - j]
                data[i - j] = temp
n = 1
for i, v in enumerate(data):
    if v == [[2]] or v == [[6]]:
        n *= i + 1
print(n)