import random

from core.map import Map


class Locator():
    """
    Класс для поиска чего-либо на карте
    """
    def __init__(self, _map: Map):
         self._map = _map

    def find_place(self) -> tuple:
        while True:
            x, y = random.randint(0, self._map.width-1), random.randint(0, self._map.height-1)
            if (x, y) not in self._map.get_map:
                return (x, y)

    def nearest_smth(self, 
            pos: list,
            obj_class_find: type, 
        ) -> tuple:
        xs = pos[0]
        ys = pos[1]
        positions_odjs = self._map.get_pos_objs(obj_class_find)
        min_dist = abs(xs - positions_odjs[0][0]) + abs(ys - positions_odjs[0][1])
        xmin, yxmin = positions_odjs[0][0], positions_odjs[0][1]
        for i in range(len(positions_odjs)):
            if abs(xs - positions_odjs[i][0]) + abs(ys - positions_odjs[i][1]) <= min_dist:
                xmin, yxmin = positions_odjs[i][0], positions_odjs[i][1]
        return xmin, yxmin
                    
    @staticmethod
    def get_dist(xs: int, ys: int, xf: int, yf: int) -> int:
        return (abs(xf-xs) + abs(yf-ys))*10
    
    @staticmethod
    def get_dist_list(pos_s: list, pos_f: list) -> int:
        return (abs(pos_f[0]-pos_s[0]) + abs(pos_f[1]-pos_s[1]))*10
    