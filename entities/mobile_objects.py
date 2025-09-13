from config import Config as Cfg
from core.map import Map
from core.pathfinding import Pathfinding, PathfindingHerbivore, PathfindingPredator
from entities.entity import Entity
from utils.helpers import GlVariables as GlV


class Creature(Entity):
    """
    Класс являющийся основой живых существ,
    определяет их базовое поведение 
    """
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

    def make_move(self) -> None:
        pos_food = self.get_pos_food()
        xf, yf = self.pathfinder.find_path(
            self.pos[0], self.pos[1], pos_food[0], pos_food[1]
            )
        GlV.map[self.pos[1]][self.pos[0]] = Cfg.picture_empty
        if GlV.map[yf][xf] == self.prey[0].symbol:
            self.eat_prey(xf, yf)
        GlV.map[yf][xf] = self.symbol
        return [xf, yf]

    # "Съесть" добычу
    def eat_prey(self, xf: int, yf: int) -> None:
        self.prey[0].generate(1, self.prey)
        for i in range(len(self.prey)):
            if self.prey[i].pos == [xf, yf]:
                self.prey.pop(i)
                break 

    # Механика "занятости" добычи,
    # чтобы все охотники не охотились на одну добычу
    def get_pos_food(self) -> list:
        free_prey = []
        for i in range(len(self.prey)):
            if not self.prey[i].is_busy:
                free_prey.append(self.prey[i])
        if len(free_prey) > 0:
            pos_prey = GlV.locator.nearest_smth(self.pos[0], self.pos[1], free_prey)
        else:
            pos_prey = GlV.locator.nearest_smth(self.pos[0], self.pos[1], self.prey)
        
        for i in range(len(self.prey)):
            if self.prey[i].pos[0] == pos_prey[0] and self.prey[i].pos[1] == pos_prey[1]:
                self.prey[i].is_busy = True
                break
        return pos_prey


class Herbivore(Creature):
    symbol=Cfg.picture_herbivore
    def __init__(self, pos: list) -> None:
        super().__init__(
            pos=pos,
            symbol=Cfg.picture_herbivore,
            prey=Map.grass,
        )
        self.pathfinder = PathfindingHerbivore(
            black_list = [
                Cfg.picture_rock, Cfg.picture_tree, 
                Cfg.picture_predator, Cfg.picture_herbivore,
                ]
        )
        self.is_busy = False

    def eat_prey(self, xf: int, yf: int) -> None:
        super().eat_prey(xf, yf)
        GlV.eaten_grass += 1 
    
    def unbusy_unit(self) -> None:
        self.is_busy = False
                

class Predator(Creature):
    symbol=Cfg.picture_predator
    def __init__(self, pos: list) -> None:
        super().__init__(
            pos=pos, 
            symbol=Cfg.picture_predator,
            prey=Map.herbivores,
        )
        self.pathfinder = PathfindingPredator(
            black_list = [
                Cfg.picture_rock, Cfg.picture_tree, 
                Cfg.picture_grass, Cfg.picture_predator,
                ]
        )

    def eat_prey(self, xf: int, yf: int) -> None:
        super().eat_prey(xf, yf)
        GlV.eaten_herbivores += 1
    