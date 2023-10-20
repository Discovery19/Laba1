salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03 + 1  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

budget = salary - spend
k_price = increase
for i in range(1, 10):
    budget += salary - spend * k_price
    k_price *= increase
money_capital = round(-1 * budget)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
