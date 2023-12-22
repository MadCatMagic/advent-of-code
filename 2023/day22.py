from vec import v3

def settleBricks(bricks: list[list[v3]], skip: int, settled: set[v3], count = False):
    falls = 0
    for i, brick in enumerate(bricks):
        if i == skip:
            continue
        z = min(b.z for b in brick)
        startZ = z
        while z > 1 and all(b - v3(0, 0, 1) not in settled for b in brick):
            for b in brick:
                b.z -= 1
            z -= 1
        if count and z != startZ:
            falls += 1
        for b in brick:
            settled.add(b)
    return settled, falls

from copy import deepcopy
def canBeDestroyed(bricks: list[list[v3]], brick: int, settled: set[v3]):
    s = {b for b in settled if b not in bricks[brick]}
    newSettled, f = settleBricks(deepcopy(bricks), brick, set(), True)
    return int(s == newSettled), f

with open("2023/day22-input.txt", "r") as f:
    v3ise = lambda x: v3(int(x[0]), int(x[1]), int(x[2]))
    data = [tuple(v3ise(k.split(",")) for k in l.split("~")) for l in f.read().split("\n")]
    
    settled = {}
    data = [(min(b[0].z, b[1].z), b) for b in data]
    data = sorted(data, key=lambda x:x[0])
    bricks = []
    for z, (a, b) in data:
        points = []
        if a.x != b.x:
            for i in range(a.x, b.x + 1): points.append(v3(i, a.y, a.z))
        elif a.y != b.y:
            for i in range(a.y, b.y + 1): points.append(v3(a.x, i, a.z))
        elif a.z != b.z:
            for i in range(a.z, b.z + 1): points.append(v3(a.x, a.y, i))
        if len(points) == 0:
            points.append(a)
        bricks.append(points)

    # settle bricks
    settled, _ = settleBricks(bricks, -1, set())

    s1 = 0
    s2 = 0
    for i in range(len(bricks)):
        r, fs = canBeDestroyed(bricks, i, settled)
        s2 += fs
        s1 += r

    print(s1, s2)