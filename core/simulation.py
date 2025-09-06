import time
from config import Cfg
from core.map import Map
from entities.mobile_objects import Herbivore, Predator
from entities.static_objects import Grass, Rock, Tree
from utils.errors import Errors
from utils.helpers import GlVariables as GlV
from utils.logger import Statistics

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
            print(Statistics.info())
            Map.draw_map(GlV.map)
            # GlV.grass = [Grass(pos=[0,0]), Grass(pos=[0,5]), Grass(pos=[3,3])]
            # GlV.herbivores = [Herbivore(pos=[1,3])]
            # GlV.predators = [Predator(pos=[3,5])]
            while True:
                Similation.next_turn()

    
    def next_turn():
        GlV.turn += 1
        time.sleep(GlV.delay)
        for i in range(len(GlV.herbivores)):
            GlV.herbivores[i].pos = GlV.herbivores[i].make_move()
        for i in range(len(GlV.predators)):
            GlV.predators[i].pos = GlV.predators[i].make_move()
        print(Statistics.info())
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