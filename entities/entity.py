import random

from config import Cfg
from utils.helpers import GlVariables as GlV


class Entity:
    """
    Класс - основа для существ. 
    Задает основные функции и параметры
    """
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol
    
    @classmethod
    def generate(cls, count: int, mass: list=None) -> None:
        def find_plase():
            while True:
                x, y = random.randint(0, Cfg.width-1), random.randint(0, Cfg.height-1)
                if GlV.map[y][x] == Cfg.picture_empty:
                    return x, y
        for i in range(count):
            x, y = find_plase()
            GlV.map[y][x] = cls.symbol
            if mass != None:
                mass.append(cls(pos = [x, y]))