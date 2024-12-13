class ElementSharipova:
    def __init__(self, name, symbol, number):
        """
        Инициализация объекта класса Element.
        Аргументы:
        - name (str): название элемента.
        - symbol (str): химический символ элемента.
        - number (int): номер элемента в таблице Менделеева.
        """
        self.name = name
        self.symbol = symbol
        self.number = number

vanadium = ElementSharipova("Ванадий", "V", 23)

print(vanadium)
