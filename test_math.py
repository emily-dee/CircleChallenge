import unittest
from main import Circle


class Validator(unittest.TestCase):

    def test_circumference(self):
        circle10 = Circle(10)
        circle20 = Circle(20)
        circle42 = Circle(4.2)
        result = circle10.calculate_circumference()
        self.assertEqual(result, 62.83)
        result = circle20.calculate_circumference()
        self.assertEqual(result, 125.66)
        result = circle42.calculate_circumference()
        self.assertEqual(result, 26.39)

    def test_area(self):
        circle10 = Circle(10)
        circle20 = Circle(20)
        circle42 = Circle(4.2)
        result = circle10.calculate_area()
        self.assertEqual(result, 314.16)
        result = circle20.calculate_area()
        self.assertEqual(result, 1256.64)
        result = circle42.calculate_area()
        self.assertEqual(result, 55.42)

    def test_diameter(self):
        circle10 = Circle(10)
        circle20 = Circle(20)
        circle42 = Circle(4.2)
        result = circle10.calculate_diameter()
        self.assertEqual(result, 20)
        result = circle20.calculate_diameter()
        self.assertEqual(result, 40)
        result = circle42.calculate_diameter()
        self.assertEqual(result, 8.4)


if __name__ == '__main__':
    unittest.main()
