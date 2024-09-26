import random

class Beehive:
    def __init__(self):
        self.nb_bee = 100
        self.hive_position = (500, 500)
        # Proposer un input pour gamifier notre programme
        self.selected_bees = 0.2
        self.mutation_rate = 0.1
        self.mutation_frequency = 0.2

    def create_bees(self, flowers):
        bees = []
        for _ in range (self.nb_bee):
            bees.append(self.create_bee(flowers))
        return bees

    def create_bee(self, flowers):
        bee = random.sample(flowers,len(flowers))
        bee.insert(0, self.hive_position)
        bee.insert(-1, self.hive_position)
        return bee 
    
    def select_bees(self):
        for i in range(len(self.bees)):
            if random.random < self.selected_bees:
                return 
            
    def mutate_bees(self):
        for i in range(len(self.bees)):
            if random.random < self.mutation_frequency:
                return 
            
    def cross_bees():
        pass
    
    def reproduce_bees():
        pass
        #for bee in self.bees:
            
        #self.bees[:10]