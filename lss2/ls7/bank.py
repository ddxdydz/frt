"""Расчет прибыли клиента после вклада"""
def show_profit(money_param,count_years):
    """Вывод ежегодной прибыли"""
    rate = 25 if count_years >=3 else 20
    for i in range(1,count_years + 1): #i - это счетчик лет
        profit = money_param * rate / 100
        money_param += profit
        print(f"За {i} год Ваша прибыль = {round(profit,2)}, сумма стала = {round(money_param,2)}")

fio_list = ["Иванов","Петров","Сидоров"]

for item in fio_list:
    money = int(input(f"Уважаемый {item}, введите Вашу сумму\n"))
    years = int(input(f"Уважаемый {item}, введите срок вклада\n"))
    print(f"Клиент {item}:")
    show_profit(money,years)
    print("-" * 50)

# pip install pylint

