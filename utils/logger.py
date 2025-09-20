from config import Config
from core.map import Map
from utils.helpers import Statistic


class Logs:
    pass


class Statistics:
    """
    Класс для вывода базовой статистики
    """
    def __init__(self, cfg: Config, statistic: Statistic):
        self.cfg = cfg
        self.stat = statistic

    def info(self):
        info = (
            "Turn: " + str(self.stat.turn) + "  " +
            self.cfg.picture_herbivore + ": " + str(self.stat.eaten_grass) + "  " +
            self.cfg.picture_predator + ": " + str(self.stat.eaten_herbivores) + "  " 
        )
        return info