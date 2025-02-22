import random

mistakes_count = 0
total_questions = 5

for _ in range(total_questions):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    correct_answer = a * b
    
    user_answer = int(input(f"Сколько будет {a} * {b}? "))
    
    if user_answer == correct_answer:
        print("Верно!")
    else:
        print(f"Неверно! Правильный ответ: {correct_answer}")
        mistakes_count += 1

if mistakes_count > 1:
    print(f"Незачет. Вы ответили правильно на {total_questions - mistakes_count} из {total_questions} вопросов.")
else:
    print(f"Зачет! Вы ответили правильно на {total_questions - mistakes_count} из {total_questions} вопросов.")
