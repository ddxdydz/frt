# print("Введите номер дня недели")
num_day = int(input("Введите номер дня недели\n"))

is_work_day = 0 < num_day < 6  #num_day > 0 and num_day < 6
is_weekend = num_day == 6 or num_day == 7
print(is_weekend)