import unittest
import sys
import os

# Добавляем родительскую директорию в путь для импорта
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app


class TestApp(unittest.TestCase):
    """
    Тесты для Flask приложения
    """

    def setUp(self):
        """Подготовка тестового клиента"""
        self.app = app.test_client()
        self.app.testing = True
        print("🔧 Подготовка тестового клиента...")

    def test_index_page(self):
        """Тест главной страницы"""
        print("🧪 Тест: Главная страница")

        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Калькулятор ипотеки', response.data)
        print("   ✓ Статус 200 OK")
        print("   ✓ Заголовок присутствует")

    def test_health_check(self):
        """Тест проверки здоровья приложения"""
        print("🧪 Тест: Проверка здоровья")

        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')
        self.assertEqual(data['service'], 'mortgage-calculator')
        print("   ✓ Статус healthy")
        print("   ✓ Корректные данные JSON")

    def test_page_content(self):
        """Тест содержимого страницы"""
        print("🧪 Тест: Содержимое страницы")

        response = self.app.get('/')
        html = response.data.decode('utf-8')

        # Проверяем наличие ключевых элементов
        self.assertIn('Сумма кредита', html)
        self.assertIn('Годовая процентная ставка', html)
        self.assertIn('Срок кредита', html)
        self.assertIn('Рассчитать ипотеку', html)
        print("   ✓ Все ключевые элементы присутствуют")


if __name__ == '__main__':
    print("🎯 Запуск тестов приложения...")
    unittest.main(verbosity=2)