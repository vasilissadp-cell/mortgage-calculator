from flask import Flask
from calculator import MortgageCalculator

app = Flask(__name__)
calculator = MortgageCalculator()


@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Калькулятор ипотеки</title>
        <style>
            body { font-family: Arial; margin: 40px; }
            .container { max-width: 600px; margin: 0 auto; }
            .form-group { margin-bottom: 15px; }
            label { display: block; margin-bottom: 5px; font-weight: bold; }
            input { padding: 8px; width: 200px; }
            button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
            .result { margin-top: 20px; padding: 15px; background: #f8f9fa; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Калькулятор ипотеки</h1>
            <div class="form-group">
                <label for="principal">Сумма кредита (руб):</label>
                <input type="number" id="principal" value="1000000">
            </div>
            <div class="form-group">
                <label for="annual_rate">Процентная ставка (%):</label>
                <input type="number" id="annual_rate" value="7.5">
            </div>
            <div class="form-group">
                <label for="years">Срок кредита (лет):</label>
                <input type="number" id="years" value="20">
            </div>
            <button onclick="calculate()">Рассчитать</button>
            <div id="result" class="result" style="display: none;"></div>
        </div>

        <script>
            function calculate() {
                const principal = parseFloat(document.getElementById('principal').value);
                const annual_rate = parseFloat(document.getElementById('annual_rate').value);
                const years = parseInt(document.getElementById('years').value);

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

                document.getElementById('result').innerHTML = `
                    <h3>Результаты:</h3>
                    <p>Ежемесячный платеж: ${monthly_payment.toFixed(2)} руб.</p>
                    <p>Общая сумма выплат: ${total_payment.toFixed(2)} руб.</p>
                    <p>Переплата: ${total_interest.toFixed(2)} руб.</p>
                `;
                document.getElementById('result').style.display = 'block';
            }
        </script>
    </body>
    </html>
    """


@app.route('/health')
def health():
    return {"status": "healthy"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)