
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
    symbol=Cfg.picture_predator

    def __init__(self,
            pos: tuple,
            dependencies: CreatureDependencies,
            prey_class: type,
            hunter_class: type,
        ) -> None:
        super().__init__(
            pos=pos,
            prey_class = prey_class, 
            pathfinder= PathfindingHerbivore(
                _map = dependencies["_map"],
                locator = dependencies["locator"],
                prey_class=prey_class,
                hunter_class=hunter_class,
                ),
            _map = dependencies["_map"],
            locator = dependencies["locator"],
            generator = dependencies["generator"],
        )
        self.hunter_class=hunter_class
        self.statistic = dependencies["statistic"]
        self.is_busy = False
        self.dependencies = dependencies

    def eat_prey(self, **kwargs) -> None:
        self.generator.generate(
            self.prey_class, 1, dependencies=self.dependencies, **kwargs
            )

class Grass(FunnyCreature):
    symbol=Cfg.picture_grass

    def eat_prey(self) -> None:
        super().eat_prey(
            prey_class=Tree, 
            hunter_class=FunnyHerbivore,
        )
        self.statistic.eaten_tree += 1
    
    
class Tree(FunnyCreature):
    symbol = Cfg.picture_tree

    def eat_prey(self) -> None:
        super().eat_prey(
            prey_class=Rock, 
            hunter_class=Grass,
        )
        self.statistic.eaten_rock += 1
    

class Rock(FunnyCreature):
    symbol = Cfg.picture_rock

    def eat_prey(self) -> None:
        super().eat_prey(
            prey_class=FunnyPredator, 
            hunter_class=Tree,
        )
        self.statistic.eaten_predator += 1

class FunnyHerbivore(FunnyCreature):
    symbol=Cfg.picture_herbivore

    def eat_prey(self) -> None:
        super().eat_prey(
            prey_class=Grass, 
            hunter_class=FunnyPredator,
        )
        self.statistic.eaten_grass += 1


class FunnyPredator(FunnyCreature):
    symbol=Cfg.picture_predator

    def eat_prey(self) -> None:
        super().eat_prey(
            prey_class=FunnyHerbivore, 
            hunter_class=Rock,
        )
        self.statistic.eaten_predator += 1