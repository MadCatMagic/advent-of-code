from v2 import *
from traceback import format_exc

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# by convention, assumes in the formatting that the first value is the one being tested for most assertions, and the second value is the true value
class TestCase:

    class outputElement:
        def __init__(self, success: bool, failureMessage: str = "", raisedError = False):
            self.success = success
            self.raisedError = raisedError
            self.message = failureMessage

        def __str__(self):
            if self.success:
                return bcolors.OKGREEN + "." + bcolors.ENDC
            elif self.raisedError:
                return bcolors.FAIL + "?" + bcolors.ENDC
            else:
                return bcolors.FAIL + "#" + bcolors.ENDC
            
    class indentElement:
        def __init__(self, header = None):
            self.header = header

        def __str__(self):
            if self.header != None:
                return f"{self.header}: "
            return ""
        
    class endIndentation: pass

    def __init__(self):
        self.assertions = []

    def assert_equal(self, a, b, message: str = "") -> bool:
        if message == "":
            message = f"assertion failed: '{a!r}' != {b!r}"
        return self._assert(lambda: a == b, message)
    
    def assert_nequal(self, a, b, message: str = "") -> bool:
        if message == "":
            message = f"assertion failed: '{a!r}' == {b!r}"
        return self._assert(lambda: a != b, message)
    
    # tests for an absolute or relative error of [tolerance]
    def assert_equal_approx(self, a, b, tolerance = 1e-8, message: str = "") -> bool:
        if message == "":
            message = f"assertion failed: '{a!r}' !~= {b!r}"
        return self._assert(lambda: abs(a - b) < tolerance or abs((a - b) / b) < tolerance, message)
        
    def assert_true(self, v, message: str = "") -> bool:
        if message == "":
            message = f"assertion failed: '{v!r}' is not True"
        return self._assert(lambda: v == True, message)
    
    # each individual call is counted as a 'test', but is within the test it is called from
    def _assert(self, function, message):
        try:
            assert function()
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
                self.assertions.append(self.indentElement(name[5:]))
                try:
                    if s != None:
                        s()
                    getattr(self, name)()
                except:
                    self.assertions.append(self.outputElement(False, f"Error while running test '{name[5:]}':\n{format_exc()[:-1]}", True))
                self.assertions.append(self.endIndentation())

    def __str__(self):
        s = ""
        indents = 1
        successes = 0
        failures = 0
        errors = 0
        start = -1
        for i, k in enumerate(self.assertions):
            if type(k) == self.indentElement:
                start = i
                indents += 1
                if str(k) != "":
                    s += '  ' * (indents - 1) + str(k)
            elif type(k) == self.endIndentation:
                s += "\n"
                for j in range(start + 1, i):
                    if not self.assertions[j].success:
                        s += f"{'  ' * indents}{self.assertions[j].message}\n"
                indents -= 1
            else:
                s += f"{k!s}"
                if k.success: successes += 1
                elif k.raisedError: errors += 1
                else: failures += 1
        s += f"\nSuccesses: {bcolors.OKGREEN}{successes}{bcolors.ENDC}\n"
        if failures > 0: s += f"Failures: {bcolors.FAIL}{failures}{bcolors.ENDC}\n"
        if errors > 0: s += f"Errors: {bcolors.WARNING}{errors}{bcolors.ENDC}\n"
        return s

    

def run_tests():
    for name, el in globals().items():
        if type(el) == type(TestCase) and el != TestCase and issubclass(el, TestCase):
            print(f"Running tests for '{name}':")
            obj = el()
            obj.RunTests()
            print(obj)

class TestTests(TestCase):
    def test_expect_to_pass(self):
        # should all pass
        self.assert_equal(1, 1)
        self.assert_equal("abc", "a" + "b" + "c")
        self.assert_equal([42, "er"], [42, "er"])
        
        self.assert_nequal(1, 5)
        self.assert_nequal(True, False)
        self.assert_nequal([], None)
        
        self.assert_true(True)
        self.assert_true(4 < 76)

        self.assert_equal_approx(100000, 100000.0003)
        self.assert_equal_approx(100000.0003, 100000)
        self.assert_equal_approx(0, 3e-10)

    def test_expect_to_fail(self):
        #self.expectFailure(11)
        # should all fail
        self.assert_equal(1, 2)
        self.assert_equal(False, 1)
        self.assert_equal([], ())

        self.assert_nequal(1, 1.0)
        self.assert_nequal((), ())
        self.assert_nequal("abc", "abc")

        self.assert_true(False)
        self.assert_true("awiodj")
        
        self.assert_equal_approx(1000, 1000.001)
        self.assert_equal_approx(5, 10)
        self.assert_equal_approx(200, -200)


if __name__ == "__main__":
    run_tests()