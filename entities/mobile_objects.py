from config import Cfg
from core.pathfinding import Pathfinding
from entities.entity import Entity


class Creature(Entity):
    def make_move():
        pathfinder = Pathfinding()
        pathfinder.find_path(3, 2, 0, 2)
    def find_prey():
        pass

class Herbivore(Creature):
    symbol = Cfg.picture_herbivore
    def make_move():
        pass
    


class Predator(Creature):
    symbol = Cfg.picture_predator