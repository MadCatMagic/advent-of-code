from copy import deepcopy
from math import prod

with open("2023/day19-input.txt", "r") as f:
    data = f.read().split("\n\n")
    lines = {k[:k.index("{")]: k[k.index("{") + 1:-1].split(",") for k in data[0].split("\n")}

    class node:
        # cond of format "a<"
        def __init__(self):
            self.cond = ""
            self.condv = 0
            self.success = None
            self.failure = None

        def __call__(self, obj: dict[str, int]) -> str:
            if self.cond != "":
                if self.cond[1] == "<": return self.success(obj) if obj[self.cond[0]] < self.condv else self.failure(obj)
                if self.cond[1] == ">": return self.success(obj) if obj[self.cond[0]] > self.condv else self.failure(obj)
            return self.success(obj)
    
        @staticmethod
        def calcRangeValue(ranges: dict[str, tuple[int]]):
            return prod(b - a + 1 for a, b in ranges.values())
        
        def summarize(self, ranges: dict[str, tuple[int]] = None) -> int:
            # if this is just a success, do that
            if self.cond == "":
                if type(self.success) == type(self):
                    return self.success.summarize(ranges)
                else:
                    return self.calcRangeValue(ranges) * (1 if self.success(0) == "A" else 0)

            # test if ranges do not pass at all
            lt = self.cond[1] == "<" and ranges[self.cond[0]][0] >= self.condv and ranges[self.cond[0]][1] >= self.condv
            gt = self.cond[1] == ">" and ranges[self.cond[0]][0] <= self.condv and ranges[self.cond[0]][1] <= self.condv
            if lt or gt:
                if type(self.failure) == type(self):
                    return self.failure.summarize(deepcopy(ranges))
                return self.calcRangeValue(ranges) * (1 if self.failure(0) == "A" else 0)
            
            # at least some part of the range does pass so pass that which passes to success
            # and that which does not to failure
            ranges2 = deepcopy(ranges)
            existing = ranges[self.cond[0]]
            if self.cond[1] == "<":
                ranges[self.cond[0]] = (existing[0], min(existing[1], self.condv - 1))
                ranges2[self.cond[0]] = (ranges[self.cond[0]][1] + 1, existing[1])
            elif self.cond[1] == ">":
                ranges[self.cond[0]] = (max(existing[0], self.condv + 1), existing[1])
                ranges2[self.cond[0]] = (existing[0], ranges[self.cond[0]][0] - 1)

            s = 0
            if type(self.success) == type(self):
                s += self.success.summarize(ranges)
            else:
                s += self.calcRangeValue(ranges) * (1 if self.success(0) == "A" else 0)
            if type(self.failure) == type(self):
                s += self.failure.summarize(ranges2)
            else:
                s += self.calcRangeValue(ranges2) * (1 if self.failure(0) == "A" else 0)
            return s
        
        @classmethod
        def createTree(cls, data: dict[str, list[str]], name: str = "in", index: int = 0):
            l = data[name]
            obj = cls()
            if index == len(l) - 1:
                if l[index] == "A" or l[index] == "R":
                    obj.success = lambda x: l[index]
                else:
                    obj.success = cls.createTree(data, l[index])
            else:
                obj.cond = l[index][:2]
                spl = l[index][2:].split(":")
                obj.condv = int(spl[0])
                if spl[1] == "A" or spl[1] == "R":
                    obj.success = lambda x: spl[1]
                else:
                    obj.success = cls.createTree(data, spl[1])
                obj.failure = cls.createTree(data, name, index + 1)
            
            return obj

    # part 1
    root = node.createTree(lines)
    import re
    s1 = 0
    for line in data[1].split("\n"):
        k = {a: int(b) for a, b in zip(("x", "m", "a", "s"), re.findall("[0-9]+", line))}
        if root(k) == "A":
            s1 += sum(k.values())

    # part 2
    s2 = root.summarize({"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})
    
    print(s1, s2)
        
    