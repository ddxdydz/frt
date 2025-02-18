class ProductFlyweight:
    def __init__(self, name, price, category):
        self._name = name
        self._price = price
        self._category = category

    def display(self, quantity):
        return "Товар: {}, Цена: {}, Категория: {}, Количество: {}".format(
            self._name, self._price, self._category, quantity
        )


class ProductFactory:
    def __init__(self):
        self.products = {}

    def get_product(self, name, price, category):
        key = (name, price, category)
        if key not in self.products:
            self.products[key] = ProductFlyweight(name, price, category)
        return self.products[key]


class Order:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append((product, quantity))

    def display_order(self):
        for product, quantity in self.items:
            print(product.display(quantity))



if __name__ == "__main__":
    factory = ProductFactory()

    # Создание продуктов через фабрику
    dog_food = factory.get_product("Корм для собак", 500, "Корм")
    cat_food = factory.get_product("Корм для кошек", 400, "Корм")

    # Добавление продуктов в заказ с указанием количества
    order1 = Order()
    order1.add_product(dog_food, 2)
    order1.add_product(cat_food, 3)

    # Повторное использование тех же продуктов
    order2 = Order()
    order2.add_product(dog_food, 1)
    order2.add_product(cat_food, 5)

    # Отображение заказов
    print("Заказ 1:")
    order1.display_order()

    print("Заказ 2:")
    order2.display_order()













# Пример использования
mediator = Mediator()

# Создаем продукты
product1 = Product("Корм для собак", 500)
product2 = Product("Корм для кошек", 550)

# Добавляем продукты на склад
mediator.inventory.add_product(product1)
mediator.inventory.add_product(product2)

# Пользователь добавляет продукты в корзину
mediator.user.add_to_cart(product1)
mediator.user.add_to_cart(product2)

# Просмотр содержимого корзины
mediator.cart.view_cart()

# Оформление заказа
mediator.notify(mediator.cart, 'checkout')
