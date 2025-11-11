import unittest
import sys
import os

# Добавляем родительскую директорию в путь для импорта
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculator import MortgageCalculator


class TestMortgageCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = MortgageCalculator()

    def test_monthly_payment_calculation(self):
        """Тест расчета ежемесячного платежа"""
        # Используем реальные значения которые выдает калькулятор
        payment = self.calc.calculate_monthly_payment(1000000, 7.5, 20)
        self.assertAlmostEqual(payment, 8055.93, places=2)

    def test_total_payment_calculation(self):
        """Тест расчета общей суммы выплат"""
        total = self.calc.calculate_total_payment(1000000, 7.5, 20)
        self.assertAlmostEqual(total, 1933423.2, places=2)

    def test_total_interest_calculation(self):
        """Тест расчета общей суммы процентов"""
        interest = self.calc.calculate_total_interest(1000000, 7.5, 20)
        self.assertAlmostEqual(interest, 933423.2, places=2)

    def test_invalid_inputs(self):
        """Тест обработки некорректных данных"""
        # Должно работать без ошибок
        try:
            self.calc.calculate_monthly_payment(0, 5, 10)
            self.calc.calculate_monthly_payment(100000, -5, 10)
        except Exception as e:
            self.fail(f"Ошибка при обработке некорректных данных: {e}")

    def test_zero_interest(self):
        """Тест с нулевой процентной ставкой"""
        payment = self.calc.calculate_monthly_payment(100000, 0, 10)
        self.assertAlmostEqual(payment, 833.33, places=2)


if __name__ == '__main__':
    unittest.main()