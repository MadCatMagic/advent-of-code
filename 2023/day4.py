
def interpAsNums(string):
    return [int(string[i + 1] + string[i + 2]) for i in range(0, len(string) - 1, 3)]

with open("2023/day4-input.txt", "r") as f:
    data = [line.split(":") for line in f.read().split("\n")]
    id = [int(k[0][5:]) for k in data]
    pair = [[interpAsNums(k) for k in l[1].split("|")] for l in data]
    
    # part 1
    s1 = 0
    encapsulated = []
    for line in pair:
        k = -1
        for el in line[1]:
            try:
                line[0].index(el)
                k += 1
            except ValueError:
                pass
        s1 += (2 ** k) if k >= 0 else 0
        encapsulated.append((1, k + 1))

    # part 2
    for i, (num, won) in enumerate(encapsulated):
        for j in range(won):
            encapsulated[i + j + 1] = (
                encapsulated[i + j + 1][0] + num,
                encapsulated[i + j + 1][1]
            )
    s2 = sum(v[0] for v in encapsulated)

    print(s1, s2)