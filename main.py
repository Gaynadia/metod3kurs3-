

from models import Student, Counter, StepRangeIterator, Product, Cart


def main() -> None:


    # Задание 2
    print("\n[1] Задание 2 (Средн.): Класс «Студент»")
    student = Student("Алексей", "Мешавкин", "ИПМКН-3", 4.85)
    print(student.info())

    # Задание 8
    print("\n[2] Задание 8 (Средн.): Класс-счётчик")
    counter = Counter(initial=0, step=5)
    print(f"Старт: {counter.value}")
    print(f"Инкремент (+5): {counter.increment()}")
    print(f"Инкремент (+5): {counter.increment()}")
    print(f"Декремент (-5): {counter.decrement()}")
    counter.reset(100)
    print(f"Сброс на 100: {counter.value}")

    # Задание 10
    print("\n[3] Задание 10 (Средн.): Класс-итератор")
    seq = StepRangeIterator(start=10, stop=50, step=8)
    print("Элементы итератора (start=10, stop=50, step=8):", list(seq))

    # Задание 3
    print("\n[4] Задание 3 (Повыш.): Система заказов")
    cart = Cart()
    p1 = Product(101, "Клавиатура механическая", 4500.0)
    p2 = Product(102, "Игровая мышь", 2500.0)
    p3 = Product(103, "Коврик для мыши", 800.0)

    cart.add_product(p1, quantity=1)
    cart.add_product(p2, quantity=2)
    cart.add_product(p3, quantity=1)

    print("Товары в корзине:")
    for item, qty in cart.items.items():
        print(f" - {item.title}: {qty} шт. по {item.price:.2f} руб.")

    print(f"Итоговая сумма без скидки: {cart.get_total_price():.2f} руб.")
    print(f"Итоговая сумма со скидкой 15%: {cart.get_total_price(discount=0.15):.2f} руб.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()