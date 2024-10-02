from beehive import Beehive
from config import NB_GEN, FLOWERS

if __name__ == "__main__":
    
    h = Beehive(FLOWERS)

    for i in range(NB_GEN):
        h.select_bees()
        for j in range(4):
            h.cross_bees()
        # h.mutate_bees()
        print(h)

