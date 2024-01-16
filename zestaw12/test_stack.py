# Kod testujący moduł.

from stack import Stack
import unittest

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack1 = Stack()
        for i in range(5):
            self.stack1.push(i)

        self.stack2 = Stack()
        for i in range(5):
            self.stack2.push(i)

        self.stack_full = Stack()
        for i in range(10):
            self.stack_full.push(i)

        self.stack_empty = Stack()

    def test_pop(self):
        self.stack1.pop()
        self.assertEqual(self.stack1.storage, list(range(4)) + [None] * 6)
        with self.assertRaises(IndexError):
            self.stack_empty.pop()

    def test_push(self):
        self.stack2.push(5)
        self.assertEqual(self.stack2.storage, list(range(6)) + [None] * 4)
        with self.assertRaises(IndexError):
            self.stack_full.push(100)

    def test_is_full(self):
        self.assertTrue(self.stack_full.is_full())
        self.assertFalse(self.stack_empty.is_full())
        self.assertFalse(self.stack1.is_full())
        self.assertFalse(self.stack2.is_full())


    def test_is_empty(self):
        self.assertFalse(self.stack_full.is_empty())
        self.assertTrue(self.stack_empty.is_empty())
        self.assertFalse(self.stack1.is_empty())
        self.assertFalse(self.stack2.is_empty())

    def tearDown(self): 
        pass

if __name__ == "__main__":
    unittest.main()  # wszystkie testy