from config import width, height

class Map():
    def create_map():
        map = [[] for i in range(width)]
        for i in range(width):
            for j in range(height):
                map[i].append("0")
        return map
    
    def draw_map(map): 
        rows = []
        for i in range(width):
            row = ' '.join(map[i])
            rows.append(f'║   {row}    ║') 
        return '\n'.join(
            ["╔" + "═══" + "═"*2 *height + "═══" + "╗"] +
            ["║" + " "*((6+2*height-20)//2 + (6+2*height-20)%2) 
            + "СИМУЛЯЦИЯ ЭКОСИСТЕМЫ" + " "*((6+2*height-20)//2) + "║"] +
            ["╠" + "═══" + "═"*2*height + "═══" + "╣"] +
                            rows +
            ["╚" + "═══" + "═"*2*height + "═══" + "╝"]
            )

