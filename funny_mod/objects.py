
from dataclasses import dataclass
from typing import TypedDict
from config import Config as Cfg
from core.generator import Generator
from core.locator import Locator
from core.map import Map
from core.pathfinding import PathfindingHerbivore
from entities.mobile_objects import Creature
from funny_mod.helpers import FunnyStatistic


class CreatureDependencies(TypedDict):
    statistic: FunnyStatistic
    _map: Map
    locator: Locator
    generator: Generator

class FunnyCreature(Creature):
    def __init__(self,
            pos: tuple,
            dependencies: CreatureDependencies,
        ) -> None:
        super().__init__(
            pos=pos,
            pathfinder= PathfindingHerbivore(
                _map = dependencies["_map"],
                locator = dependencies["locator"],
                ),
            _map = dependencies["_map"],
            locator = dependencies["locator"],
            generator = dependencies["generator"],
        )
        self.statistic = dependencies["statistic"]
        self.is_busy = False
        self.dependencies = dependencies

    def eat_prey(self, **kwargs) -> None:
        self.generator.generate(
            1, dependencies=self.dependencies, **kwargs
            )

class Grass(FunnyCreature):
    symbol=Cfg.picture_grass
    hunter_picture=Cfg.picture_herbivore
    prey_picture=Cfg.picture_tree

    def eat_prey(self) -> None:
        super().eat_prey()
        self.statistic.eaten_tree += 1
    
    
class Tree(FunnyCreature):
    symbol=Cfg.picture_tree
    hunter_picture=Cfg.picture_grass
    prey_picture=Cfg.picture_rock

    def eat_prey(self) -> None:
        super().eat_prey()
        self.statistic.eaten_rock += 1
    

class Rock(FunnyCreature):
    symbol=Cfg.picture_rock
    hunter_picture=Cfg.picture_tree
    prey_picture=Cfg.picture_predator

    def eat_prey(self) -> None:
        super().eat_prey()
        self.statistic.eaten_predator += 1

class FunnyHerbivore(FunnyCreature):
    symbol=Cfg.picture_herbivore
    hunter_picture=Cfg.picture_predator
    prey_picture=Cfg.picture_grass

    def eat_prey(self) -> None:
        super().eat_prey()
        self.statistic.eaten_grass += 1


class FunnyPredator(FunnyCreature):
    symbol=Cfg.picture_predator
    hunter_picture=Cfg.picture_rock
    prey_picture=Cfg.picture_herbivore
    
    def eat_prey(self) -> None:
        super().eat_prey()
        self.statistic.eaten_herbivores += 1