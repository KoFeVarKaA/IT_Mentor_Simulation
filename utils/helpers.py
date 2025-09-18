from config import Config as Cfg
from core.locator import Locator
from core.map import Map


class GlVariables:
    """
    Класс содержащий глобальные переменные, 
    которые изменяются по ходу исполнения программы.
    Создан для удобства и уменьшения количества импортов
    """
    map = Map(Cfg.height, Cfg.width)
    locator = Locator(map)

    pause = False
    delay = Cfg.delay

    turn = 0
    eaten_grass = 0
    eaten_herbivores = 0

class Statistic:
    turn = 0
    eaten_grass = 0
    eaten_herbivores = 0
