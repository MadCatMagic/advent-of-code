from vec import *
from testy import TestCase, run_tests

class V2Tests(TestCase):
    def setup(self):
        self.a = v2(1, 4)
        self.b = v2(-3, 2)
        self.c = v2(0.2, 0.3)

    def test_basics(self):
        self.assert_equal(self.a + self.b, v2(-2, 6))
        self.assert_equal(self.a + self.c, v2(1.2, 4.3))
        self.assert_equal(self.a - self.b, v2(4, 2))
        self.assert_equal(self.b - self.c, v2(-3.2, 1.7))
        self.assert_equal(self.a + 2, v2(3, 6))
        self.assert_equal(self.a - 2, v2(-1, 2))
        self.assert_equal(-self.a, v2(-1, -4))
        self.assert_equal(self.a * 2, v2(2, 8))

        self.assert_expect_error(lambda: self.a * self.b, TypeError)
        self.assert_expect_error(lambda: 1 * self.b, TypeError)

    def test_assignments(self):
        a = self.a
        a += self.b
        self.assert_equal(a, v2(-2, 6))
        a += 2.4
        # float problems :(
        self.assert_equal_approx(a, v2(0.4, 8.4))
        b = self.b
        b -= self.a
        self.assert_equal(b, v2(-3.4, -6.4))
        b -= -2
        self.assert_equal(b, v2(-1.4, -4.4))
        c = self.c
        c *= 4
        self.assert_equal(c, v2(0.8, 1.2))
        def mulErr():
            v = v2(4, 3)
            v *= v2(1, 2)
        self.assert_expect_error(mulErr, TypeError)

    def test_specials(self):
        self.assert_equal(str(self.a), "(1, 4)")
        self.assert_equal(repr(self.a), "v2(1, 4)")

        self.assert_equal(abs(v2(0, 0)), 0)
        self.assert_equal(abs(v2(3, 4)), 5)

class V3Tests(TestCase):
    def setup(self):
        self.a = v3(1, 4, 2)
        self.b = v3(-3, 2, 4)
        self.c = v3(0.2, 0.3, -0.2)

    def test_basics(self):
        self.assert_equal(self.a + self.b, v3(-2, 6, 6))
        self.assert_equal(self.a + self.c, v3(1.2, 4.3, 1.8))
        self.assert_equal(self.a - self.b, v3(4, 2, -2))
        self.assert_equal(self.b - self.c, v3(-3.2, 1.7, 4.2))
        self.assert_equal(self.a + 2, v3(3, 6, 4))
        self.assert_equal(self.a - 2, v3(-1, 2, 0))
        self.assert_equal(-self.a, v3(-1, -4, -2))
        self.assert_equal(self.a * 2, v3(2, 8, 4))

        self.assert_expect_error(lambda: self.a * self.b, TypeError)
        self.assert_expect_error(lambda: 1 * self.b, TypeError)

    def test_assignments(self):
        a = self.a
        a += self.b
        self.assert_equal(a, v3(-2, 6, 6))
        a += 2.4
        # float problems :(
        self.assert_equal_approx(a, v3(0.4, 8.4, 8.4))
        b = self.b
        b -= self.a
        self.assert_equal(b, v3(-3.4, -6.4, -4.4))
        b -= -2
        self.assert_equal_approx(b, v3(-1.4, -4.4, -2.4))
        c = self.c
        c *= 4
        self.assert_equal(c, v3(0.8, 1.2, -0.8))
        def mulErr():
            v = v3(4, 3, 2)
            v *= v3(1, 2, 1)
        self.assert_expect_error(mulErr, TypeError)

    def test_specials(self):
        self.assert_equal(str(self.a), "(1, 4, 2)")
        self.assert_equal(repr(self.a), "v3(1, 4, 2)")

        self.assert_equal(abs(v3(0, 0, 0)), 0)
        self.assert_equal(abs(v3(2, 3, 6)), 7)

if __name__ == "__main__":
    run_tests()