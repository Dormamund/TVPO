import pytest
from main import calculate_monthly_payment, calculate_total_payment

def test_calculate_monthly_payment():
    # Тест с реальными данными
    principal = 3000000  # 3,000,000 руб.
    annual_interest_rate = 6.5  # 6.5%
    years = 20  # 20 лет

    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
    assert round(monthly_payment, 2) == 50000  # Ожидаемый результат (22367.19)
def test_dummy():
    pass
