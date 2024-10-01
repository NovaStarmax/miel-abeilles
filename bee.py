import math
import random

HIVE_POSITION = (500, 500)

class Bee:
    def __init__(self, flowers):
        self.create_path(flowers)
        self.compute_path()

    def __str__(self):
        return f" Distance = {round(self.distance, 2)} km" #, Path = {self.path}"

    def create_path(self, flowers):
        self.path = random.sample(flowers, len(flowers))
        self.path.insert(0, HIVE_POSITION)
        self.path.append(HIVE_POSITION) 

    def compute_segment(self, pointA, pointD):
        dx = pointA[0] - pointD[0]
        dy = pointA[1] - pointD[1]
        return math.sqrt(dx**2 + dy**2)
     
    def compute_path(self):
        self.distance = 0

        for i in range(len(self.path) - 1):
            flower_1 = self.path[i]
            flower_2 = self.path[i + 1]
            self.distance += self.compute_segment(flower_1,flower_2)

    def get_distance(self):
        return self.distance
