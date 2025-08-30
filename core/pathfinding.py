import random
from config import Cfg
from utils.errors import Errors
from utils.helpers import GlVariables


class Pathfinding():
    # test_map = [
    # [' .', ' .', ' .', ' .'],  
    # [' .', '⚫', ' .', ' .'],    
    # ['🐇', '⚫', ' .', '🐺'],
    # [' .', '⚫', ' .', ' .'],
    # [' .', ' .', ' .', ' .'] 
    # ]
    def __init__(
            self,
            black_list = [Cfg.picture_rock, Cfg.picture_tree,],
            map = GlVariables.test_map,
            ch_step = {},
            trase = [] 
    ):
        self.black_list = black_list
        self.map = map
        self.ch_step = ch_step
        self.trase = trase

    def get_dist(self, xs, ys, xf, yf):
        return (abs(xf-xs) + abs(yf-ys))*10


    def get_av_step(self, xs, ys, xf, yf):
        av_step = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                xstep = xs + x
                ystep = ys + y
                if 0 <= xstep < Cfg.width and 0 <= ystep < Cfg.height :
                    name = str(xstep)+':'+str(ystep)
                    if self.map[ystep][xstep] not in self.black_list:
                        if name not in self.ch_step.keys(): 
                            if abs(x) == abs(y):
                                ln = self.ch_step[str(xs)+':'+str(ys)][2] + 14
                            else:
                                ln = self.ch_step[str(xs)+':'+str(ys)][2] +10
                            dist = self.get_dist(xstep, ystep, xf, yf)
                            self.ch_step[name] = [xs, ys, ln, dist, ln+dist]
                            av_step.append([name, ln+dist])
                        elif name not in self.trase:
                            av_step.append([name, self.ch_step[name][4]])
        return av_step


    def next_step(self, xs, ys, xf, yf):
        av_step = self.get_av_step(xs, ys, xf, yf)
        if len(av_step) == 0:
            Errors.path_error()
            return
        var_step = []
        min_weight = min(av_step,  key=lambda x: x[1])[1]
        for i in range(0, len(av_step)):
            if av_step[i][1] == min_weight:
                var_step.append(av_step[i][0])
        return random.sample(var_step, 1)[0]

    def find_path(self, xs, ys, xf, yf):
        start_pos = str(xs)+':'+str(ys)
        self.ch_step = {
            start_pos: [0, 0, 0, self.get_dist(xs, ys, xf, yf), 999]
            }
        self.trase = [start_pos]
        pos_name = start_pos
        pos = pos_name.split(":")
        while pos_name != str(xf)+':'+str(yf):
            pos_name = self.next_step(int(pos[0]), int(pos[1]), xf, yf)
            self.trase.append(pos_name)
            pos = pos_name.split(":")      
        # Делаем шаг назад, пока не узнаем конечную точку
        xn, yn = self.trase[1].split(":")[0],  xn, yn = pos_name.split(":")[0], pos_name.split(":")[1].split(":")[1]    
        # возвращаем следующий ход
        return xn, yn
        





    """ 
    ch_step - проверенные ходы, подробнее:
    {“x:y”:
    [
    Откуда пришла x
    Откуда пришла y
    Длина пути из стартовой точки
    Пр. расстояние до яч
    Вес
    ]
    }
    """