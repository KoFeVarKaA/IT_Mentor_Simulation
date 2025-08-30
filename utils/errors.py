from config import Cfg
class Errors():
    def start_err_check():
        if (
            Cfg.count_grass + Cfg.count_rock + Cfg.count_tree
            ) > Cfg.width*Cfg.height//2:
            print("ERROR: Units should not occupy more than half of the field.")
            return False
        return True