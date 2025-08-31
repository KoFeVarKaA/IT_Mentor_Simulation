from config import Cfg
from core.map import Map
from entities.mobile_objects import Herbivore, Predator
from entities.static_objects import Grass, Rock, Tree
from utils.errors import Errors
from utils.helpers import GlVariables as GlV

class Similation():
    
    def init_actions():
        Grass.generate(Cfg.count_grass, GlV.grass)
        Rock.generate(Cfg.count_rock)
        Tree.generate(Cfg.count_tree)
        Herbivore.generate(Cfg.count_herbivore, GlV.herbivores)
        Predator.generate(Cfg.count_predator, GlV.predators)

    def start_simulation():
        if Errors.start_err_check():
            Similation.init_actions()
            Map.draw_map(GlV.map)
            Similation.next_turn()
            # while True:
            #     Similation.next_turn()
    
    def next_turn():
        for i in range(len(GlV.herbivores)):
            GlV.herbivores[i].make_move()
        for i in range(len(GlV.predators)):
            GlV.predators[i].make_move()
        Map.draw_map(GlV.map)
      
    def restart_simulation():
        print("Restart_simulation? Y/N")
        if input().lower() == "y":
            Similation.start_simulation()

    def simulation_actions(inp):
        if inp == 'p' and GlV == False:
            pass
        elif inp == 'p' and GlV == True:
            pass
        return