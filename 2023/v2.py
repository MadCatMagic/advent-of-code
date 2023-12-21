from typing import List, TypeVar, Callable, Any
numeric = (int, float)

from functools import total_ordering
@total_ordering
class v2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __add__(self, o):
        if type(o) in numeric:
            return v2(self.x + o, self.y + o)
        elif type(o) == type(self):
            return v2(self.x + o.x, self.y + o.y)
        raise TypeError()
    
    def __sub__(self, o):
        if type(o) in numeric:
            return v2(self.x - o, self.y - o)
        elif type(o) == type(self):
            return v2(self.x - o.x, self.y - o.y)
        raise TypeError()
    
    def __neg__(self):
        return v2(-self.x, -self.y)
    
    def __iadd__(self, o):
        if type(o) in numeric:
            self.x += o
            self.y += o
            return self
        elif type(o) == type(self):
            self.x += o.x
            self.y += o.y
            return self
        raise TypeError()
    
    def __isub__(self, o):
        if type(o) in numeric:
            self.x -= o
            self.y -= o
            return self
        elif type(o) == type(self):
            self.x -= o.x
            self.y -= o.y
            return self
        raise TypeError()
    
    def __mul__(self, o):
        if type(o) in numeric:
            return v2(self.x * o, self.y * o)
        raise TypeError()
    
    def __imul__(self, o):
        if type(o) in numeric:
            self.x *= o
            self.y *= o
            return self
        raise TypeError()
    
    def __abs__(self):
        return (self.x * self.x + self.y * self.y) ** 0.5
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"v2({self.x}, {self.y})"
    
    def __eq__(self, o):
        if type(self) == type(o):
            return o.x == self.x and o.y == self.y
        return False
    
    def __hash__(self):
        return hash(self.x) ^ (hash(self.y) << 4)
    
    def __lt__(self, o):
        if type(self) == type(o):
            return abs(self) < abs(o)
        return False

T = TypeVar('T')
def pprintMatrix(matrix: List[List[T]], spaces: int = 0, converter: Callable[[T], str] = str, returnAsString: bool = False) -> None | str:
    s = [[converter(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = (" " * spaces).join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    res = '\n'.join(table)
    if returnAsString:
        return res
    print(res)

K = TypeVar('K')
def reverseLookup(d: dict[K: T], v: T) -> K:
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

def transposeMatrix(arr):
    if arr == []:
        return []
    elif arr == [[]]:
        return [[]]
    k = [[] for _ in range(len(arr[0]))]
    for l in arr:
        for j, c in enumerate(l):
            k[j].append(c)
    if type(arr[0]) == str:
        return ["".join(l) for l in k]
    return k

def rotateMatrixCW(arr):
    if arr == []:
        return []
    elif arr == [[]]:
        return [[]]
    k = [[arr[-j-1][i] for j in range(len(arr))] for i in range(len(arr[0]))]
    if type(arr[0]) == str:
        return ["".join(l) for l in k]
    return k

def rotateMatrixCCW(arr):
    if arr == []:
        return []
    elif arr == [[]]:
        return [[]]
    k = [[arr[j][-i-1] for j in range(len(arr))] for i in range(len(arr[0]))]
    if type(arr[0]) == str:
        return ["".join(l) for l in k]
    return k

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