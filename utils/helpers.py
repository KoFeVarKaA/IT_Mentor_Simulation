from config import Cfg
from core.locator import Locator
from core.map import Map

class GlVariables():
    herbivores = []
    predators = []
    grass = []
    map = Map.create_map()
    locator = Locator()

    pause = False
    delay = Cfg.delay

    turn = 0
    eaten_grass = 0
    eaten_herbivores = 0
    # test_map = [
    # ['🌱', ' .', ' .', ' .', ' .','🌱',],  
    # [' .', ' .', ' .', ' .', ' .',' .',],    
    # [' .', ' .', ' .', ' .', ' .',' .',],
    # [' .', '🐇', ' .', '🌱', ' .',' .',],
    # [' .', ' .', '⚫', ' .', ' .',' .',],
    # [' .', '⚫', '⚫', '🐺', ' .',' .',], 
    # [' .', ' .', ' .', ' .', ' .',' .',],  
    # ]
    # map = test_map