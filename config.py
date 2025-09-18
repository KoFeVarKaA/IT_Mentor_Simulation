class Config:
    """
    Настройки симуляции.
    """
    # Карта 
    # Максимальный размер карты 32x32, минимальный - 5x5
    width = 8   # x
    height = 8  # y

    # Количество юнитов
    # Максимальное количество юнитов - 50% от карты
    dynamic_generation = True # ДОБАВИТЬ ДИНАМИЧЕСКУЮ ГЕНЕРАЦИЮ
    count_grass = 3
    count_tree = 5
    count_rock = 5
    count_herbivore = 2
    count_predator = 2

    # Картинка для юнитов (только смайлики или текст размером в 2 пробела)
    picture_empty = ' .'
    picture_grass = '🌱'
    picture_tree = '🌲'
    picture_rock = '⚫'
    picture_herbivore = '🐇'
    picture_predator = '🐺'

    # Остальное
    delay = 1 # Задержка между ходами
