class Cfg():
    # map 
    # max 256x256; min 5x5
    width = 20   # x
    height = 20  # y

    # count_unit
    count_grass = 10
    count_tree = 10
    count_rock = 10
    count_herbivore = 10
    count_predator = 10

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