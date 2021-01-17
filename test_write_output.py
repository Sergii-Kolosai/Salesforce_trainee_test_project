import unittest
from write_output import write_output


class TestWriteOutput(unittest.TestCase):
    """Test write_output.py"""

    def test_type_var1(self):
        """Test type is list for var1 and str for var2?"""
        self.assertRaises(TypeError, write_output, "hh", ['ff',2,4])
        self.assertRaises(TypeError, write_output, True, 66)
        self.assertRaises(TypeError, write_output, {2,4,5,'d'}, False)


if __name__ == '__main__':
    unittest.main()