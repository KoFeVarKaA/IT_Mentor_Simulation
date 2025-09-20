from config import Config as Cfg
from core.simulation import Simulation
from core.generator import Generator
from core.locator import Locator
from core.map import Map
from tests.hiden_tests import HidenTests
from utils.helpers import Statistic

statistic = Statistic()
map = Map(Cfg.height, Cfg.width)
locator = Locator(map)
generator = Generator(map, locator)
simulation = Simulation(statistic, map, locator, generator)

HidenTests.test2()
# if __name__ == "main":
    # simulation.start_simulation()