from core.map import Map
from utils.helpers import GlVariables

class Similation():
    map = Map.create_map()


    def next_turn():
        pass
    
    def start_simulation():
        while True:
            Similation.next_turn()

    def pause_simulation(inp):
        if inp == 'p' and GlVariables == False:
            pass
        elif inp == 'p' and GlVariables == True:
            pass
        return