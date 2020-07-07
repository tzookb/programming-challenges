import unittest
import solution


class TestStringMethods(unittest.TestCase):

    def getResp(self, a, b):
        return solution.abbreviation(a, b)

    def test_upper(self):
        a = "beFgH"
        b = "EFG"
        res = self.getResp(a, b)
        self.assertEqual('NO', res, a+" - "+b)

    def test_upper(self):
        a = "daBcd"
        b = "ABC"
        res = self.getResp(a, b)
        self.assertEqual('YES', res, a+" - "+b)

if __name__ == '__main__':
    unittest.main()