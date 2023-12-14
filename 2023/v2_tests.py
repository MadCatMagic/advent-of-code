from v2 import *
class TestCase:
    def RunTests(self):
        pass

    def assert_equal(self, a, b, message = ""):
        if message == "":
            message = f"assertion failed: {a!r} != {b!r}"
        
    

def run():
    pass

class Vector2Tests(TestCase):
    def test_addition(self):
        a = v2(1, 2)
        b = v2(4, 7)
        c = v2(-6, -1)
        d = v2(0.3, -0.4)
        self.assert_equal(a + b, v2(5, 9))
        self.assert_equal(a + c, v2(-5, 1))
        self.assert_equal(a + d, v2(1.3, 1.6))

if __name__ == "__main__":
    run()