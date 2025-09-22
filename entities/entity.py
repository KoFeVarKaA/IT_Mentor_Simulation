class Entity:
    """
    Класс - основа для существ. 
    Задает основные функции и параметры
    """
    symbol = ""
    def __init__(self, pos: list) -> None:
        self.pos = pos