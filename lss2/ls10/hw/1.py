import json

def get_user_info():
    user_info = {}
    user_info['name'] = input("Введите ваше имя: ")
    user_info['email'] = input("Введите ваш email: ")
    user_info['phone'] = input("Введите ваш телефон: ")
    user_info['position'] = input("На какую должность вы претендуете: ")
    return user_info

def save_to_json(data, filename='job_application.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    user_data = get_user_info()
    save_to_json(user_data)
    print("Анкета успешно сохранена в файл 'job_application.json'.")
