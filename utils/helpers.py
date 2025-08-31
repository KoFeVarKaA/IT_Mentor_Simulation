from random import shuffle
from config import Cfg
from core.locator import Locator
from core.map import Map

class GlVariables():
    map = Map.create_map()
    locator = Locator()
    pause = False

    test_map = [
    [' .', ' .', ' .', ' .'],  
    [' .', '⚫', ' .', ' .'],    
    ['🐇', '⚫', ' .', '🐺'],
    [' .', '⚫', ' .', ' .'],
    [' .', ' .', ' .', ' .'] 
    ]
    # map = test_map
    herbivores = []
    predators = []
    grass = []
