
class file:
    def __init__(self, name, size):
        self.size = size
        self.name = name

class node:
    def __init__(self, name, parent):
        self.size = None
        self.name = name
        self.parent = parent
        self.children = []

    def find(self, name):
        for child in self.children:
            if child.name == name:
                return child

    def __repr__(self):
        return f"[{self.name}: [{''.join([child.name for child in self.children])}]]"

def fopen():
    with open("day7-input.txt", "r") as f:
        data = f.read().strip()
        instructions = data.split("\n")
        root = node("/", None)
        current = root
        reading = False
        for i in instructions:
            if i[0] == "$":
                reading = False
            if not reading:
                if i == "$ cd /":
                    current = root
                elif i == "$ ls":
                    reading = True
                elif i == "$ cd ..":
                    current = current.parent
                elif i[:4] == "$ cd":
                    # you will always read the dir before trying to enter it
                    current = current.find(i[5:])
            else:
                parts = i.split(" ")
                if parts[0] == "dir":
                    n = node(parts[1], current)
                    current.children.append(n)
                else:
                    f = file(parts[1], int(parts[0]))
                    current.children.append(f)

        return root

print(repr(fopen()))
            
