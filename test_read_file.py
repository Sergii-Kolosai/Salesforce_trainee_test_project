import unittest
from read_file import read_file


class TestReadFile(unittest.TestCase):
    """Test read_file.py"""

    def test_type(self):
        """Test type is str?"""
        self.assertRaises(TypeError, read_file, [4, "gg"])
        self.assertRaises(TypeError, read_file, True)
        self.assertRaises(TypeError, read_file, {2,4,5,'d'})


if __name__ == '__main__':
    unittest.main()