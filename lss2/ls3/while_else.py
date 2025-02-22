from random import randint

# is_exit = False
i = 1
while i <= 10:
    print(randint(1,10))
    if input('Для выхода введите -1') == '-1':
        # is_exit = True
        break
    i += 1
else:
    # Если оператор break не был запущен, то выполняется данный блок else
    print("Принудительного выхода не было")