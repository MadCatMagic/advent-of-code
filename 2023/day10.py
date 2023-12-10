from v2 import v2, pprintMatrix

pairs = {
    "|": (v2(0, 1), v2(0, -1)),
    "-": (v2(1, 0), v2(-1, 0)),
    "L": (v2(0, -1), v2(1, 0)),
    "J": (v2(0, -1), v2(-1, 0)),
    "7": (v2(0, 1), v2(-1, 0)),
    "F": (v2(0, 1), v2(1, 0))
}

class Program:
    def __init__(self):
        with open("2023/day10-input.txt", "r") as f:
            self.data = f.read().split("\n")
            self.size = v2(len(self.data[0]), len(self.data))

            # part 1
            start = self.findStart()
            ona = onb = start
            a, b = self.findNext(start, checkAll=True)
            da = a - start
            db = b - start
            # assuming that start is not on the edge (since it isn't for my input)
            self.data[start.y] = self.data[start.y][:start.x] + self.findInverse(da, db) + self.data[start.y][start.x + 1:]

            s1 = 1
            while a != b:
                s1 += 1

                t = ona
                ona = a
                a = self.findNext(ona, t)[0]

                t = onb
                onb = b
                b = self.findNext(onb, t)[0]

            # part 2
            self.counts = [[0 for x in range(self.size.x)] for y in range(self.size.y)]
            self.counts[start.y][start.x] = 1

            ona = onb = start
            a, b = self.findNext(start, checkAll=True)
            i = 1
            while a != b:
                i += 1
                self.counts[a.y][a.x] = i
                self.counts[b.y][b.x] = s1 * 2 - i + 2
                ona, a = a, self.findNext(a, ona)[0]
                onb, b = b, self.findNext(b, onb)[0]
            
            self.counts[a.y][a.x] = i + 1

            s2 = 0
            for y, l in enumerate(self.counts[:-1]):
                goingDown = False
                for x, v in enumerate(l):
                    if v > 0:
                        nv = self.counts[y + 1][x]
                        diff = v - nv
                        if v in (1, s1 * 2) and nv in (1, s1 * 2):
                            diff = 1
                        if nv > 0 and diff in (-1, 1):
                            goingDown = not goingDown
                    elif goingDown:
                        self.counts[y][x] += 100
                        s2 += 1
            
            #pprintMatrix(self.counts, 2)

            print(s1, s2)

    def findInverse(self, a, b):
        for key, pair in pairs.items():
            if a in pair and b in pair:
                return key

    def findStart(self):
        for y, l in enumerate(self.data):
            for x, c in enumerate(l):
                if c == "S":
                    return v2(x, y)
                
    def inBounds(self, p):
        return 0 <= p.x < self.size.x and 0 <= p.y < self.size.y
    
    def findNext(self, pos, ignore = None, checkAll = False):
        if ignore == None:
            ignore = v2(-10, -10)
        dirs = []
        if checkAll:
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    p = pos + v2(dx, dy)
                    if self.inBounds(p) and self.data[p.y][p.x] != ".":
                        offs = pairs[self.data[p.y][p.x]]
                        if pos == p + offs[0] or pos == p + offs[1]:
                            dirs.append(p)
        else:
            for k in pairs[self.data[pos.y][pos.x]]:
                p = pos + k
                if self.inBounds(p) and self.data[p.y][p.x] != ".":
                    offs = pairs[self.data[p.y][p.x]]
                    if pos == p + offs[0] or pos == p + offs[1]:
                        dirs.append(p)
        return [d for d in dirs if d != ignore]

Program()