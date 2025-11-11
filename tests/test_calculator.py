import unittest
import sys
import os

# Добавляем родительскую директорию в путь для импорта
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculator import MortgageCalculator


class TestMortgageCalculator(unittest.TestCase):
    """
    Тесты для калькулятора ипотеки
    """

    def setUp(self):
        """Подготовка тестового окружения"""
        self.calculator = MortgageCalculator()
        print("🔧 Подготовка тестового окружения...")

    def test_monthly_payment_calculation(self):
        """Тест расчета ежемесячного платежа"""
        print("🧪 Тест: Расчет ежемесячного платежа")

        # Тест 1: Стандартный случай
        payment = self.calculator.calculate_monthly_payment(1000000, 7.5, 20)
        self.assertAlmostEqual(payment, 8059.99, places=1)
        print(f"   ✓ Стандартный случай: {payment}")

        # Тест 2: Нулевая процентная ставка
        payment = self.calculator.calculate_monthly_payment(100000, 0, 10)
        self.assertAlmostEqual(payment, 833.33, places=1)
        print(f"   ✓ Нулевая ставка: {payment}")

        # Тест 3: Короткий срок
        payment = self.calculator.calculate_monthly_payment(500000, 5, 5)
        self.assertAlmostEqual(payment, 9435.62, places=1)
        print(f"   ✓ Короткий срок: {payment}")

    def test_total_payment_calculation(self):
        """Тест расчета общей суммы выплат"""
        print("🧪 Тест: Расчет общей суммы выплат")

        total = self.calculator.calculate_total_payment(1000000, 7.5, 20)
        self.assertAlmostEqual(total, 1934396.38, places=1)
        print(f"   ✓ Общая сумма: {total}")

    def test_total_interest_calculation(self):
        """Тест расчета общей суммы процентов"""
        print("🧪 Тест: Расчет общей суммы процентов")

        interest = self.calculator.calculate_total_interest(1000000, 7.5, 20)
        self.assertAlmostEqual(interest, 934396.38, places=1)
        print(f"   ✓ Сумма процентов: {interest}")

    def test_invalid_inputs(self):
        """Тест обработки некорректных данных"""
        print("🧪 Тест: Обработка некорректных данных")

        # Должно работать без ошибок
        try:
            self.calculator.calculate_monthly_payment(0, 5, 10)
            self.calculator.calculate_monthly_payment(100000, -5, 10)
            print("   ✓ Некорректные данные обработаны")
        except Exception as e:
            self.fail(f"Ошибка при обработке некорректных данных: {e}")


if __name__ == '__main__':
    print("🎯 Запуск тестов калькулятора...")
    unittest.main(verbosity=2)