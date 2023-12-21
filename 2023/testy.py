from traceback import format_exc
from typing import Callable

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

    class _outputElement:
        def __init__(self, shouldHaveFailed: bool, success: bool, failureMessage: str = "", raisedError = False):
            self.shouldHaveFailed = shouldHaveFailed
            self.success = success
            self.raisedError = raisedError
            self.message = failureMessage

        def __str__(self):
            if self.success:
                return (bcolors.FAIL if self.shouldHaveFailed else bcolors.OKGREEN) + "." + bcolors.ENDC
            elif self.raisedError:
                return bcolors.FAIL + "?" + bcolors.ENDC
            else:
                return (bcolors.OKGREEN if self.shouldHaveFailed else bcolors.FAIL) + "#" + bcolors.ENDC
            
    class _indentElement:
        def __init__(self, header = None):
            self.header = header

        def __str__(self):
            if self.header != None:
                return f"{self.header}: "
            return ""
        
    class _endIndentation: pass

    def __init__(self):
        self._assertions = []
        self._expectingFailures = 0

    def expectFailure(self, num: int = 1):
        self._expectingFailures += num

    def assert_equal(self, a, b, message: str = "") -> bool:
        if message == "":
            message = f"assertion failed: {a!r} != {b!r}"
        return self._assert(lambda: a == b, message)
    
    def assert_nequal(self, a, b, message: str = "") -> bool:
        if message == "":
            message = f"assertion failed: {a!r} == {b!r}"
        return self._assert(lambda: a != b, message)
    
    # tests for an absolute or relative error of [tolerance]
    def assert_equal_approx(self, a, b, tolerance = 1e-8, message: str = "") -> bool:
        if message == "":
            message = f"assertion failed: {a!r} !~= {b!r}"
        return self._assert(lambda: abs(a - b) < tolerance or abs((a - b) / b) < tolerance, message)
        
    def assert_true(self, v, message: str = "") -> bool:
        if message == "":
            message = f"assertion failed: {v!r} is not True"
        return self._assert(lambda: v == True, message)
    
    # disgusting functional programming here
    def assert_expect_error(self, func: Callable, exception: type = Exception, message: str = "") -> bool:
        class mesType:
            def __init__(self, m):
                self.m = m
            def __str__(self):
                return self.m
        def funct(m: mesType) -> bool:
            try:
                func()
            except exception as e:
                return True
            except Exception as e:
                if m.m == "":
                    m.m = f"assertion failed: {func!r} did not raise the error {exception.__name__}, raised {type(e).__name__} instead:\n{bcolors.WARNING}{e}{bcolors.ENDC}"
                return type(e).__name__ == exception.__name__ or issubclass(type(e), exception)
            return False
        mt = mesType(message)
        return self._assert(lambda: funct(mt), mt)
    
    # each individual call is counted as a 'test', but is within the test it is called from
    def _assert(self, function, message):
        expectFail = self._expectingFailures > 0
        if expectFail:
            self._expectingFailures -= 1
        try:
            assert function()
            self._assertions.append(self._outputElement(expectFail, True))
            return True
        except AssertionError:
            self._assertions.append(self._outputElement(expectFail, False, str(message)))
            return False

    def _runTests(self):
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
                self._assertions.append(self._indentElement(name[5:]))
                try:
                    if s != None:
                        s()
                    getattr(self, name)()
                except:
                    self._assertions.append(self._outputElement(False, False, f"Error while running test '{name[5:]}':\n{format_exc()[:-1]}", True))
                self._assertions.append(self._endIndentation())

    def __str__(self):
        s = ""
        indents = 1
        successes = 0
        failures = 0
        deliberateFailures = 0
        errors = 0
        start = -1
        for i, k in enumerate(self._assertions):
            if type(k) == self._indentElement:
                start = i
                indents += 1
                if str(k) != "":
                    s += '  ' * (indents - 1) + str(k)
            elif type(k) == self._endIndentation:
                s += "\n"
                for j in range(start + 1, i):
                    if not self._assertions[j].success:
                        if self._showDeliberateFailureAssertions and self._assertions[j].shouldHaveFailed or not self._assertions[j].shouldHaveFailed:
                            s += f"{'  ' * indents}{self._assertions[j].message}\n"
                indents -= 1
            else:
                s += f"{k!s}"
                if k.success and not k.shouldHaveFailed: successes += 1
                elif k.raisedError: errors += 1
                elif not k.success and k.shouldHaveFailed: deliberateFailures += 1
                else: failures += 1
        s += f"\nSuccessful tests: {bcolors.OKGREEN}{successes + deliberateFailures}{bcolors.ENDC}\n"
        if failures > 0: s += f"Failures: {bcolors.FAIL}{failures}{bcolors.ENDC}"
        if deliberateFailures > 0: s += f" (deliberate failures: {bcolors.OKGREEN}{deliberateFailures}{bcolors.ENDC})"
        if failures > 0 or deliberateFailures > 0: s += "\n"
        if errors > 0: s += f"Errors: {bcolors.WARNING}{errors}{bcolors.ENDC}\n"
        return s

def run_tests(showDeliberateFailureAssertions: bool = False):
    for el in TestCase.__subclasses__():
        print(f"Running tests for '{el.__name__}':")
        obj = el()
        obj._runTests()
        obj._showDeliberateFailureAssertions = showDeliberateFailureAssertions
        print(obj)

if __name__ == "__main__":
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

            self.assert_expect_error(lambda: 1 / 0, ZeroDivisionError)
            self.assert_expect_error(len)
            self.assert_expect_error(lambda: [1, 2][3], IndexError)

        def test_expect_to_fail(self):
            self.expectFailure(13)
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

            self.assert_expect_error(lambda: 1 + 1)
            self.assert_expect_error(lambda: 1 / 0, IndexError)

    run_tests()