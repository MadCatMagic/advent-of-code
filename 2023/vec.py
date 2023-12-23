numeric = (int, float)

from functools import total_ordering
# vector2 class
@total_ordering
class v2:
    __slots__ = "x", "y"
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
            return v2(self.x + o, self.y + o)
        elif type(o) == type(self):
            return v2(self.x + o.x, self.y + o.y)
        raise TypeError()
    
    def __isub__(self, o):
        if type(o) in numeric:
            return v2(self.x - o, self.y - o)
        elif type(o) == type(self):
            return v2(self.x - o.x, self.y - o.y)
        raise TypeError()
    
    def __mul__(self, o):
        if type(o) in numeric:
            return v2(self.x * o, self.y * o)
        raise TypeError()
    
    def __imul__(self, o):
        if type(o) in numeric:
            return v2(self.x * o, self.y * o)
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
        return hash(self.x ^ 1589432787438) ^ (hash(self.y) << 8)
    
    def __lt__(self, o):
        if type(self) == type(o):
            return abs(self) < abs(o)
        return False

# vector3 class
@total_ordering
class v3:
    __slots__ = "x", "y", "z"
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, o):
        if type(o) in numeric:
            return v3(self.x + o, self.y + o, self.z + o)
        elif type(o) == type(self):
            return v3(self.x + o.x, self.y + o.y, self.z + o.z)
        raise TypeError()
    
    def __sub__(self, o):
        if type(o) in numeric:
            return v3(self.x - o, self.y - o, self.z - o)
        elif type(o) == type(self):
            return v3(self.x - o.x, self.y - o.y, self.z - o.z)
        raise TypeError()
    
    def __neg__(self):
        return v3(-self.x, -self.y, -self.z)
    
    def __iadd__(self, o):
        if type(o) in numeric:
            self.x += o
            self.y += o
            self.z += o
            return self
        elif type(o) == type(self):
            self.x += o.x
            self.y += o.y
            self.z += o.z
            return self
        raise TypeError()
    
    def __isub__(self, o):
        if type(o) in numeric:
            self.x -= o
            self.y -= o
            self.z -= o
            return self
        elif type(o) == type(self):
            self.x -= o.x
            self.y -= o.y
            self.z -= o.z
            return self
        raise TypeError()
    
    def __mul__(self, o):
        if type(o) in numeric:
            return v3(self.x * o, self.y * o, self.z * o)
        raise TypeError()
    
    def __imul__(self, o):
        if type(o) in numeric:
            self.x *= o
            self.y *= o
            self.z *= o
            return self
        raise TypeError()
    
    def __abs__(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __repr__(self):
        return f"v3({self.x}, {self.y}, {self.z})"
    
    def __eq__(self, o):
        if type(self) == type(o):
            return o.x == self.x and o.y == self.y and o.z == self.z
        return False
    
    def __hash__(self):
        return (hash(self.x) ^ (hash(self.y) << 8) ^ 185423879) ^ (hash(self.z) << 16)
    
    def __lt__(self, o):
        if type(self) == type(o):
            return abs(self) < abs(o)
        return False