from entities.entity import Entity
from config import Config as Cfg


class Grass(Entity):
    symbol=Cfg.picture_grass
    def __init__(self, pos: list) -> None:
        self.pos = pos
        self.is_busy = False

    def busy_unit(self) -> None:
        self.is_busy = True

    def unbusy_unit(self) -> None:
        self.is_busy = False
    
    
class Tree(Entity):
    symbol = Cfg.picture_tree
    

class Rock(Entity):
    symbol = Cfg.picture_rock
    