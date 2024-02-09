import pytest

from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def _language_test():
    """Тест, проверяющий корректную ошибку"""
    with pytest.raises(AttributeError):
        kb._language = 'CH'


class Tests:

    def test_language(self):
        """Проверяет начальную раскладку клаиватуры"""
        assert str(kb.language) == 'EN'

    def test_change_lang(self):
        """
        Тесты для проверки правлиьной работы метода смены языка
        """
        kb.change_lang()
        assert str(kb.language) == "RU"
        kb.change_lang()
        assert str(kb.language) == "EN"
