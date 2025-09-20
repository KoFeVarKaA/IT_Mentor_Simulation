from entities.entity import Entity


class Map():
    def __init__(self, height: int, width: int):
        # map = {(x, y): obj}  
        self.__map = {}
        self._height = height  
        self._width = width  

    def add_object(self, object, x: int, y:int) -> None:
        self.__map[(x, y)] = object

    def get_object(self, x, y):  
        return self.__map[(x, y)]

    def is_empty(self, x, y) -> bool:  
        if (x, y) in self.__map.keys():
            return True
        return False

    def delete_object(self, x, y) -> None:  
        del self.__map[(x, y)]

    def get_map(self) -> dict:  
        return self.__map
    
    def get_obj(self, x:int, y:int) -> Entity:
        if (x, y) in self.__map.keys():
            return self.__map[(x, y)]
        return None
    
    def get_pos_obj(self, obj_class: type, num_in_row: int = 1) -> tuple:
        keys = self.__map.keys()
        i = 0
        while num_in_row != 0:
            if isinstance(self.__map[keys[i]], obj_class):
                num_in_row -= 1
            if i == len(keys):
                return None
            i += 1
        return keys[i-1]
    
    def get_pos_objs(self, obj_class: type) -> list[tuple]:
        keys = self.__map.keys()
        keys_obj = []
        for i in range(len(keys)):
            if isinstance(self.__map[keys[i]], obj_class):
                keys_obj.append(keys[i])
        return keys_obj
    
    @property
    def height(self) -> int:
        return self._height
    
    @property
    def width(self) -> int:
        return self._width