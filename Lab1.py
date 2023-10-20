money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05 + 1  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0
budget = money_capital + salary - spend
k_price = increase
while budget > 0:
    month += 1
    budget = budget + salary - spend * k_price
    k_price *= increase
print("Количество месяцев, которое можно протянуть без долгов:", month)
