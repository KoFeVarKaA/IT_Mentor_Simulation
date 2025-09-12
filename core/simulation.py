import time

from config import Cfg
from core.map import Map
from core.render import Render
from entities.mobile_objects import Herbivore, Predator
from entities.static_objects import Grass, Rock, Tree
from utils.errors import Errors
from utils.helpers import GlVariables as GlV
from utils.logger import Statistics


class Similation():
    """
    Класс отвечающий за порядок действий 
    и в дальнейшем для действий, 
    связанных с симуляцией (паузы, например)
    """
    def init_actions() -> None:
        Grass.generate(Cfg.count_grass, Map.grass)
        Rock.generate(Cfg.count_rock)
        Tree.generate(Cfg.count_tree)
        Herbivore.generate(Cfg.count_herbivore, Map.herbivores)
        Predator.generate(Cfg.count_predator, Map.predators)

    def next_turn() -> None:
        GlV.turn += 1
        time.sleep(GlV.delay)
        # Каждое существо делает ход
        for i in range(len(Map.herbivores)):
            Map.herbivores[i].pos = Map.herbivores[i].make_move()
        for i in range(len(Map.predators)):
            Map.predators[i].pos = Map.predators[i].make_move()

        # Добыча сбрасывает состояние
        for i in range(len(Map.herbivores)):
            Map.herbivores[i].unbusy_unit()
        for i in range(len(Map.herbivores)):
            Map.herbivores[i].unbusy_unit()
        Render.draw_map(GlV.map)
        print(Statistics.info())

    def start_simulation() -> None:
        if Errors.start_err_check():
            Similation.init_actions()
            while True:
                Similation.next_turn()
    