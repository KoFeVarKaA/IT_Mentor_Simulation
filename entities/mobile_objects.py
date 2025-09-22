from config import Config as Cfg
from core.locator import Locator
from core.generator import Generator
from core.map import Map
from core.pathfinding import Pathfinding, PathfindingHerbivore, PathfindingPredator
from entities.config_entities import ConfigHerbivore
from entities.entity import Entity
from entities.static_objects import Grass, Rock, Tree
from utils.helpers import Statistic



class Creature(Entity):
    """
    Класс являющийся основой живых существ,
    определяет их базовое поведение 
    """
    def __init__(self, 
                pos: list, 
                _map: Map,
                locator: Locator,
                generator: Generator,
                prey_class: type, 
                pathfinder: Pathfinding,
        ) -> None:
        self._map = _map
        self.locator = locator
        self.generator = generator
        self.pos = pos
        self.pathfinder = Pathfinding(
            _map = _map, locator=locator,
        )
        self.prey_class = prey_class


    # "Съесть" добычу
    def eat_prey(self, xf: int, yf: int) -> None:
        self._map.get_map().pop((xf, yf))
        self.generator.generate(self.prey_class, 1)

    # Механика "занятости" добычи,
    # чтобы все охотники не охотились на одну добычу
    def get_pos_food(self) -> list:
        # Определяем свободную добычу
        free_prey = []
        for prey_pos in self._map.get_pos_objs(self.prey_class):
            if not self._map.get_map()[prey_pos].is_busy:
                free_prey.append(prey_pos)

        # Если вся добыча уже занята
        if len(free_prey) == 0:
            return self.locator.nearest_smth(self.pos, self.prey_class)

        # Вычисляем ближайшую из свободных
        nearest_prey = free_prey[0]
        min_dist = self.locator.get_dist_list(self.pos, list(nearest_prey))
        for prey_pos in free_prey:
            cur_dist = self.locator.get_dist_list(self.pos, list(nearest_prey))
            if cur_dist < min_dist:
                min_dist = self.locator.get_dist_list(prey_pos, list(nearest_prey))
                nearest_prey = prey_pos
        
        return nearest_prey
    
    def make_move(self) -> None:
        pos_food = self.get_pos_food()
        xf, yf = self.pathfinder.find_path(
            self.pos[0], self.pos[1], pos_food[0], pos_food[1]
            )
        if (xf, yf) in self._map.get_map().keys():
            if isinstance(self._map.get_map()[(xf, yf)], self.prey_class):
                self.eat_prey(xf, yf)
        self._map.get_map()[(xf, yf)] = self._map.get_map()[self.pos]
        self._map.get_map().pop(self.pos)
        self.pos = (xf, yf)


class Herbivore(Creature):
    symbol=Cfg.picture_herbivore
    def __init__(self,
            pos: list,
            statistic: Statistic,
            _map: Map,
            locator: Locator,
            generator: Generator,
        ) -> None:
        super().__init__(
            pos=pos,
            prey_class = Grass, 
            pathfinder = PathfindingHerbivore(
                _map = _map,
                locator = locator,
                black_list = [
                        Cfg.picture_rock, Cfg.picture_tree, 
                        Cfg.picture_predator, Cfg.picture_herbivore,
                    ]
                ),
            _map = _map,
            locator = locator,
            generator = generator,
        )
        self.statistic = statistic
        self.is_busy = False

    def eat_prey(self, xf: int, yf: int) -> None:
        super().eat_prey(xf, yf)
        self.statistic.eaten_grass += 1 
    
    def unbusy_unit(self) -> None:
        self.is_busy = False
                

class Predator(Creature):
    symbol=Cfg.picture_predator
    def __init__(self,
            pos: list,
            statistic: Statistic,
            _map: Map,
            locator: Locator,
            generator: Generator,
        ) -> None:
        super().__init__(
            pos=pos,
            prey_class = Herbivore, 
            pathfinder=PathfindingPredator(
                _map = _map,
                locator = locator,
                black_list = [
                    Cfg.picture_rock, Cfg.picture_tree, 
                    Cfg.picture_grass, Cfg.picture_predator,
                    ]
                ),
            _map = _map,
            locator = locator,
            generator = generator,
        )
        self.statistic = statistic

    def eat_prey(self, xf: int, yf: int) -> None:
        super().eat_prey(xf, yf)
        self.statistic.eaten_herbivores += 1
    