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
    
    def sort_bees(self):
        self.bees.sort(key=lambda bee: bee.get_distance())
    
    # def __str__(self):
    #     # return f"Bee with distance {round(self.get_distance(), 2)}"
    #     return self.bees

    # def __str__(self):
    #     return "\n".join([str(bee) for bee in self.bees])

    def mutate_bees(self, bees):
        for bee in bees:
            print("before muttuation", bee.path)
            a = bee.path[1]
            b = bee.path[-2]
            # a, b = b, a
            bee.path[1],bee.path[-2]= b , a
            # bee[:-2]=b
            print("after mutation", bee.path)
            
    def cross_bees():
        pass
    
    def reproduce_bees():
        pass
        #for bee in self.bees:
            
        #self.bees[:10]
