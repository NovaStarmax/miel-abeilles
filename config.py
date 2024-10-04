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

PATH = "flower.json"
FLOWERS = get_flowers(PATH)
SELECTION_RATE = 0.7
MUTATION_RATE = 0.2
# MUTATION_FREQUENCY = 0.2
NB_BEES = 100
NB_GEN = 500