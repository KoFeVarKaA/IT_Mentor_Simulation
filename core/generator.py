from core.locator import Locator
from core.map import Map


class Generator:
    def __init__(self, _map: Map, locator: Locator):
        self._map = _map
        self.locator = locator
    
    def generate(self, object:type, count: int, **kwargs) -> None:
        for i in range(count):
            x, y = self.locator.find_place()
            self._map.add_object(object(pos=(x, y), **kwargs), x, y)
