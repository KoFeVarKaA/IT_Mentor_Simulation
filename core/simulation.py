from core.generator import Generator
from entities.mobile_objects import Herbivore, Predator
from entities.static_objects import Grass, Rock, Tree
from utils.errors import Errors
from utils.helpers import Statistic

class Simulation():
    def __init__(self, statistic: Statistic):
        self.statistic = statistic
        
    @staticmethod
    def init_actions():
        Generator.generate(Rock)
        Generator.generate(Tree)
        Generator.generate(Grass)
        Generator.generate(Herbivore)
        Generator.generate(Predator)
    
    @staticmethod
    def next_turn():
        pass

    @staticmethod
    def start_simulation():
        if Errors.start_err_check():
            Simulation.init_actions()
            while True:
                Simulation.next_turn()