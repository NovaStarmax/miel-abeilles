import random
import time
import json
import math

NB_BEE = 100
HIVE_POSITION = (500,500)

def get_flowers():
    position_flower = []

    with open("flower.json", "r") as f:
        data = json.load(f)

    for item in data:
        x = item['x']
        y = item['y']    
        position_flower.append((x,y))

    return position_flower

def create_bees(flowers):
    bees = []
    for _ in range (NB_BEE):
        bees.append(create_bee(flowers))
    return bees

def create_bee(flowers):
    bee = random.sample(flowers,len(flowers))
    bee.insert(0, HIVE_POSITION)
    return bee

if __name__ == "__main__":
    print("#####################################################################################")
    flowers = get_flowers()
    list_bees = create_bees(flowers)
    print("#####################################################################################")