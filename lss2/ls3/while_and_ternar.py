# Посчитаем сумму нечетных чисел от 0 до 50

s,i = 0,0
# while i < 50:
#     if i % 2 != 0:
#         s += i
#     i += 1
# print(s)

# 2ой способ решения

while i < 50:
    s += i if i % 2 != 0 else 0
    i += 1
print(s)