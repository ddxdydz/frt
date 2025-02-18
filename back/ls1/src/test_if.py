year = input("Введите год")
if year.isdigit(): #если год числовое значение
    year = int(year)
    if(year % 4 == 0):
        print("Вы ввели високосный год")
    else:
        print("Вы ввели невисокосный год")
else:
    print("Вы ввели нечисловое значение")