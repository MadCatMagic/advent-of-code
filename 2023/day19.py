
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

        def __call__(self, obj: dict[str, int]):
            if self.cond != "":
                if self.cond[1] == "<": return self.success(obj) if obj[self.cond[0]] < self.condv else self.failure(obj)
                if self.cond[1] == ">": return self.success(obj) if obj[self.cond[0]] > self.condv else self.failure(obj)
            return self.success(obj)
        
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
    
    print(s1)
        
    