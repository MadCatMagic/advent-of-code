from testy import TestCase
from vec import v2
from util import *

class UtilityTestsGeneral(TestCase):
    def test_polyAreaShoelace(self):
        points = [v2(0, 0), v2(5, 0), v2(8, 2), v2(4, 3), v2(0, 0)]
        self.assert_equal(polyAreaShoelace(points), 13)

    def test_reverseLookup(self):
        d = {2: "2", 4: "4", 5: "5"}
        self.assert_equal(reverseLookup(d, "2"), 2)
        self.assert_equal(reverseLookup(d, "5"), 5)
        self.assert_expect_error(lambda: reverseLookup(d, "6"), LookupError)


class UtilityTestsMatrices(TestCase):
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