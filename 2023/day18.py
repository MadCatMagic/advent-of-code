from vec import v2
from util import polyAreaShoelace

def prepData(points, dirs):
    dic = {
        (v2(1, 0), v2(0, 1)): v2(1, 0),
        (v2(0, 1), v2(-1, 0)): v2(1, 1),
        (v2(-1, 0), v2(0, -1)): v2(0, 1),
        (v2(-1, 0), v2(0, 1)): v2(1, 1),
        (v2(0, -1), v2(-1, 0)): v2(0, 1),
        (v2(0, 1), v2(1, 0)): v2(1, 0)
    }
    for i in range(len(points) - 1):
        pair = (dirs[i - 1], dirs[i])
        if pair in dic:
            points[i] += dic[pair]

with open("2023/day18-input.txt", "r") as f:
    dirs = {"R": v2(1, 0), "L": v2(-1, 0), "U": v2(0, -1), "D": v2(0, 1)}
    data = [k.split() for k in f.read().split("\n")]
    data = [(dirs[d], int(n), c[1:-1]) for d, n, c in data]

    # part 1
    points = [v2()]
    ds = []
    for i, (d, n, _) in enumerate(data):
        points.append(points[-1] + d * n)
        ds.append(d)
    prepData(points, ds)
    s1 = polyAreaShoelace(points)

    # part 2
    data = [(int(c[1:-1], 16), dirs[{"0": "R", "1": "D", "2": "L", "3": "U"}[c[-1]]]) for _, _, c in data]
    points = [v2(0, 0)]
    ds = []
    for n, d in data:
        points.append(points[-1] + d * n)
        ds.append(d)
    prepData(points, ds)
    points[-1] = points[0]
    
    s2 = polyAreaShoelace(points)

    print(s1, s2)