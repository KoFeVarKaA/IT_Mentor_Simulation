from config import Config as Cfg
from core.locator import Locator
from core.generator import Generator
from core.map import Map
from core.pathfinding import Pathfinding, PathfindingHerbivore, PathfindingPredator
from entities.entity import Entity
from entities.static_objects import Grass
from utils.helpers import Statistic



class Creature(Entity):
    """
    Класс являющийся основой живых существ,
    определяет их базовое поведение 
    """
    def __init__(self, 
                pos: tuple, 
                _map: Map,
                locator: Locator,
                generator: Generator,
                pathfinder: Pathfinding,
        ) -> None:
        self._map = _map
        self.locator = locator
        self.generator = generator
        self.pos = pos

    # "Съесть" добычу
    def eat_prey(self, **kwargs) -> None:
        self.generator.generate(1, **kwargs)

    # Механика "занятости" добычи,
    # чтобы все охотники не охотились на одну добычу
    def get_pos_food(self) -> tuple:
        # Просматриваем область вокруг
        # чтобы избежать ситуаций, когда охотник
        # не может съесть занятую добычу
        # Просмотривает область вокруг юнита
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue
                xstep = self.pos[0] + x
                ystep = self.pos[1] + y
                # Выбранный шаг не находится за границами карты?
                if 0 <= xstep < self._map.width and 0 <= ystep < self._map.height :
                    name = (xstep, ystep)
                    if name in self._map.get_map.keys():
                        if self._map.get_map[(xstep, ystep)].symbol == self.prey_picture:
                            return name

        # Определяем свободную добычу
        free_prey = []
        for prey_pos in self._map.get_pos_objs(obj_picture=self.prey_picture):
            if not self._map.get_map[prey_pos].is_busy:
                free_prey.append(prey_pos)

        # Если вся добыча уже занята
        if len(free_prey) == 0:
            return self.locator.nearest_smth(self.pos, self.prey_picture)

        # Вычисляем ближайшую из свободных
        nearest_prey = free_prey[0]
        min_dist = self.locator.get_dist_list(self.pos, list(nearest_prey))
        for prey_pos in free_prey:
            cur_dist = self.locator.get_dist_list(self.pos, list(prey_pos))
            if cur_dist < min_dist:
                min_dist = self.locator.get_dist_list(prey_pos, list(nearest_prey))
                nearest_prey = prey_pos
        
        return nearest_prey
    
    def make_move(self) -> None:
        pos_food = self.get_pos_food()          # Найти добычу
        self._map.get_map[pos_food].busy_unit() # Занять добычу (чтобы другие не охотились на нее)
        xf, yf = self.pathfinder.find_path(     # Ищем путь до добычи
            self.pos[0], self.pos[1], pos_food[0], pos_food[1]
            )
        # Если объект не может сходить
        if (xf, yf) == self.pos:
            return
        # Если хищник съедает добычу
        elif (xf, yf) in self._map.get_map.keys():
            if self._map.get_map[(xf, yf)].symbol == self.prey_picture:
                self.eat_prey() # Съедаем добычу
                self._map.delete_object(xf, yf)                                   # Удаляем добычу
        self._map.add_object(self._map.get_obj(self.pos[0], self.pos[1]), xf, yf) # Делаем шаг охотником
        self._map.delete_object(self.pos[0], self.pos[1])                         # Удаляем охотника со старого места
        self._map.get_obj(xf, yf).pos = (xf, yf)                                  # Меняем данные у охотника (Не в карте, а в "памяти" у сущности)

    def busy_unit(self) -> None:
        self.is_busy = True

    def unbusy_unit(self) -> None:
        self.is_busy = False


class Herbivore(Creature):
    symbol=Cfg.picture_herbivore
    hunter_picture=Cfg.picture_predator
    prey_picture=Cfg.picture_grass

    def __init__(self,
            pos: tuple,
            statistic: Statistic,
            _map: Map,
            locator: Locator,
            generator: Generator,
        ) -> None:
        super().__init__(
            pos=pos,
            pathfinder = PathfindingHerbivore(
                _map = _map,
                locator = locator,
                ),
            _map = _map,
            locator = locator,
            generator = generator,
        )
        self.statistic = statistic
        self.is_busy = False

    def eat_prey(self) -> None:
        super().eat_prey()
        self.statistic.eaten_grass += 1 

    
                

class Predator(Creature):
    symbol=Cfg.picture_predator
    prey_picture=Cfg.picture_herbivore

    def __init__(self,
            pos: tuple,
            statistic: Statistic,
            _map: Map,
            locator: Locator,
            generator: Generator,
        ) -> None:
        super().__init__(
            pos=pos,
            pathfinder=PathfindingPredator(
                _map = _map,
                locator = locator,
                ),
            _map = _map,
            locator = locator,
            generator = generator,
        )
        self.statistic = statistic
        self.is_busy = False

    def eat_prey(self,) -> None:
        super().eat_prey( 
            statistic=self.statistic,
            _map = self._map,
            locator = self.locator,
            generator = self.generator)        
        self.statistic.eaten_herbivores += 1
    