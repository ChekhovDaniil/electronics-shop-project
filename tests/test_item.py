from src.item import Item

data = Item("Смартфон", 10000, 20)


class Tests:
    def test_calculate_total_price(self):
        """Проверяет правильность выполнения метода, который подсчитывает total price"""
        assert data.calculate_total_price() == 200000
        assert data.quantity == 20

    def test_apply_discount(self):
        """Проверяет правильность выполнения метода, который подсчитвает установленную скидку для конкретного товара"""
        data.pay_rate = 0.8
        data.apply_discount()
        assert data.price == 8000.0

    def test_name(self):
        """Тест сеттера сокращающего длину имени до 10(и) символов."""
        data.name = "Abrakadabra"
        assert len(data.name) == 10

    def test_instantiate_from_csv(self):
        """
        Проверка метода инициализируеющнго экземпляры класса Item данными из файла src/items.csv
        """
        Item.instantiate_from_csv()
        assert len(Item.all) == 5

    def test_string_to_number(self):
        """
        Проверка метода преоброзвания строки в число
        """
        assert data.string_to_number("200") == 200
