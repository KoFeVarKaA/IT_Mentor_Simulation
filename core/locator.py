import random

from core.map import Map


class Locator():
    """
    Класс для поиска чего-либо на карте
    """
    def __init__(self, __map: Map):
         self.__map = __map

    def find_place(self) -> tuple:
        while True:
                x, y = random.randint(0, self.__map.width-1), random.randint(0, self.__map.height-1)
                if (x, y) not in self.__map.get_map().items():
                    return (x, y)
 
    def nearest_smth(self, 
            xs: int, 
            ys: int,
            obj_class_find: type, 
        ) -> tuple:
        positions_odj = self.__map.get_pos_objs(obj_class_find)
        min_dist = abs(xs - positions_odj[0][0]) + abs(ys - positions_odj[0][0])
        xmin, yxmin = None, None
        for i in range(len(positions_odj)):
            if abs(xs - positions_odj[i][0]) + abs(ys - positions_odj[i][1]) <= min_dist:
                xmin, yxmin = positions_odj[i][0], positions_odj[i][1]
        return xmin, yxmin
                    
    @staticmethod
    def get_dist(xs: int, ys: int, xf: int, yf: int) -> int:
        return (abs(xf-xs) + abs(yf-ys))*10
    