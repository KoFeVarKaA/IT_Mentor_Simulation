from config import Cfg

class Map():
    def create_map():
        map = []
        for i in range(Cfg.height):
            map.append([])
            for j in range(Cfg.width):
                map[i].append(Cfg.picture_empty)
        return map
    
    def draw_map(map): 
        rows = []
        for i in range(Cfg.height):
            row = ' '.join(map[i])
            rows.append(f'║   {row}    ║') 
        cnt_space = (1+Cfg.size_empty)*Cfg.width
        drawn_map = '\n'.join(
            ["╔" + "═══" + "═"*cnt_space + "═══" + "╗"] +
            ["║" + " "*((6+cnt_space-20)//2 + (6+cnt_space-20)%2) 
            + "СИМУЛЯЦИЯ ЭКОСИСТЕМЫ" + " "*((6+cnt_space-20)//2) + "║"] +
            ["╠" + "═══" + "═"*cnt_space + "═══" + "╣"] +
                            rows +
            ["╚" + "═══" + "═"*cnt_space + "═══" + "╝"]
            )
        print(drawn_map)
