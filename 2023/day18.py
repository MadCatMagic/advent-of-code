from v2 import v2, pprintMatrix

# points[0] should equal points[-1]
def polyAreaShoelace(points: list[v2]):
    assert points[0] == points[-1], "points[0] should equal points[-1]"
    v = sum(
        (points[i].y + points[i + 1].y) * (points[i].x - points[i + 1].x) 
        for i in range(len(points) - 1)
    ) * 0.5
    if int(v) == v:
        return int(v)
    return v

def prepData(points, dirs):
    dic = {
        (v2(1, 0), v2(0, 1)): v2(1, 0),
        (v2(0, 1), v2(-1, 0)): v2(1, 1),
        (v2(-1, 0), v2(0, -1)): v2(0, 1),
        (v2(-1, 0), v2(0, 1)): v2(1, 1),
        (v2(0, -1), v2(-1, 0)): v2(0, 1),
        (v2(0, 1), v2(1, 0)): v2(1, 0)
    }
    for i in range(0, len(dirs)):
        pair = tuple(dirs[i - 1:i + 1])
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
    ds.append(data[0][0])
    prepData(points, ds)
    s1 = polyAreaShoelace(points)

    """
    # find bounds
    pos = v2()
    minimum, maximum = v2(), v2()
    for d, n, _ in data:
        pos += d * n
        minimum = v2(min(minimum.x, pos.x), min(minimum.y, pos.y))
        maximum = v2(max(maximum.x, pos.x), max(maximum.y, pos.y))
    size = maximum - minimum + 1
    pos = -minimum
    # fill out edges
    arr = [["." for x in range(size.x)] for y in range(size.y)]
    nums = [[-1 for _ in range(size.x)] for _ in range(size.y)]
    arr[pos.y][pos.x] = "#"
    nums[pos.y][pos.x] = 1
    j = 2
    for d, n, _ in data:
        for i in range(n):
            pos += d
            arr[pos.y][pos.x] = "#"
            nums[pos.y][pos.x] = j
            j += 1
    # fill in centre
    for y, r in enumerate(arr):
        if y == 0:
            continue
        inside = False
        for x, c in enumerate(r):
            if nums[y][x] != -1 and abs(nums[y][x] - nums[y - 1][x]) == 1:
                inside = not inside
            if inside:
                arr[y][x] = "#"
    # count hashtags
    s1 = sum(r.count("#") for r in arr)
    """

    # part 2
    # dear god
    data = [(int(c[1:-1], 16), dirs[{"0": "R", "1": "D", "2": "L", "3": "U"}[c[-1]]]) for _, _, c in data]
    points = [v2(0, 0)]
    ds = [data[-1][1]]
    for n, d in data:
        points.append(points[-1] + d * n)
        ds.append(d)
    
    prepData(points, ds)
    
    s2 = polyAreaShoelace(points)

    print(s1, s2)