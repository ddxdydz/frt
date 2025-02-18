from datetime import datetime

birth_year = int(input("Введите ваш год рождения: "))
current_year = datetime.now().year
age = current_year - birth_year
print(f"Ваш возраст: {age} лет.")
