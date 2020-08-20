import unittest
import sol


class TestStringMethods(unittest.TestCase):

    def test_not_exist(self):
        s = sol.LRUCache(2)
        self.assertEqual(-1, s.get('notfound'))

    def test_put_get(self):
        s = sol.LRUCache(2)
        s.put('key', 1111)
        v = s.get('key')
        self.assertEqual(1111, v)


if __name__ == '__main__':
    unittest.main()