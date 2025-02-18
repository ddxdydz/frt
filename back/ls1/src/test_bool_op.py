num_day = int(input("Введите номер дня недели от 1 до 7\n"))

is_work_day = num_day > 0 and num_day < 6
is_weekend = num_day == 6 or num_day == 7
print(f"День №{num_day} это будний день? Ответ: {is_work_day}")
print(f"День №{num_day} это выходной день? Ответ: {is_weekend}")