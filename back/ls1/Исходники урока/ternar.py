day = input("Введите номер дня недели\n")
if day.isdigit():
    day = int(day)
    if 1 <= day <= 7:
        print("Будний день" if 0 < day < 6 else "Выходной день")
    else:
        print("Вы ввели некорректное значение")
else:
    print("Вы ввели не число")