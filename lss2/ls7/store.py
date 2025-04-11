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

items = [
    {
        'id':1,
        'title':'Audi',
        'price':1000
    },
    {
        'id':2,
        'title':'BMW',
        'price':3000
    },
    {
        'id':3,
        'title':'VW',
        'price':900
    }
]

# cart = []
# {id,count:1}


def show_items():
    print("*" * 50)
    for i,item in enumerate(items,1):
        print(f"{i}) {item['title']} стоит {item['price']} (id = {item['id']})")
    print("*" * 50)

def add_item():
    title = input("Введите название товара\n")
    price = int(input("Введите стоимость товара\n"))
    item = {
        'id':get_max_id() + 1,
        'title':title,
        'price':price
    }
    items.append(item)
    show_items()

def add_item_cart():
    pass

def get_max_id():
    max_id = 0
    for item in items:
        if item['id'] > max_id:
            max_id = item['id']
    return max_id


def edit_price():
    item_id = int(input('Введите id товара у которого меняем стоимость\n'))
    for item in items:
        if item['id'] == item_id:
            item['price'] = int(input(f"Введите новую стоимость для {item['title']}"))
            show_items()
            break
    else:
        print("Вы ввели несуществующий ID")

def remove_item():
    item_id = int(input('Введите id товара, который нужно удалить\n'))
    for i,item in enumerate(items):
        if item['id'] == item_id:
            print(f"Товар {items.pop(i)['title']} был удален!")
            show_items()
            break
    else:
        print("Товар не найден")


def show_cart():
    pass


while 1:
    choise = int(input('Выберите пункт меню:\n1) Показать каталог товаров'
                   '\n2) Добавить товар в каталог товаров'
                   '\n3) Добавить товар в корзину покупок'
                   '\n4) Редактировать стоимость товара'
                   '\n5) Удалить товар'
                   '\n6) Вывести корзину покупок'
                   '\n7) Выход\n').strip())
    match(choise):
        case 1:
            show_items()
        case 2:
            add_item()
        case 3:
            add_item_cart()
        case 4:
            edit_price()
        case 5:
            remove_item()
        case 6:
            show_cart()
        case 7:
           break
        case _:
            print("Вы ввели некорректный номер пункта меню!")
