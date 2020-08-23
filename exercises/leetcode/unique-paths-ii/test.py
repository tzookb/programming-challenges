import unittest
import dp


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.s = dp.Solution()

    def getRes(self, grid):
        return self.s.uniquePathsWithObstacles(grid)

    def test_end_is_obstacle(self):
        grid = [[0, 1]]
        res = self.getRes(grid)
        self.assertEqual(0, res)
        grid = [
            [0, 0],
            [0, 1],
        ]
        res = self.getRes(grid)
        self.assertEqual(0, res)

if __name__ == '__main__':
    unittest.main()