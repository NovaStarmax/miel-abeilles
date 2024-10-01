from config import NB_BEES,SELECTED_BEES, MUTATION_RATE
from bee import Bee
import random
class Beehive:
    def __init__(self,flowers):
        self.hive_position = (500, 500)
        self.create_bees(flowers)

    def create_bees(self, flowers):
        self.bees = []
        for _ in range (NB_BEES):
            b = Bee(flowers)
            self.bees.append(b)

    def list_bees(self):
        return self.bees

    def sort_bees(self):
        return self.bees.sort(key=lambda bee: bee.get_distance())

    def select_bees(self):
        bees_selected = int(len(self.bees) * SELECTED_BEES)
        self.sort_bees()
        selected_bees = self.bees[:bees_selected]
        return selected_bees

    def mutate_bees(self):
        # bees_mutated = self.bees * MUTATION_RATE
        for bee in self.bees: #bees_mutated:
            a = random.randint(1,len(bee.path)-2)
            b = random.randint(1,len(bee.path)-2)
            if bee.path[a] != bee.path[b]:
                old_distance = bee.get_distance()
                print("_____________________")
                print(old_distance,"OLD distance")
                print(bee.path[a],"PATH AAA BEFORE")
                print(bee.path[b],"PATH BBB BEFORE")
                bee.path[a], bee.path[b] = bee.path[b], bee.path[a]
                print(bee.path[a],"PATH AAA AFTER ")
                print(bee.path[b],"PATH BBB AFTER")
                new_distance = bee.get_distance()
                print(new_distance,"New distance")
                print("_____________________")
                if new_distance > old_distance:
                    bee.path[a], bee.path[b] = bee.path[b], bee.path[a]

    def cross_bees():
        pass

    def reproduce_bees():
        pass
  
    def __str__(self):
        return '\n'.join([str(bee) for bee in self.bees])