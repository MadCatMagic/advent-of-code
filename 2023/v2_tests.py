from v2 import *
from traceback import format_exc
class TestCase:

    class outputElement:
        def __init__(self, success: bool, failureMessage: str = ""):
            self.success = success
            self.message = failureMessage

        def __str__(self):
            if self.success:
                return "success"
            else:
                return self.message

    def __init__(self):
        self.assertions = []

    # each individual call is counted as a 'test', but is within the test it is called from
    # returns whether the test succeeds, but does not raise an error itself
    def assert_equal(self, a, b, message: str = "") -> bool:
        if message == "":
            message = f"assertion failed: {a!r} != {b!r}"
        try:
            assert a == b
            self.assertions.append(self.outputElement(True))
            return True
        except AssertionError:
            self.assertions.append(self.outputElement(False, message))
            return False

    def RunTests(self):
        a = dir(self)

        s = None
        if (a + ["setup"]).index("setup") != len(a):
            try:
                s = getattr(self, "setup")
            except AttributeError:
                pass
            if not callable(s):
                s = None

        for name in a:
            if len(name) < 6 or name[:5] != "test_":
                continue

            if callable(getattr(self, name)):
                try:
                    if s != None:
                        s()

                    getattr(self, name)()
                except:
                    self.assertions.append(f"Error while running test '{name[5:]}':")
                    self.assertions.append(format_exc())

    def print(self):
        for k in self.assertions:
            print(str(k))

    

def run_tests():
    for name, el in globals().items():
        if type(el) == type(TestCase) and el != TestCase and issubclass(el, TestCase):
            print(f"Running tests for '{name}':")
            obj = el()
            obj.RunTests()
            obj.print()

class Vector2Tests(TestCase):
    def setup(self):
        self.a = v2(1, 2)
        self.b = v2(4, 7)
        self.c = v2(-6, -1)
        self.d = v2(0.3, -0.4)

    def test_addition(self):
        self.assert_equal(self.a + self.b, v2(5, 9))
        self.assert_equal(self.a + self.c, v2(-5, 1))
        self.assert_equal(self.a + self.d, v2(1.3, 1.6))

    def test_subtraction(self):
        self.assert_equal(self.a - self.b, v2(-3, -5))
        self.assert_equal(self.a - self.c, v2(7, 3))
        self.assert_equal(self.a - self.d, v2(0.7, 2.4))

if __name__ == "__main__":
    run_tests()