import time
from core.generator import Generator
from core.locator import Locator
from core.map import Map
from core.render import Render
from entities.mobile_objects import Herbivore, Predator
from entities.static_objects import Grass, Rock, Tree
from utils.errors import Errors
from utils.helpers import Control, Statistic

class Simulation:
    def __init__(self, 
            statistic: Statistic,
            __map: Map, 
            locator: Locator, 
            generator: Generator,
    ) -> None:
        self.statistic = statistic
        self.__map = __map 
        self.locator = locator
        self.generator = generator
    
    @staticmethod
    def init_actions():
        Generator.generate(Rock)
        Generator.generate(Tree)
        Generator.generate(Grass)
        Generator.generate(Herbivore)
        Generator.generate(Predator)
    
    def next_turn(self):
        self.statistic.turn += 1
        time.sleep(Control.delay)
        # Каждое существо делает ход
        for key in self.__map.get_map().keys():
            if isinstance(self.__map[key], Herbivore):
                self.__map[key].make_move()
        for key in self.__map.get_map().keys():
            if isinstance(self.__map[key], Predator):
                self.__map[key].make_move()
            
        # Добыча сбрасывает состояние
        for key in self.__map.get_map().keys():
            if isinstance(self.__map[key], Herbivore):
                self.__map[key].unbusy_unit()
        for key in self.__map.get_map().keys():
            if isinstance(self.__map[key], Grass):
                self.__map[key].unbusy_unit()

        Render.draw_map(self.__map)
        print(self.statistic.get_statistic())

        

    @staticmethod
    def start_simulation():
        if Errors.start_err_check():
            Simulation.init_actions()
            while True:
                Simulation.next_turn()