from config import Config as Cfg

class Map():
    """
    Класс содержащий функцию для инициализации карты
    (сама карта храниться в GlVariables), а также
    массивы объектов связанных с ней
    """
    herbivores = []
    predators = []
    grass = []

    def create_map() -> list:
        map = []
        for i in range(Cfg.height):
            map.append([])
            for j in range(Cfg.width):
                map[i].append(Cfg.picture_empty)
        return map
    