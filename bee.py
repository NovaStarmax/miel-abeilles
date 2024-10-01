import math
import random
HIVE =(500,500)

class Bee:
    def __init__(self, flowers):
        self.create_path(flowers)
        self.compute_path()

    def __str__(self):
        return f" Distance = {round(self.distance, 2)} km, Path = {self.path}"

    def create_path(self, flowers):
        self.path = random.sample(flowers, len(flowers))
        self.path.insert(0, (500, 500))
        self.path.append((500, 500)) 

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
        a = random.randint(1,len(self.path)-2)
        b = random.randint(1,len(self.path)-2)
        if a != b:
            self.path[a], self.path[b] = self.path[b], self.path[a]

    def cross(bee_1, bee_2):
        # new = Bee_()
        segment_size = int(len(bee_1.path)/4)
        print(segment_size)
        # print(bee_1.path,"OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        for i in range(0, len(bee_1.path), segment_size*4):
            # print(i)
            child_1 = bee_1.path[i:i+segment_size] + bee_2.path[i+segment_size:i+segment_size*2] + bee_1.path[i+segment_size*2:i+segment_size*3] + bee_2.path[i+segment_size*3:i+segment_size*4]
            print("child 1", child_1)
            child_2 = bee_2.path[i:i+segment_size] + bee_1.path[i+segment_size:i+segment_size*2] + bee_2.path[i+segment_size*2:i+segment_size*3] + bee_1.path[i+segment_size*3:i+segment_size*4]
            print("child 2", child_2)

            # idée pour contrer les doublons, une liste qui contient tout les sommets, 
            # on parcourt l'enfant si doublon on change avec un sommet d'ordre chrono qui n'est pas présent chez l'enfant