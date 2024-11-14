import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -10), -11)
    # Add the following test methods to the TestCalculator class:
    
    def test_substract(self):
        self.assertEqual(self.calc.subtract(-2, 8), -10)
        self.assertEqual(self.calc.subtract(-1, -10), 9)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 8), 48)
        self.assertEqual(self.calc.multiply(-9, 7), -63)

    def test_divide(self):
        self.assertEqual(self.calc.divide(17,7), 2)
        self.assertEqual(self.calc.divide(-111, -5), 22)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(213,-9), -3)
        self.assertEqual(self.calc.modulo(-155, -7), -1)

if __name__ == '__main__':
    unittest.main()