#Пример 1

# Если нужно принимать неограниченное количество параметров, то используйте в последнем параметре
# оператор *. Данный оператор упаковывает все поступающие в функцию значения в кортеж.Кортеж - это статический
# список:

# def get_sum(a,b,*x):
#     s = a + b
#     for item in x: #item - это переменная, которая принимает каждое значение из кортежа
#         s += item
#     return s
#
# print(get_sum(1,2,3,4,8,6,2))


# Пример 2
# def func():
#     return 10,20,(1,2,3,(5,6),7),9
#
# print(func()[2][3][0])


# Пример 3
# Вложенные функции - это функции, которые вложены в другие функции. Вложенные функции
# могут обращаться к переменным внешней функции. Внешние функции не видят содержимое вложенной функции,
# но внешние функции знают, что есть вложенные функции и могут их запускать

# def pc(title,on = False):
#     def ram(size = 512):
#         print(f"Модуль оперативной памяти для ПК {title} запущен")
#     def hard(size = 1):
#         print(f"Жесткий диск для ПК {title} имеет емкость {size}ТБ")
#
#     return ram,hard
#
# pc("ACER")[0](1024)

# Замыкание функций имеет цель - генерация новых функций
#
# def outer(a):
#     def sum(b):
#         return a + b
#     return sum
#
# sum_ten = outer(10)
# print(sum_ten(7))
# print(sum_ten(5))
# print(sum_ten(2))
#
# sum_two = outer(2)
# print(sum_two(7))
# print(sum_two(5))
# print(sum_two(2))

# Пример 4 (Передача функций в аргументе)

# def sum(a,b):
#     return a + b
# def calc(a,b,c):
#     print(a(b,c))
#
# calc(sum,2,4)

# Пример 5 (Лямбда)
# def sum(a,b):
#    return a + b

# Лямбда выражения - это более компактный вариант записи функции.
# Формула: lambda параметры функции : тело функции. В теле функции допускается только одно выражение.
# Оператор return используется по умолчанию

# sum = lambda a,b : a + b
# print(sum(2,3))

# is_even = lambda x : True if x % 2 == 0 else False
# is_even = lambda x : x % 2 == 0
# print(is_even(9))

# Пример - создание калькулятора

# sum = lambda a,b : a + b
# dif = lambda a,b : a - b
# comp = lambda a,b : a * b
# div = lambda a,b : a / b if b != 0 else None
#
# def calc(sign,a,b):
#     match sign:
#         case "+":
#             print(sum(a,b))
#         case "-":
#             print(dif(a, b))
#         case "*":
#             print(comp(a, b))
#         case "/":
#             print(div(a, b))
#
# calc("*",2,3)

# Способ №2
# calc = lambda sign,a,b: print((lambda a,b : a + b if sign == '+' else a - b if sign == '-' else a * b if sign == '*' else a / b if b != 0 else None)(a,b))
# calc("*",3,4)

# calc = lambda sign,x,y : eval(str(x) + sign + str(y)) if not(y == 0 and sign == '/') else "На 0 делить нельзя"
# print(calc("+",2,3))

# print(eval("2 + 3"))