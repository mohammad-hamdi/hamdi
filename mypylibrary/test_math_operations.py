# tests/test_math_operations.py
import unittest
from math_operations import add, multiply

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 3), -3)

if __name__ == "__main__":
    unittest.main()
# tests/test_string_operations.py
import unittest
from string_operations import reverse_string, capitalize_words

class TestStringOperations(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python programming"), "Python Programming")

if __name__ == "__main__":
    unittest.main()
