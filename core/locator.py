


class Locator():
    def __init__(self):
        pass
    
    def get_dist(self, xs, ys, xf, yf):
        return (abs(xf-xs) + abs(yf-ys))*10

    def nearest_smth(self, 
            xs: int, 
            ys: int, 
            mass_to_find: list,
        ):
        mass = mass_to_find
        min_dist = abs(xs - mass[0].pos[0]) + abs(ys - mass[0].pos[1])
        xmin, yxmin = None, None
        for i in range(len(mass)):
            if abs(xs - mass[i].pos[0]) + abs(ys - mass[i].pos[1]) <= min_dist:
                xmin, yxmin = mass[i].pos[0], mass[i].pos[1]
        return xmin, yxmin