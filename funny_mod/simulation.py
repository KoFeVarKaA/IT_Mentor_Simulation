import os
import time
from config import Config as Cfg
from core.simulation import Simulation
from funny_mod.objects import CreatureDependencies, FunnyHerbivore, FunnyPredator, Grass, Rock, Tree
from utils.helpers import Control


class FunnySimulation(Simulation):
    def init_actions(self):
        clases = [Tree, Rock, FunnyPredator, FunnyHerbivore, Grass]
        counts = [Cfg.count_tree, Cfg.count_rock, Cfg.count_predator, 
                  Cfg.count_herbivore, Cfg.count_grass]
        dependencies : CreatureDependencies = {
            'statistic': self.statistic,
            '_map': self._map,
            'locator': self.locator,
            'generator': self.generator,
        } 
        # prey_class и hunter_class
        other = [
            [Rock, Grass],
            [FunnyPredator, Tree],
            [FunnyHerbivore, Rock],
            [Grass, FunnyPredator],
            [Tree, FunnyHerbivore],
        ]
        for i in range(len(clases)):
            self.generator.generate(
                object=clases[i], count=counts[i],
                dependencies=dependencies,
                prey_class=other[i][0], 
                hunter_class=other[i][1],)
        
        self.render.draw_map(self._map)
        print(self.statistic.get_statistic())

    def next_turn(self):
        self.statistic.turn += 1
        time.sleep(Control.delay)
        # Каждое существо делает ход
        for entt_pos in self._map.get_pos_objs(Grass):
            self._map.get_map[entt_pos].make_move()
        for entt_pos in self._map.get_pos_objs(FunnyHerbivore):
            self._map.get_map[entt_pos].make_move()
        for entt_pos in self._map.get_pos_objs(FunnyPredator):
            self._map.get_map[entt_pos].make_move()
        for entt_pos in self._map.get_pos_objs(Rock):
            self._map.get_map[entt_pos].make_move()
        for entt_pos in self._map.get_pos_objs(Tree):
            self._map.get_map[entt_pos].make_move()
            
        # Добыча сбрасывает состояние
        for key in self._map.get_map.keys():
            self._map.get_map[key].unbusy_unit()

        self.render.draw_map(self._map)
        print(self.statistic.get_statistic())