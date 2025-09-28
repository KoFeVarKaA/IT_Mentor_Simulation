from config import Config as Cfg
from core.render import Render
from core.simulation import Simulation
from core.generator import Generator
from core.locator import Locator
from core.map import Map
from funny_mod.helpers import FunnyStatistic
from funny_mod.simulation import FunnySimulation
from tests.hiden_tests import HidenTests
from utils.errors import Errors
from utils.helpers import Statistic

map = Map(Cfg.height, Cfg.width)
locator = Locator(map)
render = Render()
errors = Errors()
generator = Generator(map, locator)
if Cfg.funny_mode == True:
    statistic = FunnyStatistic()
    simulation = FunnySimulation(
        statistic, map, locator, generator, render, errors
        )
else:
    statistic = Statistic()
    simulation = Simulation(
        statistic, map, locator, generator, render, errors
        )

# HidenTests.test2()
if __name__ == "__main__":
    simulation.start_simulation()