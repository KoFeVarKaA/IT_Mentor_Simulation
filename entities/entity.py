import random

from config import Cfg
from utils.helpers import GlVariables



class Entity:
    symbol = 'T'
    
    # V1
    @classmethod
    def generate(cls, count):
        def find_plase():
            while True:
                x, y = random.randint(0, Cfg.width-1), random.randint(0, Cfg.height-1)
                if GlVariables.map[x][y] == Cfg.picture_empty:
                    return x, y
        for i in range(count):
            x, y = find_plase()
            GlVariables.map[x][y] = cls.symbol