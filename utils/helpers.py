from config import Config as Cfg


class Control:
    """
    Класс отвечающий за управление симуляцией
    """
    pause = False
    delay = Cfg.delay

class Statistic:
    turn = 0
    eaten_grass = 0
    eaten_herbivores = 0

    def get_statistic(self) -> str:
        return (f"turn: {self.turn}" +
                f"{Cfg.picture_herbivore} {self.eaten_grass}" +
                f"{Cfg.count_predator} {self.eaten_herbivores}")
