import json
import math


class Bee:
    def __init__(self, distance):
        self.nb_bee = 100
        self.hive_position = (500,500)
        self.distance = distance
        
    def get_flowers(self):
        position_flower = []

        with open("flower.json", "r") as f:
            data = json.load(f)

        for item in data:
            x = item['x']
            y = item['y']    
            position_flower.append((x,y))

        return position_flower

    def calculate_distance(self, pointA, pointD):
        dx = pointA[0] - pointD[0]
        dy = pointA[1] - pointD[1]
        self.distance = math.sqrt(dx**2 + dy**2)
        return self.distance

    def get_distance(self, bees):
        total_distance = []
        for bee in bees:
            distance = 0
            for i in range(len(bee) - 1):
                flower_1 = bee[i]
                flower_2 = bee[i + 1]
                distance += self.calculate_distance(flower_1,flower_2)
            total_distance.append(round(distance, 2))
        return total_distance
