# my_tuple = (1,2,3,4,5)
# my_tuple2 = tuple([1,2,3,4,5])
#
# print(my_tuple2)

# Пример 1
# Найти сумму элементов списка в котором в качестве значений могут быть кортежи

# nums = [1,2,3,4,(10,20),1]
# sum = 0
#
#
# for item in nums:
#     if isinstance(item,tuple):#проверка каждого значения списка на кортеж
#         for i in item:
#             sum += i
#     else:
#         sum += item
#
# print(sum)

# Пример 2

# s = (1,)
# print(type(s))

# a = (1,2,3)
# b = (3,2,1)
# print(a + b)

# a = [1,2,3]
# b = [3,2,1]
# print(a + b) #[1, 2, 3, 3, 2, 1]
