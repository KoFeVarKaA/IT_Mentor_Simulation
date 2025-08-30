from random import shuffle
from config import Cfg
from core.map import Map

class GlVariables():
    map = Map.create_map()
    pause = False

    test_map = [
    [' .', ' .', ' .', ' .'],  
    [' .', '⚫', ' .', ' .'],    
    ['🐇', '⚫', ' .', '🐺'],
    [' .', '⚫', ' .', ' .'],
    [' .', ' .', ' .', ' .'] 
    ]
    # map = test_map