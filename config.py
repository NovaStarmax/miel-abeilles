import json

def get_flowers(path):
    position_flowers = []

    with open(path, "r") as f:
        data = json.load(f)

    for item in data:
        x = item["x"]
        y = item["y"]
        position_flowers.append((x, y))

    return position_flowers

PATH = "flowers.json"
FLOWERS = get_flowers(PATH)
SELECTION_RATE = 0.2 # Meilleur à 0,2 
MUTATION_RATE = 0.10 #Meilleur à 0,1 
MUTATION_FREQUENCY = 0.02 # Meilleur à 0,02
NB_BEES = 100 
NB_GEN = 1000 # Très bien à partir de 1000
CROSS_PART = 0.5 #Meilleur à 0,6