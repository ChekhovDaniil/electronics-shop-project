class InstantiateCSVError(KeyError):
    """Вызывает исключение при ошибке KeyError"""

    def __str__(self):
        return 'Файл item.csv поврежден'
