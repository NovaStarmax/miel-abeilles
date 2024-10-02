from beehive import Beehive
from config import NB_GEN, FLOWERS


if __name__ == "__main__":
    
    h = Beehive(FLOWERS)
    # print("base", h)
    for i in range(NB_GEN):
        h.select_bees()
        # print("selected",i, h)
        # for j in range(4):
        h.cross_bees()
       
        h.mutate_bees()
        print("Génération_average", i, ":", round(h.average_bees(), 2), "km")
        # print("cross", i, h)
