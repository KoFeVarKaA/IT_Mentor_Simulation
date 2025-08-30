from config import Cfg
from utils.helpers import GlVariables


class Pathfinding():
    # test_map = [
    # [' .', ' .', ' .', ' .'],  
    # [' .', '⚫', ' .', ' .'],    
    # ['🐇', '⚫', ' .', '🐺'],
    # [' .', '⚫', ' .', ' .'],
    # [' .', ' .', ' .', ' .'] 
    # ]
    black_list = [Cfg.picture_rock, Cfg.picture_tree]
    map = GlVariables.test_map
    ch_step = {}
    def get_dist(self, xs, ys, xf, yf):
        return xf-xs + ys-yf


    def get_av_step(self, xs, ys, xf, yf):
        av_step = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                xstep = xs + x
                ystep = ys + y
                if xstep >= 0 and ystep >= 0:
                    name = str(xstep)+':'+str(ystep)
                    if (
                        name not in self.ch_step.items() 
                        and 
                        self.map[xstep][ystep] not in self.black_list):
                        if abs(x) == abs(y):
                            ln = self.ch_step[str(xs)+':'+str(ys)][2] + 14
                        else:
                            ln = self.ch_step[str(xs)+':'+str(ys)][2] +10
                        dist = self.get_dist(xstep, ystep, xf, yf)
                        self.ch_step[name] = [xs, ys, ln, dist, ln+dist]
                        av_step.append(name)
        return av_step


    def next_step(self, xs, ys, xf, yf):
        av_step = self.get_av_step(xs, ys)
        for i in av_step:
            pass

    def find_path(self, xs, ys, xf, yf):
        self.ch_step = {
            str(xs)+':'+str(ys): [0, 0, 0, self.get_dist(xs, ys, xf, yf)]
            }
        is_end = False
        while is_end == False:
            is_end = self.next_step()
        name =''
        # Делаем шаг назад, пока не узнаем конечную точку
        while name != '0:0':
            nxt_name = self.ch_step[name][0] + ":" + self.ch_step[name][0]
            if nxt_name == "0:0":
                xn, yn = name.split(":")[0], name.split(":")[2]
            
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