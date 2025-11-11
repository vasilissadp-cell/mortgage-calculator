import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class TestApp(unittest.TestCase):
    def test_file_existence(self):
        self.assertTrue(os.path.exists('app.py'))
        self.assertTrue(os.path.exists('calculator.py'))

    def test_calculator_import(self):
        try:
            from calculator import MortgageCalculator
            calc = MortgageCalculator()
            self.assertTrue(hasattr(calc, 'calculate_monthly_payment'))
        except ImportError as e:
            self.fail(f"Import error: {e}")


if __name__ == '__main__':
    unittest.main()