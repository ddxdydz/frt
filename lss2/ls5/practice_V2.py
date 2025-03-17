cources = ['JS1','JS2','Python','Java','C#','C++']
remove = input("Введите часть названия курса, который нужно удалить из списка")

# Вариант 1 (регистр не учитываем)
# cources = [lang for lang in cources if remove not in lang]
# print(cources)

# Вариант 2 (регистр учитываем)

print([e for e in cources if remove.upper() not in e.upper()])