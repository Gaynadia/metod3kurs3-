"""Заданние 2"""
class Student:
    def __init__(self, name: str, familia: str, group: str, gp: float = 0.0) -> None:
        self.name = name
        self.familia = familia
        self.group = group
        self.gp = gp

    def info(self) -> str:
        return (f" Студент: {self.familia} {self.name} Группа: {self.group} Средний балл: {self.gp:.2f}" )

    def set_gp(self, new_gp: float) -> None:
        if not (0.0 <= new_gp <= 5.0):
            raise ValueError("Средний балл должен быть в диапазоне от 0.0 до 5.0")
        self.gp = new_gp

"""Заданние 8"""
class Counter:
    def __init__(self, initial: int = 0, step: int = 1) -> None:
        if step <= 0:
            raise ValueError("Шаг изменения должен быть положительным числом")
        self._value = initial
        self.step = step

    @property
    def value(self) -> int:
        """текущее значение счётчика"""
        return self._value

    def increment(self) -> int:
        """увеличивает счётчик на step"""
        self._value += self.step
        return self._value

    def decrement(self) -> int:
        """уменьшает счётчик на step"""
        self._value -= self.step
        return self._value

    def reset(self, new_value: int = 0) -> None:
        """сбрасывает значение счётчика"""
        self._value = new_value

"""Заданние 10"""
class StepRangeIterator:
    def __init__(self, start: int, stop: int, step: int = 1) -> None:
        if step <= 0:
            raise ValueError("Шаг должен быть > 0")
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current >= self.stop:
            raise StopIteration
        result = self.current
        self.current += self.step
        return result

"""Заданние 3, повышка"""
class Product:
    """Класс товары магазина"""

    def __init__(self, product_id: int, title: str, price: float) -> None:
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.product_id = product_id
        self.title = title
        self.price = float(price)

    def __repr__(self) -> str:
        return f"Product(id={self.product_id}, title='{self.title}', price={self.price:.2f})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return False
        return self.product_id == other.product_id

    def __hash__(self) -> int:
        return hash(self.product_id)


class Cart:
    """корзина покупателя"""

    def __init__(self) -> None:
        self.items: dict[Product, int] = {}

    def add_product(self, product: Product, quantity: int = 1) -> None:
        """Добавляет товар в корзину"""
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным целым числом")
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_product(self, product: Product) -> None:
        """уаляет товар из корзины"""
        if product in self.items:
            del self.items[product]

    def get_total_price(self, discount: float = 0.0) -> float:
        if not (0.0 <= discount <= 1.0):
            raise ValueError("Скидка должна выражаться дробью от 0.0 до 1.0, ну все таки процентики")
        total = sum(product.price * count for product, count in self.items.items())
        return round(total * (1.0 - discount), 2)

    def clear(self) -> None:
        """Очищает корзину"""
        self.items.clear()