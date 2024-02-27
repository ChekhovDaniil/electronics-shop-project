import pytest

from src.item import Item, InstantiateCSVError

data = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    """Проверяет правильность выполнения метода, который подсчитывает total price"""
    assert data.calculate_total_price() == 200000
    assert data.quantity == 20


def test_apply_discount():
    """Проверяет правильность выполнения метода, который подсчитвает установленную скидку для конкретного товара"""
    data.pay_rate = 0.8
    data.apply_discount()
    assert data.price == 8000.0


def test_name():
    """Тест сеттера сокращающего длину имени до 10(и) символов."""
    data.name = "Abrakadabra"
    assert len(data.name) == 10


def test_unbroken_instantiate_from_csv():
    """Тестирование несломленного метода instantiate_from_csv."""
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_broken_instantiate_from_csv():
    """Тестирование сломленного метода instantiate_from_csv."""
    # Если файл items.csv отсутствует.
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()
    # Если файл item.csv поврежден
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()


def test_string_to_number():
    """
    Проверка метода преоброзвания строки в число
    """
    assert data.string_to_number("200") == 200


def test__repr__():
    """
    Тест правуильного вывода информации для разработчика
    """
    assert data.__repr__() == "Item('Abrakadabr', 8000.0, 20)"


def test__str__():
    """
    Тест правуильного вывода информации для пользователя
    """
    assert data.__str__() == 'Abrakadabr'
