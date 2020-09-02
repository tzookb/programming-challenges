import unittest
import sol


class TestStringMethods(unittest.TestCase):

    def test_rotate_middle(self):
        res = (sol.Solution()).find_rotate_index([4,5,1,2,3])
        self.assertEqual(2, res)

    def test_rotate_no(self):
        res = (sol.Solution()).find_rotate_index([1,2,3])
        self.assertEqual(0, res)

    def test_rotate_last(self):
        res = (sol.Solution()).find_rotate_index([1,2,3,0])
        self.assertEqual(3, res)

    def test_binary_search_first(self):
        res = (sol.Solution()).binary_search([1,2,3,4], 1, 0, 3)
        self.assertEqual(0, res)

    def test_binary_search_sec(self):
        res = (sol.Solution()).binary_search([1,2,3,4], 2, 0, 3)
        self.assertEqual(1, res)

    def test_binary_searchthird(self):
        res = (sol.Solution()).binary_search([1,2,3,4], 3, 0, 3)
        self.assertEqual(2, res)

    def test_binary_search_last(self):
        res = (sol.Solution()).binary_search([1,2,3,4], 4, 0, 3)
        self.assertEqual(3, res)

    def test_binary_search_not_found(self):
        res = (sol.Solution()).binary_search([1,2,3,4], 5, 0, 3)
        self.assertEqual(-1, res)


if __name__ == '__main__':
    unittest.main()