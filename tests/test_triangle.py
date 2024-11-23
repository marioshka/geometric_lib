import unittest

def area(a, b, c):
    return (a + b + c) / 2

def perimeter(a, b, c):
    return a + b + c

class TestGeometryFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(3, 4, 5), 6.0)
        self.assertEqual(area(1, 1, 1), 1.5)
        self.assertEqual(area(2, 2, 2), 3.0)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(1, 1, 1), 3)
        self.assertEqual(perimeter(2, 2, 2), 6)

if __name__ == '__main__':
    unittest.main()
