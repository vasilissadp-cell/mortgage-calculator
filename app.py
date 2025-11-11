from flask import Flask
from calculator import MortgageCalculator

# Создаем экземпляр Flask приложения
app = Flask(__name__)
# Создаем экземпляр калькулятора
calculator = MortgageCalculator()


@app.route('/')
def index():
    """
    Главная страница с калькулятором ипотеки
    """
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Калькулятор ипотеки</title>
        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }

            body {
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: #333;
                background-color: #f4f4f4;
                padding: 20px;
            }

            .container {
                max-width: 600px;
                margin: 0 auto;
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }

            h1 {
                text-align: center;
                color: #2c3e50;
                margin-bottom: 30px;
            }

            .form-group {
                margin-bottom: 20px;
            }

            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
                color: #555;
            }

            input {
                width: 100%;
                padding: 10px;
                border: 2px solid #ddd;
                border-radius: 5px;
                font-size: 16px;
            }

            input:focus {
                border-color: #007bff;
                outline: none;
            }

            button {
                width: 100%;
                padding: 12px;
                background: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 18px;
                cursor: pointer;
                transition: background 0.3s;
            }

            button:hover {
                background: #0056b3;
            }

            .result {
                margin-top: 30px;
                padding: 20px;
                background: #e8f4ff;
                border-radius: 5px;
                border-left: 4px solid #007bff;
            }

            .result h3 {
                color: #2c3e50;
                margin-bottom: 15px;
            }

            .result p {
                margin-bottom: 10px;
                font-size: 16px;
            }

            .error {
                margin-top: 15px;
                padding: 10px;
                background: #ffe8e8;
                border: 1px solid #ffcccc;
                border-radius: 5px;
                color: #d63031;
            }

            .summary-item {
                display: flex;
                justify-content: space-between;
                margin-bottom: 8px;
                padding: 8px;
                background: white;
                border-radius: 4px;
            }

            .summary-value {
                font-weight: bold;
                color: #2c3e50;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🏠 Калькулятор ипотеки</h1>

            <div class="form-group">
                <label for="principal">Сумма кредита (руб):</label>
                <input type="number" id="principal" value="1000000" step="1000" min="1">
            </div>

            <div class="form-group">
                <label for="annual_rate">Годовая процентная ставка (%):</label>
                <input type="number" id="annual_rate" value="7.5" step="0.1" min="0" max="100">
            </div>

            <div class="form-group">
                <label for="years">Срок кредита (лет):</label>
                <input type="number" id="years" value="20" step="1" min="1" max="50">
            </div>

            <button onclick="calculateMortgage()">📊 Рассчитать ипотеку</button>

            <div id="result" class="result" style="display: none;">
                <h3>📈 Результаты расчета:</h3>
                <div id="summary"></div>
            </div>

            <div id="error" class="error" style="display: none;"></div>
        </div>

        <script>
            function calculateMortgage() {
                // Получаем значения из полей ввода
                const principal = parseFloat(document.getElementById('principal').value);
                const annual_rate = parseFloat(document.getElementById('annual_rate').value);
                const years = parseInt(document.getElementById('years').value);

                // Скрываем предыдущие результаты и ошибки
                document.getElementById('error').style.display = 'none';
                document.getElementById('result').style.display = 'none';

                // Проверяем валидность данных
                if (isNaN(principal) || principal <= 0) {
                    showError('Введите корректную сумму кредита');
                    return;
                }

                if (isNaN(annual_rate) || annual_rate < 0) {
                    showError('Введите корректную процентную ставку');
                    return;
                }

                if (isNaN(years) || years <= 0) {
                    showError('Введите корректный срок кредита');
                    return;
                }

                // Выполняем расчет
                const monthly_rate = annual_rate / 100 / 12;
                const months = years * 12;

                let monthly_payment;
                if (monthly_rate === 0) {
                    monthly_payment = principal / months;
                } else {
                    monthly_payment = (principal * monthly_rate * Math.pow(1 + monthly_rate, months)) / 
                                    (Math.pow(1 + monthly_rate, months) - 1);
                }

                const total_payment = monthly_payment * months;
                const total_interest = total_payment - principal;

                // Показываем результаты
                displayResults({
                    monthly_payment: monthly_payment.toFixed(2),
                    total_payment: total_payment.toFixed(2),
                    total_interest: total_interest.toFixed(2)
                });
            }

            function displayResults(data) {
                const summary = document.getElementById('summary');
                summary.innerHTML = `
                    <div class="summary-item">
                        <span>Ежемесячный платеж:</span>
                        <span class="summary-value">${formatMoney(data.monthly_payment)} руб.</span>
                    </div>
                    <div class="summary-item">
                        <span>Общая сумма выплат:</span>
                        <span class="summary-value">${formatMoney(data.total_payment)} руб.</span>
                    </div>
                    <div class="summary-item">
                        <span>Общая переплата:</span>
                        <span class="summary-value">${formatMoney(data.total_interest)} руб.</span>
                    </div>
                `;

                document.getElementById('result').style.display = 'block';
            }

            function showError(message) {
                document.getElementById('error').textContent = '❌ ' + message;
                document.getElementById('error').style.display = 'block';
            }

            function formatMoney(amount) {
                // Форматируем число с пробелами между тысячами
                return parseFloat(amount).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$& ');
            }

            // Добавляем обработчик нажатия Enter
            document.addEventListener('keypress', function(event) {
                if (event.key === 'Enter') {
                    calculateMortgage();
                }
            });
        </script>
    </body>
    </html>
    """


@app.route('/health')
def health_check():
    """
    Endpoint для проверки работоспособности приложения
    """
    return {
        "status": "healthy",
        "service": "mortgage-calculator",
        "version": "1.0.0"
    }


if __name__ == '__main__':
    # Запускаем приложение
    print("🚀 Запуск калькулятора ипотеки...")
    print("📍 Приложение доступно по адресу: http://localhost:5000")
    print("❤️  Проверка здоровья: http://localhost:5000/health")
    app.run(host='0.0.0.0', port=5000, debug=False)