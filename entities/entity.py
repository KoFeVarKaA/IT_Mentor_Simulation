class Entity:
    """
    Класс - основа для существ. 
    Задает основные функции и параметры
    """
    def __init__(self, pos: list) -> None:
        self.pos = pos