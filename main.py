import random
import time
import json
import math

NB_BEE = 100

def get_flowers():
    position_flower = []

    with open("test-flower.json", "r") as f:
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
    bee = [random.sample(flowers,len(flowers))]
    return bee

def calculate_distance(xa, xd, ya, yd):
    dx = xa['x'] - xd['x']
    dy = ya['y'] - yd['y']
    distance = math.sqrt(dx**2 + dy**2)
    return distance

def get_distance(bees):
    for bee in bees:
        #print(bee)
        for flower_1 in bee:
            #print(flower_1,"zertyuioiuytrertyuio")
            for f in flower_1:
                #print(f,"FFFFFFFFFFFFFFF")
                x,y = f
                #print(x,"XXXX")
                #print(y,"YYYYYYYYY")
                
            # print(flower_2)
            # xd,yd = flower_1
            # xa,ya = flower_2
            # print(xa,ya,"X,Y")
            # print(xd,yd,"A,B")

if __name__ == "__main__":
    flo = get_flowers()
    list_bees = create_bees(flo)
    print(get_distance(list_bees))