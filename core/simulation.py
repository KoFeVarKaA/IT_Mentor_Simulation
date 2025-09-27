import time
from config import Config as Cfg
from core.generator import Generator
from core.locator import Locator
from core.map import Map
from core.render import Render
from entities.config_entities import ConfigHerbivore, ConfigPredator
from entities.mobile_objects import Herbivore, Predator
from entities.static_objects import Grass, Rock, Tree
from utils.errors import Errors
from utils.helpers import Control, Statistic

class Simulation:
    def __init__(self, 
            statistic: Statistic,
            _map: Map, 
            locator: Locator, 
            generator: Generator,
            render: Render,
            errors: Errors,
    ) -> None:
        self.statistic = statistic
        self._map = _map 
        self.locator = locator
        self.generator = generator
        self.render = render
        self.errors = errors
    
    def init_actions(self):
        self.generator.generate(object=Rock, count=Cfg.count_rock)
        self.generator.generate(object=Tree, count=Cfg.count_tree)
        self.generator.generate(object=Grass, count=Cfg.count_grass)
        self.generator.generate(
            object=Herbivore, count=Cfg.count_herbivore,
            statistic=self.statistic,
            _map = self._map,
            locator = self.locator,
            generator = self.generator)
        self.generator.generate(
            object=Predator, count=Cfg.count_predator,
            statistic=self.statistic,
            _map = self._map,
            locator = self.locator,
            generator = self.generator,)
        self.render.draw_map(self._map)
        print(self.statistic.get_statistic())
    
    def next_turn(self):
        self.statistic.turn += 1
        time.sleep(Control.delay)
        # Каждое существо делает ход
        for herb_pos in self._map.get_pos_objs(Herbivore):
            self._map.get_map[herb_pos].make_move()
        for herb_pos in self._map.get_pos_objs(Predator):
            self._map.get_map[herb_pos].make_move()
            
        # Добыча сбрасывает состояние
        for key in self._map.get_map.keys():
            if isinstance(self._map.get_map[key], Herbivore):
                self._map.get_map[key].unbusy_unit()
        for key in self._map.get_map.keys():
            if isinstance(self._map.get_map[key], Grass):
                self._map.get_map[key].unbusy_unit()

        self.render.draw_map(self._map)
        print(self.statistic.get_statistic())

    def start_simulation(self):
        if self.errors.start_err_check():
            self.init_actions()
            while True:
                self.next_turn()