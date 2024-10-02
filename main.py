import json
from bee import Bee
from beehive import Beehive
from config import NB_GEN


def get_flowers():
    position_flowers = []

    with open("flower.json", "r") as f:
        data = json.load(f)

    for item in data:
        x = item["x"]
        y = item["y"]
        position_flowers.append((x, y))

    return position_flowers


if __name__ == "__main__":
    flowers = get_flowers()
    h = Beehive(flowers)

    for i in range(NB_GEN):
        h.select_bees()
        h.cross_bees()
        # h.mutate_bees()
        print(h)

