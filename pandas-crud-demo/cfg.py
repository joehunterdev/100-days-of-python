import os
PATH = os.path.dirname(os.path.realpath(__file__))
IN_GAME :bool = True

def image_path(folder):
    return os.path.join(PATH, "game/"+folder, "map.gif")

def csv_path(folder):
    return os.path.join(PATH, "game/"+folder, "state-coords.csv")

 