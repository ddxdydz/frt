from utils.get_max_id import get_max_id

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


def show_items():
    print("*" * 50)
    for i,item in enumerate(items,1):
        print(f"{i}) {item['title']} стоит {item['price']} (id = {item['id']})")
    print("*" * 50)


def add_item():
    title = input("Введите название товара\n")
    price = int(input("Введите стоимость товара\n"))
    item = {
        'id': get_max_id(items) + 1,
        'title':title,
        'price':price
    }
    items.append(item)
    show_items()


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
