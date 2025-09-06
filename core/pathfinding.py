import logging
import random
from config import Cfg
from core.map import Map
from utils.errors import Errors
from utils.helpers import GlVariables as GlV


class Pathfinding():
    """
    Класс отвечающий за поиск пути (алгоритм A*). 
    Формирует основу для PathfindingHerbivore и PathfindingPredator,
    которые переделавают некоторые функции под свои нужды

    Помарки:
    xf и yf означают точку финиша
    xs и ys точку старта соотвественно
    Для каждой функции они свои

    ch_step имеет следующий вид:
    {“x:y”: 
    [x предыдущ. точки, 
    y предыдущ. точки, 
    Длина пути из стартовой точки, 
    Пр. расстояние до яч, 
    Вес(Длина + Раст до яч + Опцианально)]
    }
    """
    def __init__(
            self,
            black_list: list = [Cfg.picture_rock, Cfg.picture_tree,],
            ch_step: dict = {},
            blocked_pos: list = [], 
    ) -> None:
        self.black_list = black_list    # Объекты на которые нельзя наступать
        self.ch_step = ch_step          # Проверенные позиции (для оптимального пути и веса)
        self.blocked_pos = blocked_pos  # Пройденные позиции

    # Основная функция
    def find_path(self, xs: int, ys: int, xf: int, yf: int) -> tuple:
        # Задаем стартовую позицию и добавляем ее в ch_step и blocked_pos
        start_pos = str(xs)+':'+str(ys)
        self.ch_step = {
            start_pos: [0, 0, 0, GlV.locator.get_dist(xs, ys, xf, yf), 999]
            }
        self.blocked_pos = [start_pos]
        pos_name = start_pos        # Имя теоритической позиции
        pos = pos_name.split(":")   # Теоритическая позиция на данный момент (в виде массива)

        # Пока мы не пришли к финишной позиции
        while pos_name != str(xf)+':'+str(yf):
            pos_name = self.next_step(int(pos[0]), int(pos[1]), xf, yf)

            # В случае если юнит заблудился - стоим на месте, либо идем в сторону жертвы
            if pos_name == None:
                keys = list(self.ch_step.keys())
                if len(keys) < 2:
                    pos_name = keys[0]
                else:
                    pos_name = keys[1]
                break

            self.blocked_pos.append(pos_name)
            pos = pos_name.split(":")

        # Смотрим на пройденный путь и выбираем следующий шаг
        xn, yn = xs, ys
        while pos_name != start_pos:
            nxt_name = str(self.ch_step[pos_name][0]) + ":" + str(self.ch_step[pos_name][1])
            if nxt_name == start_pos:
                xn, yn = int(pos_name.split(":")[0]), int(pos_name.split(":")[1])
            pos_name = nxt_name   
        return xn, yn

    # Выбор следующего шага из доступных
    def next_step(self, xs: int, ys: int, xf: int, yf: int) -> tuple:
        av_step = self.get_av_step(xs, ys, xf, yf)

        # Юнит заблудился?
        if len(av_step) == 0:
            return None
        
        # Для случая, когда 2 хода имеют одинаковый вес
        var_step = [] 
        min_weight = min(av_step,  key=lambda x: x[1])[1]
        for i in range(0, len(av_step)):
            if av_step[i][1] == min_weight:
                var_step.append(av_step[i][0])
        return random.sample(var_step, 1)[0]

    # Узнать доступные шаги
    def get_av_step(self, xs: int, ys: int, xf: int, yf: int) -> list:
        av_step = []
        
        # Просмотривает область вокруг юнита
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                xstep = xs + x
                ystep = ys + y

                # Выбранный шаг не находится за границами карты?
                if 0 <= xstep < Cfg.width and 0 <= ystep < Cfg.height :
                    name = str(xstep)+':'+str(ystep)
                    # Выбранный шаг - это не объект в черном списке (см. выше)
                    if GlV.map[ystep][xstep] not in self.black_list:
                        # Юнит еще не выбирал данный шаг?
                        if name not in self.blocked_pos:
                            # Расчет параметров
                            ln = self.get_len(x, y, xs, ys)
                            dist = GlV.locator.get_dist(xstep, ystep, xf, yf)
                            weight = self.get_weight([ln, dist], xs, ys)

                            # Выбор минимального веса для хода
                            if name in self.ch_step.keys():
                                if weight < self.ch_step[name][4]:
                                     self.ch_step[name] = [xs, ys, ln, dist, weight]
                            else:
                                self.ch_step[name] = [xs, ys, ln, dist, weight]
                            
                            av_step.append([name, self.ch_step[name][4]])
        return av_step
    
    def get_weight(self, weight_mass: list, xs, ys) -> int:
        return sum(weight_mass)
    
    def get_len(self, x: int, y: int, xs: int, ys: int) -> int:
        if abs(x) == abs(y):
            return self.ch_step[str(xs)+':'+str(ys)][2] + 14
        else:
            return self.ch_step[str(xs)+':'+str(ys)][2] +10


class PathfindingPredator(Pathfinding):
    pass


class PathfindingHerbivore(Pathfinding):    
    def dist_to_pred(self, xs: int, ys: int) -> int:
        xf, yf = GlV.locator.nearest_smth(xs, ys, Map.predators)
        return GlV.locator.get_dist(xs, ys, xf, yf)

    def get_weight(self, weight_mass: list, xs: int, ys: int) -> int:
        return sum(weight_mass) - self.dist_to_pred(xs, ys)