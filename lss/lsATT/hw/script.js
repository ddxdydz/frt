class Size {
    constructor(name, price, calories) {
        this.name = name;
        this.price = price;
        this.calories = calories;
    }

    getPrice() {
        return this.price;
    }

    getCalories() {
        return this.calories;
    }
}

class Filling {
    constructor(name, price, calories) {
        this.name = name;
        this.price = price;
        this.calories = calories;
    }

    getPrice() {
        return this.price;
    }

    getCalories() {
        return this.calories;
    }
}

class Topping {
    constructor(name, price, calories) {
        this.name = name;
        this.price = price;
        this.calories = calories;
    }

    getPrice() {
        return this.price;
    }

    getCalories() {
        return this.calories;
    }
}

class Burger {
    constructor(size, filling, toppings) {
        this.size = size;
        this.filling = filling;
        this.toppings = toppings || [];
    }

    getPrice() {
        let totalPrice = this.size.getPrice() + this.filling.getPrice();
        for (const topping of this.toppings) {
            totalPrice += topping.getPrice();
        }
        return totalPrice;
    }

    getCalories() {
        let totalCalories =
            this.size.getCalories() + this.filling.getCalories();
        for (const topping of this.toppings) {
            totalCalories += topping.getCalories();
        }
        return totalCalories;
    }
}

// Обработчик события формы
document
    .getElementById("burgerForm")
    .addEventListener("submit", function (event) {
        event.preventDefault();

        const sizeValue = document.getElementById("size").value;
        const fillingValue = document.getElementById("filling").value;

        // Создаем объекты для размеров и начинок
        const sizes = {
            small: new Size("Маленький", 150, 20),
            large: new Size("Большой", 200, 40),
        };

        const fillings = {
            chicken: new Filling("Курица", 50, 20),
            beef: new Filling("Говядина", 70, 15),
            bacon: new Filling("Бекон", 65, 40),
        };

        // Создаем массив добавок
        const toppings = [];

        if (document.getElementById("spice").checked) {
            toppings.push(new Topping("Приправа", 15, 0));
        }

        if (document.getElementById("mayonnaise").checked) {
            toppings.push(new Topping("Майонез", 20, 5));
        }

        // Создаем бургер
        const burger = new Burger(
            sizes[sizeValue],
            fillings[fillingValue],
            toppings
        );

        // Получаем результат
        const price = burger.getPrice();
        const calories = burger.getCalories();

        // Отображаем результат
        document.getElementById("result").innerHTML = `
        <div>
            <h2>Результаты:</h2>
            <p>Стоимость: ${price} рублей</p>
            <p>Калорийность: ${calories} калорий</p>
        </div>
    `;
    });
