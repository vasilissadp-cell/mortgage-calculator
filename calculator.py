class MortgageCalculator:
    def calculate_monthly_payment(self, principal, annual_rate, years):
        monthly_rate = annual_rate / 100 / 12
        months = years * 12

        if monthly_rate == 0:
            return round(principal / months, 2)

        numerator = principal * monthly_rate * (1 + monthly_rate) ** months
        denominator = (1 + monthly_rate) ** months - 1
        monthly_payment = numerator / denominator

        return round(monthly_payment, 2)

    def calculate_total_payment(self, principal, annual_rate, years):
        monthly_payment = self.calculate_monthly_payment(principal, annual_rate, years)
        return round(monthly_payment * years * 12, 2)

    def calculate_total_interest(self, principal, annual_rate, years):
        total_payment = self.calculate_total_payment(principal, annual_rate, years)
        return round(total_payment - principal, 2)