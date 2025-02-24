import unittest
import math
import calculator

class TestCalculator(unittest.TestCase):
    def test_square_root(self):
        self.assertAlmostEqual(calculator.square_root(16), 4)
        self.assertEqual(calculator.square_root(-1), "Invalid input for square root.")

    def test_factorial(self):
        self.assertEqual(calculator.factorial(5), 120)
        self.assertEqual(calculator.factorial(-1), "Invalid input for factorial.")

    def test_natural_log(self):
        self.assertAlmostEqual(calculator.natural_log(math.e), 1)
        self.assertEqual(calculator.natural_log(-10), "Invalid input for natural logarithm.")

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertTrue("Error" in str(calculator.power("a", 3)))

if __name__ == '__main__':
    unittest.main()
