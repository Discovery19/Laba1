import doctest


class Furniture:
    def __init__(self, item_name: str, price: float):
        """
        Создание и подготовка к работе объекта "Мебель".
        item_name: Название предмета мебели
        price: Цена предмета мебели
        Примеры:
        >>> furniture_item = Furniture("Sofa", 500.0)  # инициализация экземпляра класса
        """
        if not isinstance(item_name, str):
            raise TypeError("Название предмета мебели должно быть строкой")
        self.item_name = item_name

        if not isinstance(price, (int, float)):
            raise TypeError("Цена предмета мебели должна быть числом")
        if price < 0:
            raise ValueError("Цена предмета мебели не может быть отрицательным числом")
        self.price = price

    def get_price(self) -> float:
        """
        Получение текущей цены предмета мебели.
        Текущая цена предмета мебели
        Примеры:
        >>> furniture_item = Furniture("Sofa", 500.0)
        >>> furniture_item.get_price()
        500.0
        """
        return self.price

    def discount(self, discount_amount: float) -> float:
        """
        Применение скидки к цене предмета мебели.
        discount_amount: Сумма скидки
        Новая цена после применения скидки
        Примеры:
        >>> furniture_item = Furniture("Sofa", 500.0)
        >>> furniture_item.discount(100.0)
        400.0
        """
        if not isinstance(discount_amount, (int, float)):
            raise TypeError("Сумма скидки должна быть числом")
        if discount_amount < 0:
            raise ValueError("Сумма скидки не может быть отрицательной")
        self.price -= discount_amount
        return self.price


class Recipe:
    def __init__(self, dish_name: str, ingredients: list):
        """
        Создание и подготовка к работе объекта "Рецепт".
        dish_name: Название блюда
        ingredients: Список ингредиентов
        Примеры:
        >>> recipe = Recipe("Pasta Carbonara", ["pasta", "bacon", "eggs", "parmesan cheese"])  # инициализация экземпляра класса
        """
        if not isinstance(dish_name, str):
            raise TypeError("Название блюда должно быть строкой")
        self.dish_name = dish_name

        if not isinstance(ingredients, list):
            raise TypeError("Ингредиенты должны быть представлены списком")
        self.ingredients = ingredients

    def get_recipe_info(self) -> str:
        """
        Получение информации о рецепте.
        Строка с информацией о рецепте
        Примеры:
        >>> recipe = Recipe("Pasta Carbonara", ["pasta", "bacon", "eggs", "parmesan cheese"])
        >>> recipe.get_recipe_info()
        'Recipe for Pasta Carbonara: pasta, bacon, eggs, parmesan cheese'
        """
        ingredients_str = ", ".join(self.ingredients)
        return f'Recipe for {self.dish_name}: {ingredients_str}'


class Smartphone:
    def __init__(self, brand: str, model: str, year: int, storage_capacity: int, battery_life: float):
        """
        Создание и подготовка к работе объекта "Смартфон".
        brand: Бренд смартфона
        model: Модель смартфона
        year: Год выпуска смартфона
        storage_capacity: Объем памяти смартфона в гигабайтах
        battery_life: Время автономной работы батареи в часах
        Примеры:
        >>> smartphone = Smartphone("Samsung", "Galaxy S21", 2021, 128, 10.5)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд смартфона должен быть строкой")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель смартфона должна быть строкой")
        self.model = model

        if not isinstance(year, int) or year < 2000:
            raise ValueError("Год выпуска смартфона должен быть положительным целым числом после 2000 года")
        self.year = year

        if not isinstance(storage_capacity, int) or storage_capacity <= 0:
            raise ValueError("Объем памяти смартфона должен быть положительным целым числом")
        self.storage_capacity = storage_capacity

        if not isinstance(battery_life, (int, float)) or battery_life <= 0:
            raise ValueError("Время автономной работы батареи должно быть положительным числом")
        self.battery_life = battery_life

    def get_smartphone_info(self) -> str:
        """
        Получение информации о смартфоне.
        Строка с информацией о смартфоне
        Примеры:
        >>> smartphone = Smartphone("Samsung", "Galaxy S21", 2021, 128, 10.5)
        >>> smartphone.get_smartphone_info()
        'Samsung Galaxy S21 (2021), 128GB, Battery Life: 10.5 hours'
        """
        return f'{self.brand} {self.model} ({self.year}), {self.storage_capacity}GB, Battery Life: {self.battery_life} hours'


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
