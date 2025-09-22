import os
from config import Config as Cfg
from core.map import Map


class Render():
    """
    Класс для рендера чего бы то не было
    """
    def draw_map(__map: Map) -> None:
        # os.system('cls')
        map_list = []
        for i in range(Cfg.height):
            map_list.append([])
            for j in range(Cfg.width):
                map_list[i].append(Cfg.picture_empty)

        for key in __map.get_map().keys():
            map_list[key[1]][key[0]] = __map.get_map()[key].symbol
            
        cnt_space = 3*__map.width
        total_width = 6 + cnt_space
        drawn_map = '\n'.join([
            f'╔{"═" * total_width}╗',
            f'║{"СИМУЛЯЦИЯ ЭКОСИСТЕМЫ".center(total_width)}║',
            f'╠{"═" * total_width}╣',
            *[f'║   {" ".join(map_list[i])}    ║' for i in range(Cfg.height)],
            f'╚{"═" * total_width}╝'
        ])
        print(drawn_map)
