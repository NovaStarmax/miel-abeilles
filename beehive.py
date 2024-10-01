from config import NB_BEES,SELECTED_BEES
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
        self.selected_bees = self.bees[:bees_selected]
        print(self.bees[:bees_selected])
        # print(self.selected_bees)
        
    def mutate_bees(self):
        for bee in self.selected_bees:
            bee.mutate()

    def cross_bees(self):
        for i in range(len(self.selected_bees)-1):
            bee_1 = self.selected_bees[i]
            bee_2 = self.selected_bees[i+1]
            bee_1.cross(bee_2)

    def reproduce_bees():
        pass
  
def __str__(self):
    return '\n'.join([str(bee) for bee in self.bees])# + '\n'.join([str(bee) for bee in self.selected_bees])