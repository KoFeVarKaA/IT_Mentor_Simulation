import os
from config import Config as Cfg


class Render():
    """
    Класс для рендера чего бы то не было
    """
    def draw_map(map: list) -> None:
        os.system('cls')
        rows = []
        for i in range(Cfg.height):
            row = ' '.join(map[i])
            rows.append(f'║   {row}    ║') 
        cnt_space = 3*Cfg.width
        drawn_map = '\n'.join(
            ["╔" + "═══" + "═"*cnt_space + "═══" + "╗"] +
            ["║" + " "*((6+cnt_space-20)//2 + (6+cnt_space-20)%2) 
            + "СИМУЛЯЦИЯ ЭКОСИСТЕМЫ" + " "*((6+cnt_space-20)//2) + "║"] +
            ["╠" + "═══" + "═"*cnt_space + "═══" + "╣"] +
                            rows +
            ["╚" + "═══" + "═"*cnt_space + "═══" + "╝"]
            )
        print(drawn_map)
