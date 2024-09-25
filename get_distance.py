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

def calculate_distance(pointA, pointD):
    dx = pointA[0] - pointD[0]
    dy = pointA[1] - pointD[1]
    distance = math.sqrt(dx**2 + dy**2)
    return distance

def get_distance(bees):
    total_distance = []
    for bee in bees:
        distance = 0
        for i in range(len(bee) - 1):
            flower_1 = bee[i]
            flower_2 = bee[i + 1]
            distance += calculate_distance(flower_1,flower_2)
        total_distance.append(round(distance, 2))

    return total_distance

if __name__ == "__main__":
    print("#####################################################################################")
    flowers = get_flowers()
    list_bees = create_bees(flowers)
    print(get_distance(list_bees))
    print("#####################################################################################")