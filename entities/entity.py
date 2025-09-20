class Entity:
    """
    Класс - основа для существ. 
    Задает основные функции и параметры
    """
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol