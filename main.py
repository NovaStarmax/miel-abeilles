import json
from bee import Bee
from beehive import Beehive


def get_flowers():
    position_flowers = []

    with open("flower.json", "r") as f:
        data = json.load(f)

    for item in data:
        x = item['x']
        y = item['y']    
        position_flowers.append((x,y))

    return position_flowers

if __name__ == "__main__":
    print("#####################################################################################")
    flowers = get_flowers()

    h = Beehive(flowers)
    for i, bee in enumerate(h.list_bees()):
        print(f"Bee {i + 1}: {round(bee.get_distance(), 2)} km")
    
    print("#####################################################################################")