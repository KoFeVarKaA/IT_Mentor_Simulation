from entities.entity import Entity
from config import Cfg

class Grass(Entity):
    symbol=Cfg.picture_grass
    def __init__(self, pos: list) -> None:
        self.pos = pos

    
    
class Tree(Entity):
    symbol = Cfg.picture_tree
    

class Rock(Entity):
    symbol = Cfg.picture_rock
    