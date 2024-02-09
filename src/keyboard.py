from src.item import Item


class Mixin:
    _language: str = "EN"

    @property
    def language(self) -> str:
        return self._language

    def change_lang(self) -> None:
        if self._language == 'RU':
            self._language = 'EN'
        else:
            self._language = 'RU'


class Keyboard(Item, Mixin):
    pass
