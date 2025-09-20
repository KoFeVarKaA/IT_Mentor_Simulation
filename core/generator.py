from core.locator import Locator
from core.map import Map


class Generator:
    def __init__(self, __map: Map, locator: Locator):
        self.__map = __map
        self.locator = locator

    def generate(self, object:type, *args, **kwargs) -> None:
        x, y = self.locator.find_place()
        self.__map.get_map()[(x, y)] = object(*args, pos=[x, y], **kwargs)
