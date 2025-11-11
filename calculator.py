class MortgageCalculator:
    """
    Калькулятор для расчета ипотечных платежей
    """

    def calculate_monthly_payment(self, principal, annual_rate, years):
        """
        Расчет ежемесячного платежа по ипотеке
        """
        monthly_rate = annual_rate / 100 / 12
        months = years * 12

        if monthly_rate == 0:
            return round(principal / months, 2)

        # Формула аннуитетного платежа - исправленная версия
        numerator = principal * monthly_rate * (1 + monthly_rate) ** months
        denominator = (1 + monthly_rate) ** months - 1
        monthly_payment = numerator / denominator

        return round(monthly_payment, 2)

    def calculate_total_payment(self, principal, annual_rate, years):
        """
        Расчет общей суммы выплат за весь период
        """
        monthly_payment = self.calculate_monthly_payment(principal, annual_rate, years)
        total = monthly_payment * years * 12
        return round(total, 2)

    def calculate_total_interest(self, principal, annual_rate, years):
        """
        Расчет общей суммы переплаты по процентам
        """
        total_payment = self.calculate_total_payment(principal, annual_rate, years)
        interest = total_payment - principal
        return round(interest, 2)