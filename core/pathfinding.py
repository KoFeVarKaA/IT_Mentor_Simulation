import random
from config import Cfg
from utils.errors import Errors
from utils.helpers import GlVariables as GlV


class Pathfinding():
     
    def __init__(
            self,
            black_list = [Cfg.picture_rock, Cfg.picture_tree,],
            ch_step = {},
            blocked_pos = [] 
    ):
        self.black_list = black_list
        self.ch_step = ch_step
        self.blocked_pos = blocked_pos

    def get_weight(self, weight_mass: list, xs, ys) -> int:
        return sum(weight_mass)

    def get_av_step(self, xs, ys, xf, yf):
        av_step = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                xstep = xs + x
                ystep = ys + y
                if 0 <= xstep < Cfg.width and 0 <= ystep < Cfg.height :
                    name = str(xstep)+':'+str(ystep)
                    if GlV.map[ystep][xstep] not in self.black_list:
                        if name not in self.blocked_pos: 
                            if abs(x) == abs(y):
                                ln = self.ch_step[str(xs)+':'+str(ys)][2] + 14
                            else:
                                ln = self.ch_step[str(xs)+':'+str(ys)][2] +10
                            dist = GlV.locator.get_dist(xstep, ystep, xf, yf)
                            weight = self.get_weight([ln, dist], xs, ys)
                            if name in self.ch_step.keys():
                                if weight < self.ch_step[name][4]:
                                     self.ch_step[name] = [xs, ys, ln, dist, weight]
                            else:
                                self.ch_step[name] = [xs, ys, ln, dist, weight]
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
            start_pos: [0, 0, 0, GlV.locator.get_dist(xs, ys, xf, yf), 999]
            }
        self.blocked_pos = [start_pos]
        pos_name = start_pos
        pos = pos_name.split(":")
        while pos_name != str(xf)+':'+str(yf):
            pos_name = self.next_step(int(pos[0]), int(pos[1]), xf, yf)
            if pos_name == None:
                pos_name = str(xf)+':'+str(yf)
            self.blocked_pos.append(pos_name)
            pos = pos_name.split(":")

        while pos_name != start_pos:
            nxt_name = str(self.ch_step[pos_name][0]) + ":" + str(self.ch_step[pos_name][1])
            if nxt_name == start_pos:
                xn, yn = int(pos_name.split(":")[0]), int(pos_name.split(":")[1])
            pos_name = nxt_name   
        return xn, yn
        

class PathfindingHerbivore(Pathfinding):    
    def dist_to_pred(self, xs, ys):
        xf, yf = GlV.locator.nearest_smth(xs, ys, GlV.predators)
        return GlV.locator.get_dist(xs, ys, xf, yf)

    def get_weight(self, weight_mass: list, xs, ys) -> int:
        return sum(weight_mass) - self.dist_to_pred(xs, ys)