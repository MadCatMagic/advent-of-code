from v2 import *
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

class UtilityTests(TestCase):
    def setup(self):
        # abcd
        # efgh
        # ijkl
        self.m1 = ["abcd", "efgh", "ijkl"]
        self.m2 = [[1, 2], [3, 4], [5, 6]]

    def test_pprintMatrix(self):
        self.assert_equal(pprintMatrix(self.m1, returnAsString=True), "abcd\nefgh\nijkl")
        self.assert_equal(pprintMatrix(self.m2, returnAsString=True), "12\n34\n56")
        self.assert_equal(pprintMatrix(self.m2, 2, returnAsString=True), "1  2\n3  4\n5  6")
        self.m2[0][0] = 23
        self.assert_equal(pprintMatrix(self.m2, returnAsString=True), "232\n3 4\n5 6")
        self.assert_equal(pprintMatrix(self.m2, 1, lambda x: str(x % 10), True), "3 2\n3 4\n5 6")

        self.assert_equal(pprintMatrix([], returnAsString=True), "")
        self.assert_equal(pprintMatrix([[]], returnAsString=True), "")

    def test_transposeMatrix(self):
        self.assert_equal(transposeMatrix(self.m1), ["aei", "bfj", "cgk", "dhl"])
        self.assert_equal(transposeMatrix(transposeMatrix(self.m1)), self.m1)
        self.assert_equal(transposeMatrix(self.m2), [[1, 3, 5], [2, 4, 6]])
        self.assert_equal(transposeMatrix([]), [])
        self.assert_equal(transposeMatrix([[]]), [[]])

    def test_rotateMatrix(self):
        self.assert_equal(rotateMatrixCCW(self.m1), ["dhl", "cgk", "bfj", "aei"])
        self.assert_equal(rotateMatrixCW(self.m1), ["iea", "jfb", "kgc", "lhd"])
        self.assert_equal(rotateMatrixCCW(self.m2), [[2, 4, 6], [1, 3, 5]])
        self.assert_equal(rotateMatrixCW(self.m2), [[5, 3, 1], [6, 4, 2]])

        self.assert_equal(rotateMatrixCCW(rotateMatrixCW(self.m2)), self.m2)
        self.assert_equal(rotateMatrixCW(rotateMatrixCCW(self.m1)), self.m1)

        self.assert_equal(rotateMatrixCCW([]), [])
        self.assert_equal(rotateMatrixCW([]), [])
        self.assert_equal(rotateMatrixCCW([[]]), [[]])
        self.assert_equal(rotateMatrixCW([[]]), [[]])

    def test_polyAreaShoelace(self):
        points = [v2(0, 0), v2(5, 0), v2(8, 2), v2(4, 3), v2(0, 0)]
        self.assert_equal(polyAreaShoelace(points), 13)

if __name__ == "__main__":
    run_tests()