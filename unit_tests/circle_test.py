import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_string_type_area(self):
        self.assertEqual(area("5"), 78.53981633974483)
        self.assertEqual(area("10"), 314.1592653589793)

    def test_wrong_value_area(self):
        self.assertRaises(ValueError, area, -5)
        self.assertRaises(ValueError, area, "-5")

    def test_zero_area(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(area("0"), 0)

    def test_area(self):
        self.assertEqual(area(5), 78.53981633974483)
        self.assertEqual(area(10), 314.1592653589793)

    def test_string_type_perimeter(self):
        self.assertEqual(perimeter("5"), 31.41592653589793)
        self.assertEqual(perimeter("10"), 62.83185307179586)

    def test_wrong_value_perimeter(self):
        self.assertRaises(ValueError, perimeter, -5)
        self.assertRaises(ValueError, perimeter, "-5")

    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter("0"), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 31.41592653589793)
        self.assertEqual(perimeter(10), 62.83185307179586)
