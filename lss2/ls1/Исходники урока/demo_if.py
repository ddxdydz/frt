# x = True
# if not x:
#     print("Да")

year = input("Введите год\n") #получили с консоли введенное значение
if year.isdigit(): #если ввели число
    year = int(year) #преобразовали строку к числу
    if year % 4 == 0:
        print("Високосный год")
    else:
        print("Год невисокосный")
else:
    print("Вы ввели некорректное значение вместо года!")