from typing import List, Any

def pprintMatrix(matrix: List[List[Any]], spaces: int) -> None:
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = (" " * spaces).join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    
class v2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __add__(self, o):
        if type(o) == int:
            return v2(self.x + o, self.y + o)
        elif type(o) == type(self):
            return v2(self.x + o.x, self.y + o.y)
        raise TypeError()
    
    def __sub__(self, o):
        if type(o) == int:
            return v2(self.x - o, self.y - o)
        elif type(o) == type(self):
            return v2(self.x - o.x, self.y - o.y)
        raise TypeError()
    
    def __neg__(self):
        return v2(-self.x, -self.y)
    
    def __iadd__(self, o):
        if type(o) == int:
            self.x += o
            self.y += o
            return self
        elif type(o) == type(self):
            self.x += o.x
            self.y += o.y
            return self
        raise TypeError()
    
    def __isub__(self, o):
        if type(o) == int:
            self.x -= o
            self.y -= o
            return self
        elif type(o) == type(self):
            self.x -= o.x
            self.y -= o.y
            return self
        raise TypeError()
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"v2({self.x}, {self.y})"
    
    def __eq__(self, o):
        if type(self) == type(o):
            return o.x == self.x and o.y == self.y
        return False