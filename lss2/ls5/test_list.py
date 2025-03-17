# my_list = [2,3,4]

# if 36 in my_list:
#     print(my_list.index(36))

# sum = lambda a,b:  a + b
# print(sum(2,3))

# my_list = map(lambda a:  a ** 2,my_list)
# print(list(my_list))

# Задание: построить список в виде [10,20,30...100]
# 1 способ
# x = []
# for i in range(10):
#     x.append((i + 1) * 10)
# print(x)

# 2ой способ
# x = [(i + 1) * 10 for i in range(10)]
# print(x)

# 3ий способ
# print(list(range(10,110,10)))

# Задание №2 - создать 3 офиса и заполнить их сотрудниками с рандомными окладами
from random import randint

def show_salaries(salaries):
    for i,item in enumerate(salaries,1): #здесь 1 это начальное значение для переменной i
        print(f"Сотрудник №{i} имеет оклад {item}")
    print('-' * 50)
    print(f"Сумма всех з/п {sum(salaries)}")
    print("-" * 50)

def create_office(address:str,count_men:int) -> list:
    print(f"В офисе по адресу {address} работает {count_men} сотрудников")
    salaries = [randint(70_000,200_000) for i in range(count_men)]
    show_salaries(salaries)
    return salaries

office1 = create_office("Москва",10)
office2 = create_office("Казань",8)
office3 = create_office("Томск",12)

print(max(max(office1),max(office2),max(office3)))
