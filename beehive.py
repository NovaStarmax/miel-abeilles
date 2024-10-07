import random
from bee import Bee
from config import NB_BEES, SELECTION_RATE, MUTATION_RATE

class Beehive:
    def __init__(self, flowers):
        self.flowers = flowers
        self.create_bees(flowers)

    def create_bees(self, flowers):
        self.bees = []
        for _ in range(NB_BEES):
            b = Bee(flowers)
            self.bees.append(b)


    def sort_bees(self):
        return self.bees.sort(key=lambda bee: bee.get_distance())
    

    def select_bees(self):
        nb_selected = int(len(self.bees) * SELECTION_RATE)
        self.sort_bees()
        selected_bees = self.bees[:nb_selected]
        return selected_bees

    def cross_bees(self):
        selected_bees = self.select_bees()
        new_population = []

        while len(new_population) < NB_BEES:
            bee_1 = random.choice(selected_bees)
            bee_2 = random.choice(selected_bees)
            while bee_1 == bee_2:
                bee_2 = random.choice(selected_bees)
            child = bee_1.cross(bee_2)
            new_population.append(child)

        self.bees = new_population

    def mutate_bees(self):
        nb_bees_to_mutate = int(NB_BEES * MUTATION_RATE)
        bees_to_mutate = random.sample(self.bees, nb_bees_to_mutate)
        for bee in bees_to_mutate:
            bee.mutate()

    def average_bees(self):
        total = 0   
        for bee in self.bees:
            total += bee.get_distance()
        average = total / NB_BEES 
        return average