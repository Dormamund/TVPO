def calculate_monthly_payment(principal, annual_interest_rate, years):
    """
    Рассчитывает ежемесячный платеж по ипотеке.
    """
    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_months = years * 12

    if monthly_interest_rate == 0:  # Если процентная ставка равна 0
        return principal / total_months

    monthly_payment = (
        principal * monthly_interest_rate
        * (1 + monthly_interest_rate) ** total_months
    ) / ((1 + monthly_interest_rate) ** total_months - 1)

    return monthly_payment


def calculate_total_payment(monthly_payment, years):
    """
    Рассчитывает общую сумму выплат по ипотеке.
    """
    return monthly_payment * years * 12


def main():
    """
    Основная функция для запуска калькулятора.
    """
    print("Добро пожаловать в калькулятор ипотеки!")
    principal = float(input("Введите сумму кредита (руб): "))
    annual_interest_rate = float(input("Введите годовую процентную ставку (%): "))
    years = int(input("Введите срок кредита (лет): "))

    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
    total_payment = calculate_total_payment(monthly_payment, years)

    print(f"\nЕжемесячный платеж: {monthly_payment:.2f} руб.")
    print(f"Общая сумма выплат: {total_payment:.2f} руб.")


if __name__ == "__main__":
    print("Hello World")
    main()
