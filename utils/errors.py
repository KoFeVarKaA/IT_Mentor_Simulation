from config import Config as Cfg


class Errors():
    """
    Класс для действий связанных с ошибками 
    (вывод сообщений, проверка)
    """
    @staticmethod
    def start_err_check():
        if (
            Cfg.count_grass + Cfg.count_rock + Cfg.count_tree
            ) > Cfg.width*Cfg.height//2:
            print("ERROR: Units should not occupy more than half of the field.")
            return False
        elif 5 > Cfg.width > 32 or 5 > Cfg.height > 32:
            print("""WARNING: map dimensions
maximum map dimensions - 32x32
minimum map dimensions - 5xx5
                  
Continue? y/n""")
            if input().lower() != "y":
                return False
        return True
    @staticmethod
    def path_error():
        print("ERROR: Unit has nowhere else to go")
