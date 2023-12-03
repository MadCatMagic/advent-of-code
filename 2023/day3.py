
with open("2023/day3input.txt") as f:
    data = [k + "." for k in f.read().split("\n")]

    # part 1
    s1 = 0
    for y, line in enumerate(data):
        num = ""
        add = False
        for x, char in enumerate(line):
            if char.isdecimal():
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if 0 <= dy + y < len(data) and 0 <= dx + x < len(line):
                            if data[dy + y][dx + x] in "*&$/-+=%@#":
                                add = True
                num += char
            elif len(num) > 0:
                if add:
                    s1 += int(num)
                add = False
                num = ""

    # part 2
    for y, line in enumerate(data):
        data[y] = list(data[y])
        for x, char in enumerate(line):
            if char == "*":
                data[y][x] = []
    
    for y, line in enumerate(data):
        num = ""
        gears = set()
        for x, char in enumerate(line):
            if type(char) == str and char.isdecimal():
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if 0 <= dy + y < len(data) and 0 <= dx + x < len(line):
                            if type(data[dy + y][dx + x]) == list:
                                gears.add((dx + x, dy + y))
                num += char
            elif len(num) > 0:
                for g in gears:
                    data[g[1]][g[0]].append(int(num))
                gears = set()
                num = ""
    
    s2 = 0
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if type(char) == list and len(char) == 2:
                s2 += char[0] * char[1]

    print(s1, s2)