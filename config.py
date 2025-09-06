class Cfg():
    """
    Настройки симуляции.
    Количество юнитов ограничено 50% от размера карты
    """
    # Карта 
    # max 32x32; min 5x5
    width = 32   # x
    height = 32 # y

    # Количество юнитов
    count_grass = 5
    count_tree = 102
    count_rock = 102
    count_herbivore = 3
    count_predator = 3

    # Картинка для юнитов (только смайлики или текст размером в 2 пробела)
    picture_empty = ' .'
    picture_grass = '🌱'
    picture_tree = '🌲'
    picture_rock = '⚫'
    picture_herbivore  = '🐇'
    picture_predator = '🐺'

    # Остальное
    delay = 1 # Задержка между ходами