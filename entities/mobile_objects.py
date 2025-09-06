from config import Cfg
from core.pathfinding import Pathfinding, PathfindingHerbivore
from entities.entity import Entity
from utils.helpers import GlVariables as GlV

class Creature(Entity):
    def __init__(self, 
                 pos: list, 
                 symbol: str = '', 
                 prey: list = [], 
                 eaten_prey: int = 0,
        ) -> None:
        self.pos = pos
        self.pathfinder = Pathfinding()
        self.symbol = symbol
        self.prey = prey
        self.eaten_prey = eaten_prey

    def eat_prey(self):
        pass

    def make_move(self) -> None:
        pos_food = GlV.locator.nearest_smth(self.pos[0], self.pos[1], self.prey)
        xf, yf = self.pathfinder.find_path(
            self.pos[0], self.pos[1], pos_food[0], pos_food[1]
            )
        GlV.map[self.pos[1]][self.pos[0]] = Cfg.picture_empty
        if GlV.map[yf][xf] == self.prey[0].symbol:
            self.eat_prey(xf, yf)
        GlV.map[yf][xf] = self.symbol
        return [xf, yf]

class Herbivore(Creature):
    symbol=Cfg.picture_herbivore
    def __init__(self, pos: list):
        super().__init__(
            pos=pos,
            symbol=Cfg.picture_herbivore,
            prey=GlV.grass,
        )
        self.pathfinder = PathfindingHerbivore(
            black_list = [
                Cfg.picture_rock, Cfg.picture_tree, 
                Cfg.picture_predator, Cfg.picture_herbivore,
                ]
        )

    def eat_prey(self, xf, yf):
        self.prey[0].generate(1, self.prey)
        GlV.eaten_grass += 1
        for i in range(len(self.prey)):
            if self.prey[i].pos == [xf, yf]:
                self.prey.pop(i)
                break      
    

class Predator(Creature):
    symbol=Cfg.picture_predator
    def __init__(self, pos: list):
        super().__init__(
            pos=pos, 
            symbol=Cfg.picture_predator,
            prey=GlV.herbivores,
        )
        self.pathfinder = Pathfinding(
            black_list = [
                Cfg.picture_rock, Cfg.picture_tree, 
                Cfg.picture_grass, Cfg.picture_predator,
                ]
        )
    
    def eat_prey(self, xf, yf):
        self.prey[0].generate(1, self.prey)
        GlV.eaten_herbivores += 1
        for i in range(len(self.prey)):
            if self.prey[i].pos == [xf, yf]:
                self.prey.pop(i)
                break  