class Cfg():
    # map 
    # max 256x256; min 5x5
    width = 6   # x
    height = 6  # y

    # count_unit
    count_grass = 2
    count_tree = 2
    count_rock = 2
    count_herbivore = 1
    count_predator = 1

    # unit picture (only emoticons sizes two spaces)
    picture_empty = ' .'
    size_empty = 2 # How many spaces does it take
    picture_grass = '🌱'
    picture_tree = '🌲'
    picture_rock = '⚫'
    picture_herbivore  = '🐇'
    picture_predator = '🐺'

    # other
    delay = 1