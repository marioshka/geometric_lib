import unittest
from unittest.mock import patch
import circle
import square

def calc(fig, func, size):
    assert fig in ['circle', 'square']
    assert func in ['perimeter', 'area']
    return eval(f'{fig}.{func}(*{size})')

class TestCalcFunction(unittest.TestCase):

    @patch('circle.area', return_value=3.14)
    @patch('square.area', return_value=4)
    def test_area(self, mock_square_area, mock_circle_area):
        self.assertEqual(calc('circle', 'area', [1]), 3.14)
        self.assertEqual(calc('square', 'area', [2]), 4)

    @patch('circle.perimeter', return_value=6.28)
    @patch('square.perimeter', return_value=8)
    def test_perimeter(self, mock_square_perimeter, mock_circle_perimeter):
        self.assertEqual(calc('circle', 'perimeter', [1]), 6.28)
        self.assertEqual(calc('square', 'perimeter', [2]), 8)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc('triangle', 'area', [1, 2, 3])

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('circle', 'volume', [1])

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            calc('circle', 'area', ['invalid_size'])

if name == 'main':
    unittest.main()
