# Пример №1

# items = [1,2,3,4,5,6,7,8]
# print(items[::3])


# Пример №2
# Построить 1 список, содержащий 5 повторений значений 1,2,3
# list = [1,2,3] * 5
# print(list)

# Пример №3
# Построить список от 1 по 5
# list1 = [1,2,3,4,5]
# list2 = list(range(1,6))
# print(list2)

# Пример №4: Проверка на равенство
# list1 = [1,2,3,4,5]
# list2 = list(range(1,6))
# print(id(list1))
# print(id(list2))
#
# print("Равны" if list1 is list2 else "Не равны") #хэш коды объектов не равны

# Пример №5. Заполнение списка рандомными значениями

from random import randint

# numbers = []
# for i in range(10):
#     numbers.append(randint(0,9)) #append - добавление элемента в конец
# print(numbers)

# numbers = [randint(0,9) for i in range(10)]
# print(numbers)

# 1-ый способ сортировки
# numbers.sort() #по возрастанию

# 2ой способ сортировки
# numbers = sorted(numbers,reverse=True)
#
# print(numbers)

# Пример №6 (Поиск элемента)
langs = [item.upper() for item in ['java','python','js','c#']]
# print(langs)
# Виды поиска
# 1) Через in
# print("Найдено" if input("Введите искомое значение").upper() in langs else "Не найдено")

# 2) __contains__
# print(langs.__contains__('JS'))

# Получение индекса у искомого элемента
# Метод index нужно применять к гарантированно существующим значениям списка
# print(langs.index('JS1')) #будет ошибка

# Вставка элемента в произвольное место списка - insert

# langs.insert(0,'PHP') #вставка элемент на индекс 0
# print(langs)

# Удаление элемента из списка
# 1) pop() - удаление последнего элемента списка
#    pop(index) - удаление по индексу
#    Метод удаляет элемент, который был удален
# print(langs.pop(0))

# 2) remove() - удаление по значению
# langs.remove("JS")
# print(langs)

# Если нужно узнать количество повторений элемента в списке - используйте count

# x = [1,2,3,5,1,2,1]
# print(x.count(1))


# Практика - нотариус

COUNT = 5
clients = []

while 1:
    clients.append(input("Введите Ваше имя\n"))
    if len(clients) > COUNT:
        print(f"Можете войти: {clients.pop(0)}, готовится {clients[0]}")

# x1 = [1,2,3,4,5]
# x1.pop(0)
# print(x1)