from decimal import Decimal
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).parent


class CalculatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('calc', ROOT / 'calculator.py')
        cls.calc = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.calc)

    def test_add(self):
        self.assertEqual(self.calc.calculate('0.1', '+', '0.2'), Decimal('0.3'))

    def test_subtract(self):
        self.assertEqual(self.calc.calculate('5', '-', '8'), Decimal('-3'))

    def test_multiply(self):
        self.assertEqual(self.calc.calculate('-2.5', '*', '4'), Decimal('-10'))

    def test_divide(self):
        self.assertEqual(self.calc.calculate('10', '/', '4'), Decimal('2.5'))

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            self.calc.calculate('1', '/', '0')

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calc.calculate('1', '**', '2')

    def test_invalid_number(self):
        for number in ['abc', 'NaN', 'Infinity']:
            with self.assertRaises(ValueError):
                self.calc.calculate(number, '+', '2')


if __name__ == '__main__':
    unittest.main(verbosity=2)
