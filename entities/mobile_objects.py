from config import Cfg
from entities.entity import Entity


class Creature(Entity):
    def make_move():
        pass
    def find_prey():
        pass

class Herbivore(Creature):
    symbol = Cfg.picture_herbivore
    def make_move():
        pass
    


class Predator(Creature):
    symbol = Cfg.picture_predator
    def make_move():
        pass