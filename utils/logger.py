from config import Cfg
from utils.helpers import GlVariables as GlV
class Logs():
    """
    В дальнейшем планируется добавить расширенные логи
    """
    pass

class Statistics():
    """
    Класс для вывода базовой статистики
    """
    def info():
        info = (
            "Turn: " + str(GlV.turn) + "  " +
            Cfg.picture_herbivore + ": " + str(GlV.eaten_grass) + "  " +
            Cfg.picture_predator + ": " + str(GlV.eaten_herbivores) + "  " 
        )
        return info