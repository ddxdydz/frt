class MediatorInterface:
    def notify(self, sender, event):
        pass


class Mediator(MediatorInterface):
    def __init__(self):
        self.cart = Cart(self)
        self.inventory = Inventory(self)
        self.user = User(self)

    def notify(self, sender, event):
        if event == 'added_to_cart':
            self.cart.view_cart()
        elif event == 'checkout':
            self.order_checkout()

    def order_checkout(self):
        if self.cart.items:
            print('Заказ успешно оформлен!')
            self.cart.clear_cart()
        else:
            print('Корзина пуста, добавьте товары в корзину!')


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, mediator):
        self.mediator = mediator

    def add_to_cart(self, product):
        self.mediator.cart.add_to_cart(product)


class Cart:
    def __init__(self, mediator):
        self.mediator = mediator
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)
        print(f'{product.name} добавлен в корзину.')
        self.mediator.notify(self, 'added_to_cart')

    def view_cart(self):
        if not self.items:
            print('Корзина пуста!')
        else:
            print('В корзине:')
            for item in self.items:
                print(f' - {item.name}: {item.price} рублей')

    def clear_cart(self):
        self.items.clear()
        print('Корзина очищена.')


class Inventory:
    def __init__(self, mediator):
        self.mediator = mediator
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f'Товар {product.name} добавлен на склад.')


# Пример использования
mediator = Mediator()

# Создаем продукты
product1 = Product("Книга", 500)
product2 = Product("Ноутбук", 30000)

# Добавляем продукты на склад
mediator.inventory.add_product(product1)
mediator.inventory.add_product(product2)

# Пользователь добавляет продукты в корзину
mediator.user.add_to_cart(product1)  # Книга добавлена
mediator.user.add_to_cart(product2)  # Ноутбук добавлен

# Просмотр содержимого корзины
mediator.cart.view_cart()

# Оформление заказа
mediator.notify(mediator.cart, 'checkout')
