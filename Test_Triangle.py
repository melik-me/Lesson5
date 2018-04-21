import unittest

from Task6 import does_it_exist

class TriangleTest(unittest.TestCase):
    def test_large_side(self):
        res = does_it_exist(3, 4, 5)
        self.assertEqual(res, False)




# if __name__ == "__main__":
#     unittest.main()