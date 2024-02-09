from src.item import Item


class Mixin:
    # Класс-миксин, имеющий функционал для работы в классе Keyboard
    _language: str = "EN"

    @property
    def language(self) -> str:
        return self._language

    def change_lang(self) -> None:
        """Меняет язык раскладки клавиатуры"""
        if self._language == 'RU':
            self._language = 'EN'
        else:
            self._language = 'RU'


class Keyboard(Item, Mixin):
    # Класс наследует функционал классов Item и Mixin
    pass

