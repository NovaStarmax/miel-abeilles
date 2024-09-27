from config import NB_BEES
from bee import Bee
class Beehive:
    def __init__(self,flowers):
        self.hive_position = (500, 500)
        self.create_bees(flowers)

    def create_bees(self, flowers):
        self.bees = []
        # Appeler compute_path a chaque création de path(bee)
        for _ in range (NB_BEES):
            b = Bee(flowers)
            self.bees.append(b)

    def list_bees(self):
        return self.bees
    
    def __str__(self):
        return f"This is a sorted bee {self.sorted_bees}"

    def sort_bees(self):
        self.bees.sort(key=lambda bee: bee.get_distance())


    #def mutate_bees(self, bees):
        #for i in range(len(bees)):
            #if random.random < self.mutation_frequency:
                #return 
            
    def cross_bees():
        pass
    
    def reproduce_bees():
        pass
        #for bee in self.bees:
            
        #self.bees[:10]
