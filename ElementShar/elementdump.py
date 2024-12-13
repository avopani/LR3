class ElementSharipova:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        """
        Выводит на экран значения атрибутов объекта.
        """
        print(f"Название: {self.name}, Символ: {self.symbol}, Номер: {self.number}")

vanadium = ElementSharipova("Ванадий", "V", 23)

vanadium.dump()
