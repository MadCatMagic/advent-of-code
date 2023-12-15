def HASH(inp):
    i = 0
    for c in inp:
        i += ord(c)
        i *= 17
        i %= 256
    return i

with open("2023/day15-input.txt") as f:
    data = f.read().split(",")
 
    # part 1
    s1 = 0
    for v in data:
        s1 += HASH(v)
   
    # part 2
    arr = [[] for _ in range(256)]
    for v in data:
        if v.find("=") != -1:
            a, b = v.split("=")
            h = HASH(a)
            added = False
            for i, el in enumerate(arr[h]):
                if el[0] == a:
                    arr[h][i] = (a, int(b))
                    added = True
            if not added:
                arr[h].append((a, int(b)))
        else:
            code = v[:-1]
            h = HASH(code)
            for i, el in enumerate(arr[h]):
                if el[0] == code:
                    del arr[h][i]
 
    s2 = 0  
    for i, k in enumerate(arr):
        if k != []:
            s2 += (i + 1) * sum((j + 1) * f for j, (_, f) in enumerate(k))
   
    print(s1, s2)