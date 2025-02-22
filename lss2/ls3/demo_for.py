# range - генерирует набор чисел
# [1,2,3,4,5,6,7,8,9]
# print(list(range(1,10)))

# print(list(range(10))) #[0-9]

# print(list(range(1,10,3))) #[1, 4, 7]

# Конструкция цикла for:
# for item in range(1,6):
#     print(item)

# items = [1,2,3,4,5]
# i = 0
# while i < len(items):
#     print(items[i])
#     i += 1

# Найдем сумму чисел через for
#
# s = 0
# for i in range(11) :
#     s += i;

# Пример на цикл for/else

for i in range(1,10):
    if i == 50:
        print("Достигнуто значение 5")
        break
else:
    print("Условие в цикле ни разу не выполнилось!")