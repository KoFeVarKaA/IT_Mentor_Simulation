from config import Cfg

class Map():
    def create_map():
        map = []
        for i in range(Cfg.width):
            map.append([])
            for j in range(Cfg.height):
                map[i].append(" .")
        return map
    
    def draw_map(map): 
        rows = []
        for i in range(Cfg.width):
            row = ' '.join(map[i])
            rows.append(f'║   {row}    ║') 
        return '\n'.join(
            ["╔" + "═══" + "═"*3 *Cfg.height + "═══" + "╗"] +
            ["║" + " "*((6+3*Cfg.height-20)//2 + (6+3*Cfg.height-20)%2) 
            + "СИМУЛЯЦИЯ ЭКОСИСТЕМЫ" + " "*((6+3*Cfg.height-20)//2) + "║"] +
            ["╠" + "═══" + "═"*3*Cfg.height + "═══" + "╣"] +
                            rows +
            ["╚" + "═══" + "═"*3*Cfg.height + "═══" + "╝"]
            )

