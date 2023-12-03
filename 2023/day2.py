
with open("2023/day2input.txt", "r") as f:
    data = f.read().split("\n")
    s1 = 0
    s2 = 0
    for l in data:
        spl = l[5:].split(":")
        i = int(spl[0])
        games = [[r.strip().split(" ") for r in g.split(",")] for g in spl[1].split(";")]

        # part 1
        m = {"red": 12, "green": 13, "blue": 14}
        corr = True
        for g in games:
            for r in g:
                if int(r[0]) > m[r[1]]:
                    corr = False
                    break
            if not corr:
                break
        if corr:
            s1 += i

        # part 2
        m = {"red": 0, "green": 0, "blue": 0}
        for g in games:
            for r in g:
                m[r[1]] = max(m[r[1]], int(r[0]))
        s2 += m["red"] * m["green"] * m["blue"]
    print(s1, s2)