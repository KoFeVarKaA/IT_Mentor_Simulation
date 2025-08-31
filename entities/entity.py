import random

from config import Cfg
from utils.helpers import GlVariables



class Entity:
    def __init__(self, symbol):
        self.symbol = symbol
    
    # V1
    @classmethod
    def generate(cls, count, mass: list=None):
        def find_plase():
            while True:
                x, y = random.randint(0, Cfg.width-1), random.randint(0, Cfg.height-1)
                if GlVariables.map[y][x] == Cfg.picture_empty:
                    return x, y
        for i in range(count):
            x, y = find_plase()
            GlVariables.map[y][x] = cls.symbol
            if mass != None:
                mass.append(cls(pos = [x, y]))