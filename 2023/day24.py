from vec import v3

with open("2023/day24-input.txt", "r") as f:
    v3ise = lambda x: v3(int(x[0]), int(x[1]), int(x[2]))
    data = [tuple(v3ise(k.split(",")) for k in l.split("@")) for l in f.read().split("\n")]
    
    # part 1
    minv = 200000000000000
    maxv = 400000000000000
    s1 = 0
    for i, (p1, d1) in enumerate(data):
        for j, (p2, d2) in enumerate(data):
            if j < i:
                continue
            if p1 == p2 and d1 == d2:
                continue
            # calculate whether they intersect
            m1 = d1.y / d1.x
            m2 = d2.y / d2.x
            # lines are parallel
            if m1 == m2:
                continue
            x = (p1.x * m1 - p2.x * m2 + p2.y - p1.y) / (m1 - m2)
            t1, t2 = (x - p1.x) / d1.x, (x - p2.x) / d2.x
            y = t1 * d1.y + p1.y # = t2 / d2.y
            if t1 > 0 and t2 > 0 and minv <= x <= maxv and minv <= y <= maxv:
                s1 += 1
    
    print(s1)