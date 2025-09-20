import random
from core.locator import Locator
from core.map import Map


class Pathfinding():
    def __init__(
            self,
            _map: Map,
            locator: Locator,
            black_list: list = [],
            hunter_class: type = None,
    ) -> None:
        self.black_list = black_list    
        self.ch_step = {}         
        self.blocked_pos = []
        self._map = _map
        self.locator = locator 
        self.hunter_class = hunter_class

    # Узнать доступные шаги
    def get_av_step(self, xs: int, ys: int, xf: int, yf: int) -> list:
        av_step = []
        
        # Просмотривает область вокруг юнита
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                xstep = xs + x
                ystep = ys + y

                # Выбранный шаг не находится за границами карты?
                if 0 <= xstep < self._map.width and 0 <= ystep < self._map.height :
                    name = (xstep, ystep)
                    # Выбранный шаг - это не объект в черном списке (см. выше)
                    if self._map.get_obj(x=xstep, y=ystep).symbol not in self.black_list:
                        # Юнит еще не выбирал данный шаг?
                        if name not in self.blocked_pos:
                            # Расчет параметров
                            ln = self.get_len(x, y, self.ch_step[(xs, ys)][2] )
                            dist = self.locator.get_dist(xstep, ystep, xf, yf)
                            weight = self.get_weight([ln, dist], xs, ys)

                            # Выбор минимального веса для хода
                            if name in self.ch_step.keys():
                                if weight < self.ch_step[name][4]:
                                     self.ch_step[name] = [xs, ys, ln, dist, weight]
                            else:
                                self.ch_step[name] = [xs, ys, ln, dist, weight]
                            
                            av_step.append([name, self.ch_step[name][4]])
        return av_step
    
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
    
    # Основная функция
    def find_path(self, xs: int, ys: int, xf: int, yf: int) -> tuple:
        # Задаем стартовую позицию и добавляем ее в ch_step и blocked_pos
        start_pos = (xs, ys)
        self.ch_step = {
            start_pos: [0, 0, 0, self.locator.get_dist(xs, ys, xf, yf), 999]
            }
        self.blocked_pos = [start_pos]
        pos = start_pos    # Теоритическая позиция на данный момент (в виде кортежа)

        # Пока мы не пришли к финишной позиции
        while pos != (xf, yf):
            pos = self.next_step(pos[0], pos[1], xf, yf)

            # В случае если юнит заблудился - стоим на месте, либо идем в сторону жертвы
            if pos == None:
                keys = list(self.ch_step.keys())
                if len(keys) < 2:
                    pos = keys[0]
                else:
                    pos = keys[1]
                break

            self.blocked_pos.append(pos)

        # Смотрим на пройденный путь и выбираем следующий шаг
        xn, yn = xs, ys
        while pos != start_pos:
            nxt_name = (self.ch_step[pos][0], self.ch_step[pos][1])
            if nxt_name == start_pos:
                xn, yn = pos
            pos = nxt_name   
        return xn, yn

    
    def get_weight(self, weight_mass: list, xs: int, ys: int) -> int:
        return sum(weight_mass)
    
    def get_len(self, x: int, y: int, start_step_len: int) -> int:
        if abs(x) == abs(y):
            return start_step_len + 14
        else:
            return start_step_len + 10


class PathfindingPredator(Pathfinding):
    pass


class PathfindingHerbivore(Pathfinding):    
    def dist_to_pred(self, xs: int, ys: int) -> int:
        xf, yf = self.locator.nearest_smth([xs, ys], self.hunter_class)
        return self.locator.get_dist(xs, ys, xf, yf)

    def get_weight(self, weight_mass: list, xs: int, ys: int) -> int:
        return sum(weight_mass) - self.dist_to_pred(xs, ys)
    