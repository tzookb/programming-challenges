import unittest
import play


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.target = play.MaxStack()

    def test_push_and_peekmax(self):
        self.target.push(1)
        self.assertEqual(self.target.peekMax(), 1)
        self.target.push(2)
        self.assertEqual(self.target.peekMax(), 2)
        self.target.push(3)
        self.assertEqual(self.target.peekMax(), 3)
        self.target.push(2)
        self.assertEqual(self.target.peekMax(), 3)

    def test_push_and_popmax(self):
        self.target.push(3)
        self.assertEqual(self.target.popMax(), 3)
        self.target.push(2)
        self.assertEqual(self.target.peekMax(), 2)
        self.assertEqual(self.target.popMax(), 2)

    def test_push_and_top(self):
        self.target.push(1)
        self.assertEqual(self.target.top(), 1)
        self.target.push(2)
        self.assertEqual(self.target.top(), 2)
        self.target.push(3)
        self.assertEqual(self.target.top(), 3)

    def test_push_and_top(self):
        self.target.push(5)
        self.target.push(1)
        self.target.push(5)
        self.target.print()
        self.assertEqual(self.target.top(), 5)
        self.assertEqual(self.target.popMax(), 5)
        self.target.print()
        self.assertEqual(self.target.top(), 1)
        self.target.print()

if __name__ == '__main__':
    unittest.main()