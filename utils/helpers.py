from config import Cfg
from core.locator import Locator
from core.map import Map

class GlVariables():
    # def __init__(
    #         self,
    #         herbivores: Herbivore = [],
    #         predators: Predator = [],
    #         grass: Grass = [],
    #         map: Map = Map.create_map(),
    #         locator: Locator = Locator(),
    #         pause: bool = False,
    #     ):
    #     self.herbivores = herbivores
    #     self.predators = predators
    #     self.grass = grass
    #     self.map = map
    #     self.locator = locator
    #     self.pause = pause
    test_map = [
    ['🌱', ' .', ' .', ' .', ' .','🌱',],  
    [' .', ' .', ' .', ' .', ' .',' .',],    
    [' .', ' .', ' .', ' .', ' .',' .',],
    [' .', '🐇', ' .', '🌱', ' .',' .',],
    [' .', ' .', '⚫', ' .', ' .',' .',],
    [' .', '⚫', '⚫', '🐺', ' .',' .',], 
    [' .', ' .', ' .', ' .', ' .',' .',],  
    ]
    herbivores = []
    predators = []
    grass = []
    map = Map.create_map()
    locator = Locator()

    pause = False
    delay = Cfg.delay

    # map = test_map