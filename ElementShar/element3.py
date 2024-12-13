class ElementSharipova:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def dump(self):
        """
        Выводит на экран значения атрибутов объекта.
        """
        print(f"Название: {self.name}, Символ: {self.symbol}, Номер: {self.number}")

vanadium = ElementSharipova("Ванадий", "V", 23)

vanadium.dump()
