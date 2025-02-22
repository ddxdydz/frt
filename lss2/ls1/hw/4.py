a = int(input("Введите значение a (-10 до 10): "))
b = int(input("Введите значение b (-10 до 10): "))

if a > 0 and b > 0:
    print(f"Разность a и b: {a - b}")
elif a < 0 and b < 0:
    print(f"Произведение a и b: {a * b}")
else:
    print(f"Сумма a и b: {a + b}")
