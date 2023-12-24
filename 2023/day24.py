from vec import v3

# calculate whether they intersect
def testIntersectXY(p1: v3, d1: v3, p2: v3, d2: v3) -> bool:
    m1 = d1.y / d1.x
    m2 = d2.y / d2.x
    # lines are parallel
    if m1 == m2:
        return False
    # considers both y=mx+c representations of lines and parametric representations
    x = (p1.x * m1 - p2.x * m2 + p2.y - p1.y) / (m1 - m2)
    t1, t2 = (x - p1.x) / d1.x, (x - p2.x) / d2.x
    y = t1 * d1.y + p1.y # = t2 / d2.y
    if t1 > 0 and t2 > 0 and minv <= x <= maxv and minv <= y <= maxv:
        return True
    return False


with open("2023/day24-input.txt", "r") as f:
    v3ise = lambda x: v3(int(x[0]), int(x[1]), int(x[2]))
    data = [tuple(v3ise(k.split(",")) for k in l.split("@")) for l in f.read().split("\n")]
    
    # part 1
    minv = 200000000000000
    maxv = 400000000000000
    s1 = 0
    for i, (p1, d1) in enumerate(data):
        for j, (p2, d2) in enumerate(data):
            # don't overcount or test a hailstone against itself
            if j < i:
                continue
            if p1 == p2 and d1 == d2:
                continue
            if testIntersectXY(p1, d1, p2, d2):
                s1 += 1

    # part 2
    # to determine the correct position and velocity you only need to examine some of the hailstones
    # since we know a solution exists and there is only one solution that works for 3 hailstones
    from sympy import symbols, Eq, solve
    equations = []
    rpx, rpy, rpz = symbols("rpx,rpy,rpz")
    rvx, rvy, rvz = symbols("rvx,rvy,rvz")
    ts = symbols("t1,t2,t3")
    for i, (p, v) in enumerate(data[:3]):
        equations.append(Eq(rpx + rvx * ts[i], p.x + v.x * ts[i]))
        equations.append(Eq(rpy + rvy * ts[i], p.y + v.y * ts[i]))
        equations.append(Eq(rpz + rvz * ts[i], p.z + v.z * ts[i]))
    solved = solve(equations)[0]
    s2 = solved[rpx] + solved[rpy] + solved[rpz]
    print(s1, s2)