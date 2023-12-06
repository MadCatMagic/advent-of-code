def dostuff(seeds):
    s1 = 10 ** 12
    for seed in seeds:
        for map in maps:
            for range in map:
                if range[1] <= seed < range[1] + range[2]:
                    seed = range[0] + seed - range[1]
                    break
        s1 = min(seed, s1)
    return s1

def domorestuff(a, b, reverse):
    if reverse:
        newera = []
        for ra in a:
            rs, re = ra[1], ra[1] + ra[2]
            for rb in b:
                if rs <= rb[0] <= re or rs <= rb[0] + rb[2] <= re or rb[0] < rs and rb[0] + rb[2] > re:
                    ck = min(re, rb[0] + rb[2]) - max(rs, rb[0])
                    if ck == 0:
                        continue
                    newera.append([
                        max(rs, rb[0]) - rs + ra[0],
                        max(rs, rb[0]),
                        ck
                    ])
        return newera
    else:
        newera = []
        for ra in a:
            rs, re = ra[0], ra[0] + ra[2]
            for rb in b:
                if rs <= rb[1] <= re or rs <= rb[1] + rb[2] <= re or rb[1] < rs and rb[1] + rb[2] > re:
                    ck = min(re, rb[1] + rb[2]) - max(rs, rb[1])
                    if ck == 0:
                        continue
                    newera.append([
                        max(rs, rb[1]),
                        ra[1] + max(rs, rb[1]) - rs,
                        ck
                    ])
        return newera
    
def correctmap(m):
    s = 0
    toadd = []
    for r in m:
        if r[1] - s > 0:
            toadd.append([s, s, r[1] - s])
        s = r[1] + r[2]
    toadd.append([s, s, 2 ** 32])
    return m + toadd

with open("2023/day5input.txt", "r") as f:
    data = f.read().split("\n\n")
    seeds = [int(i) for i in data[0].split(" ")[1:]]
    maps = [[[int(v) for v in l.split(" ")] for l in k.split("\n")[1:]] for k in data[1:]]
    
    # part 1
    s1 = dostuff(seeds)

    # part 2
    # destination range, source range, length
    seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    #maps = [
    #    [[0, 3, 3], [3, 0, 3]], 
    #    [[0, 2, 4], [4, 0, 2]], 
    #    [[0, 1, 5], [5, 0, 1]]
    #]
    #maps = [
    #    [[0, 2, 3], [5, 0, 2], [3, 3, 2]], # ../.../.. -> ... /../..
    #    [[4, 0, 4], [0, 4, 3]],            #              ..../.. .  -> . ../.. ..
    #    [[6, 0, 1], [4, 5, 2], [0, 1, 4]]  #                            ./.. ../.. -> ..../../.
    #]
    # ././.../.. -> .../././..                correct
    #               .../././.. -> ./../..../. correct
    #maps = maps[:3]
    maps = [sorted(m, key=lambda x:x[1]) for m in maps]
    maps = [correctmap(m) for m in maps]
    print(maps)
    print([len(maps[i]) for i in range(len(maps))])
    for _ in range(len(maps) - 1):
        newmaps = []
        for i, a in enumerate(maps):
            if i == 0:
                newmaps.append(domorestuff(a, maps[i + 1], False))
            elif i == len(maps) - 1:
                newmaps.append(domorestuff(a, maps[i - 1], True))
            else:
                newera = domorestuff(a, maps[i + 1], False)
                newera2 = domorestuff(newera, maps[i - 1], True)
                newmaps.append(newera2)
        print([len(newmaps[i]) for i in range(len(newmaps))])
        maps = newmaps
    print(maps)
    s2 = 2 ** 31
    for i, best in enumerate(maps[-1]):
        curr = best
        for map in reversed(maps[:-1]):
            for range in map:
                if range[0] == curr[1]:
                    curr = range
                    break
        
        for seed in seeds:
            s = seed[0]
            e = seed[0] + seed[1]
            if s <= curr[1] < e or s <= curr[1] + curr[2] < e or curr[1] < s and curr[1] + curr[2] >= e:
                s2 = min(s2, best[0] + max(s, curr[1]) - curr[1])

    print(s1, s2)
    