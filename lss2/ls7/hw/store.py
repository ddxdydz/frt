from modules.admins import *
from modules.cart import *
from modules.items import *

admin_authorized = False

while 1:
    choise = int(input('Выберите пункт меню:\n1) Показать каталог товаров'
               '\n2) Добавить товар в каталог товаров'
               '\n3) Добавить товар в корзину покупок'
               '\n4) Редактировать стоимость товара'
               '\n5) Удалить товар'
               '\n6) Вывести корзину покупок'
               '\n7) Добавить товар в корзину покупок'
               '\n8) Убрать товар из корзины покупок'
               '\n9) Зарегистрировать администратора'
               '\n10) Войти как администратор'
               '\n11) Выход\n').strip())
    
    match(choise):
        case 1:
            show_items()
        case 2:
            if admin_authorized:
                add_item()
            else:
                print("Это действие может выполнять только администратор.")
        case 3:
            add_item_cart()
        case 4:
            if admin_authorized:
                edit_price()
            else:
                print("Это действие может выполнять только администратор.")
        case 5:
            if admin_authorized:
                remove_item()
            else:
                print("Это действие может выполнять только администратор.")
        case 6:
            show_cart()
        case 7:
            add_item_cart()
        case 8:
            remove_item_cart()
        case 9:
            register()
        case 10:
            if login():
                admin_authorized = True
        case 11:
           break
        case _:
            print("Вы ввели некорректный номер пункта меню!")
