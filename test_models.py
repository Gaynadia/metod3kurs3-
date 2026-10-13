import unittest
from models import Student, Counter, StepRangeIterator, Product, Cart


class TestStudent(unittest.TestCase):
    """Тестирование класса Student (Задание 2)."""

    def setUp(self):
        self.student = Student("Иван", "Иванов", "ИВТ-21", 4.5)

    def test_info(self):
        info = self.student.info()
        self.assertIn("Иванов Иван", info)
        self.assertIn("ИВТ-21", info)
        self.assertIn("4.50", info)

    def test_update_gp_valid(self):
        self.student.set_gp(4.9)
        self.assertEqual(self.student.gp, 4.9)

    def test_update_gp_invalid_high(self):
        with self.assertRaises(ValueError):
            self.student.set_gp(5.5)

    def test_update_gp_invalid_negative(self):
        with self.assertRaises(ValueError):
            self.student.set_gp(-0.5)


class TestCounter(unittest.TestCase):
    """Тестирование класса Counter (Задание 8)."""

    def test_counter_flow(self):
        c = Counter(initial=10, step=2)
        self.assertEqual(c.value, 10)
        self.assertEqual(c.increment(), 12)
        self.assertEqual(c.decrement(), 10)
        c.reset(0)
        self.assertEqual(c.value, 0)

    def test_invalid_step(self):
        with self.assertRaises(ValueError):
            Counter(step=0)


class TestStepRangeIterator(unittest.TestCase):
    """Тестирование итератора StepRangeIterator (Задание 10)."""

    def test_iteration(self):
        iterator = StepRangeIterator(start=2, stop=10, step=2)
        result = list(iterator)
        self.assertEqual(result, [2, 4, 6, 8])

    def test_empty_range(self):
        iterator = StepRangeIterator(start=10, stop=5)
        self.assertEqual(list(iterator), [])

    def test_invalid_step(self):
        with self.assertRaises(ValueError):
            StepRangeIterator(start=0, stop=10, step=-1)


class TestOrderSystem(unittest.TestCase):
    """Тестирование системы заказов: Product и Cart (Повышенная сложность №3)."""

    def setUp(self):
        self.cart = Cart()
        self.laptop = Product(product_id=1, title="Ноутбук", price=50000.0)
        self.mouse = Product(product_id=2, title="Мышь", price=1500.0)

    def test_add_and_total(self):
        self.cart.add_product(self.laptop, 1)
        self.cart.add_product(self.mouse, 2)
        # 50000 + 2 * 1500 = 53000
        self.assertEqual(self.cart.get_total_price(), 53000.0)

    def test_total_with_discount(self):
        self.cart.add_product(self.laptop, 1)
        # Скидка 10%
        self.assertEqual(self.cart.get_total_price(discount=0.10), 45000.0)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            self.cart.get_total_price(discount=1.5)

    def test_remove_product(self):
        self.cart.add_product(self.laptop, 1)
        self.cart.add_product(self.mouse, 1)
        self.cart.remove_product(self.mouse)
        self.assertNotIn(self.mouse, self.cart.items)
        self.assertEqual(self.cart.get_total_price(), 50000.0)

    def test_clear_cart(self):
        self.cart.add_product(self.laptop, 1)
        self.cart.clear()
        self.assertEqual(len(self.cart.items), 0)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Product(3, "Брак", -100.0)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_product(self.laptop, quantity=0)


if __name__ == "__main__":
    unittest.main()