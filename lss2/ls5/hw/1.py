import random

questions = [
    {"question": "Столица Франции?", "answers": {"A": "Берлин", "B": "Мадрид", "C": "Париж", "D": "Рим"}, "correct": "C"},
    {"question": "Самая высокая гора в мире?", "answers": {"A": "Килиманджаро", "B": "Эверест", "C": "К2", "D": "Канченджанга"}, "correct": "B"},
    {"question": "Сколько планет в Солнечной системе?", "answers": {"A": "7", "B": "8", "C": "9", "D": "10"}, "correct": "B"},
    {"question": "Какой химический элемент обозначается символом H?", "answers": {"A": "Helium", "B": "Hydrogen", "C": "Oxygen", "D": "Carbon"}, "correct": "B"},
    {"question": "Автор романа \"Война и мир\"?", "answers": {"A": "Лермонтов", "B": "Пушкин", "C": "Толстой", "D": "Достоевский"}, "correct": "C"}
]

def display_question(question):
    print(question["question"])
    for key, value in question["answers"].items():
        print(f"{key}: {value}")

def get_answer():
    while True:
        answer = input("Ваш ответ (A, B, C или D): ").upper()
        if answer in tuple("A", "B", "C", "D"):
            return answer
        else:
            print("Неверный формат ответа. Попробуйте еще раз.")

def play_game():
    score = 0
    random.shuffle(questions) #Перемешиваем вопросы для случайности

    for i, question in enumerate(questions):
        print(f"\nВопрос {i+1}:")
        display_question(question)
        answer = get_answer()
        if answer == question["correct"]:
            print("Правильно!")
            score += 1
        else:
            print(f"Неправильно. Правильный ответ: {question['correct']}")
            break # Игра заканчивается при неправильном ответе

    print(f"\nИгра окончена! Ваш счет: {score} из {len(questions)}")


play_game()
