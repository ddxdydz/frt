from utils.get_max_id import get_max_id

cart = []  # {id,count:1}



def show_cart():
    print("*" * 50)
    for i, item_cart in enumerate(cart):
        print(f"{i}) Количество единиц товара с id = {item_cart['id']} равно {item_cart["count"]}")
    print("*" * 50)


def add_item_cart():
    id = int(input("Введите название id товара для добавления в корзину\n"))
    for cart_item in cart:
        if cart_item["id"] == id:
            cart_item["count"] += 1
            break
    else:
        cart.append({"id": id, "count": 1})
    show_cart()


def remove_item_cart():
    id = int(input("Введите название id товара для удаления из корзины\n"))
    for i, cart_item in enumerate(cart):
        if cart_item["id"] == id:
            cart_item["count"] -= 1
            if cart_item["count"] == 0:
                cart.pop(i)
            show_cart()
            break
    else:
        print("Такого товара нет в корзине")
