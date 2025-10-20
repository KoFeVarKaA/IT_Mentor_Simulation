class Entity:
    """
    Класс - основа для существ. 
    Задает основные функции и параметры
    """
    symbol = ""
    prey_picture = ""
    hunter_picture = ""
    def __init__(self, pos: list) -> None:
        self.pos = pos