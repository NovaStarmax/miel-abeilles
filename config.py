import json

def get_flowers():
    position_flowers = []

    with open("flower.json", "r") as f:
        data = json.load(f)

    for item in data:
        x = item["x"]
        y = item["y"]
        position_flowers.append((x, y))

    return position_flowers

FLOWERS = get_flowers()
SELECTION_RATE = 0.2
MUTATION_RATE = 0.2
MUTATION_FREQUENCY = 0.2
NB_BEES = 100
NB_GEN = 100