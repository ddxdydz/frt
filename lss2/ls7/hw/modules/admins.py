from utils.get_max_id import get_max_id

MIN_LOGIN_LENGHT = 3
MIN_PASSWORD_LENGHT = 3

admins = [
    {
        'id':1,
        'login':'admin',
        'password':'12345'
    },
    {
        'id':2,
        'login':'test',
        'password':'123'
    }
]


def register():
    login = input("Введите логин\n").strip()
    
    if ' ' in login:
        print("Неверный формат логина: в логине не должно быть пробелов!")
        return False

    if len(login) < MIN_LOGIN_LENGHT:
        print(f"Неверный формат логина: длина логина в символах должна быть минимум {MIN_LOGIN_LENGHT}")
        return False
    
    password = input("Пароль\n").strip()

    if ' ' in password:
        print("Неверный формат пароля: в пароле не должно быть пробелов!")
        return False

    if len(password) < MIN_LOGIN_LENGHT:
        print(f"Неверный формат пароля: длина пароля в символах должна быть минимум {MIN_PASSWORD_LENGHT}")
        return False
    
    admins.append({'id': get_max_id(admins) + 1, 'login': login, 'password': password})
    print("Администратор добавлен")
    return True


def login():
    login = input("Введите логин\n").strip()
    password = input("Пароль\n").strip()
    for admin in admins:
        if admin["login"] == login:
            if admin["password"] == password:
                print("Вы вошли как администратор")
                return True
    print("Неправильный логин или пароль")
    return False
