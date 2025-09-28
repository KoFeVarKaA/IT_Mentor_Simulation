from config import Config as Cfg


class FunnyStatistic:
    turn = 0
    eaten_grass = 0
    eaten_herbivores = 0
    eaten_tree = 0
    eaten_rock = 0
    eaten_predator = 0
    

    def get_statistic(self) -> str:
        return (f"turn: {self.turn}" +
                f"  {Cfg.picture_herbivore}:  {self.eaten_grass}" +
                f"  {Cfg.picture_predator}: {self.eaten_herbivores}" +
                f"  {Cfg.picture_tree}: {self.eaten_rock}" +
                f"  {Cfg.picture_rock}: {self.eaten_predator}" +
                f"  {Cfg.picture_grass}: {self.eaten_tree}" )
