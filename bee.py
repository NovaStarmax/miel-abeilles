import math
import random
import copy

from config import FLOWERS, MUTATION_RATE, CROSS_PART
HIVE =(500,500)

class Bee:
    def __init__(self, flowers, path = []):
        if len(path)==0:
            self.create_path(flowers)
        else: 
            self.path = path
        self.compute_path()

    def __str__(self):
        return f" Distance = {round(self.distance, 2)}, Path = {self.path}"

    def create_path(self, flowers):
        self.path = random.sample(flowers, len(flowers))

    def compute_segment(self, pointA, pointD):
        dx = pointA[0] - pointD[0]
        dy = pointA[1] - pointD[1]
        return math.sqrt(dx**2 + dy**2)

    def compute_path(self):
        self.distance =  self.compute_segment(HIVE, self.path[0])
        for i in range(len(self.path) - 1):
            flower_1 = self.path[i]
            flower_2 = self.path[i + 1]
            self.distance += self.compute_segment(flower_1,flower_2)
        self.distance += self.compute_segment(self.path[-1], HIVE)      

    def get_distance(self):
        return self.distance

    def mutate(self):
        a = random.randint(0,len(self.path)-1)
        b = random.randint(0,len(self.path)-1)
        bee = copy.copy(self)

        if a != b and random.random() < MUTATION_RATE:
            bee.path[a], bee.path[b] = bee.path[b], bee.path[a]
            self.compute_path()
        return bee
        
    def cross(bee_1, bee_2):
        segment_size = int(len(bee_1.path)*CROSS_PART)
        child_path = bee_1.path[0:segment_size]
        for f in bee_2.path:
            if f not in child_path:
                child_path.append(f)
        return Bee(FLOWERS,path = child_path)