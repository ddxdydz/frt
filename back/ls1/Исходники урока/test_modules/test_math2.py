from math import fabs

# print(max(2,5,1))

a,b = int(input("Введите первое число")),int(input("Введите второе число"))

print(f"Одно число больше другого на {fabs(a - b)}")
