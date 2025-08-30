from config import Cfg
from core.map import Map
from entities.mobile_objects import Herbivore, Predator
from entities.static_objects import Grass, Rock, Tree
from utils.errors import Errors
from utils.helpers import GlVariables

class Similation():
    # map = GlVariables.maps  

    def next_turn():
        Herbivore.make_move()
        Predator.make_move()
        Map.draw_map()
    
    def start_simulation():
        if Errors.start_err_check():
            Similation.init_actions()
            # while True:
            #     Similation.next_turn()

    def pause_simulation(inp):
        if inp == 'p' and GlVariables == False:
            pass
        elif inp == 'p' and GlVariables == True:
            pass
        return
    
    def init_actions():
        Grass.generate(Cfg.count_grass)
        Rock.generate(Cfg.count_rock)
        Tree.generate(Cfg.count_tree)