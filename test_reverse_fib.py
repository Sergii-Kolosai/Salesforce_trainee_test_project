import unittest
from reverse_fib import reverse_fib


class TestIsFib(unittest.TestCase):
    """Test reverse_fib.py"""

    def test_type(self):
        """Test type is list?"""
        self.assertRaises(TypeError, reverse_fib, '222')
        self.assertRaises(TypeError, reverse_fib, True)
        self.assertRaises(TypeError, reverse_fib, {2,4,5,'d'})

if __name__ == '__main__':
    unittest.main()