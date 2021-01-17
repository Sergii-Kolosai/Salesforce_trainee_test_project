import unittest
from is_fibonacci import is_fibonacci


class TestIsFib(unittest.TestCase):
    """Test is_fibonacci.py"""

    def test_result(self):
        """Test output is correct?"""
        self.assertEqual(is_fibonacci(34), True)
        self.assertEqual(is_fibonacci(33), False)

    def test_value(self):
        """Test value is positive?"""
        self.assertRaises(ValueError, is_fibonacci, -2)
        self.assertRaises(ValueError, is_fibonacci, -5)

    def test_type(self):
        """Test type is int?"""
        self.assertRaises(TypeError, is_fibonacci, [4, "gg"])
        self.assertRaises(TypeError, is_fibonacci, True)
        self.assertRaises(TypeError, is_fibonacci, {2,4,5,'d'})

if __name__ == '__main__':
    unittest.main()