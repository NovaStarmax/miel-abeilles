from config import NB_BEES, SELECTION_RATE, MUTATION_RATE
from bee import Bee
import random


class Beehive:
    def __init__(self, flowers):
        self.hive_position = (500, 500)
        self.create_bees(flowers)

    def create_bees(self, flowers):
        self.bees = []
        for _ in range(NB_BEES):
            b = Bee(flowers)
            self.bees.append(b)

    def list_bees(self):
        return self.bees

    def sort_bees(self):
        return self.bees.sort(key=lambda bee: bee.get_distance())


    def select_bees(self):
        bees_selected = int(len(self.bees) * SELECTION_RATE)
        self.sort_bees()
        self.bees = self.bees[:bees_selected]
        print(self.bees)

    def mutate_bees(self):
        for _ in range(NB_BEES - len(self.bees)):
            a = random.randint(0, len(self.bees) - 1)
            new_bee = self.bees[a].mutate()
            self.bees.append(new_bee)            

    def average_bees(self):
        total = 0   
        for bee in self.bees:
            total += bee.get_distance()
        average = total / NB_BEES 
        return average

    def cross_bees(self):
        for _ in range(NB_BEES - len(self.bees)):
            a = random.randint(0, len(self.bees) - 1)
            b = random.randint(0, len(self.bees) - 1)
            while a == b:
                b = random.randint(0, len(self.bees) - 1)
            bee_1 = self.bees[a]
            bee_2 = self.bees[b]
            new_child = bee_1.cross(bee_2)
            self.bees.append(new_child)

    def __str__(self):
        bee_info = "\n".join([str(bee) for bee in self.bees]) 
        return f"Beehive with {len(self.bees)} bees:\n{bee_info}"