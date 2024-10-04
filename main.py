from beehive import Beehive
from config import NB_GEN, FLOWERS
import matplotlib.pyplot as plt

if __name__ == "__main__":
    h = Beehive(FLOWERS)
    # print([bee.distance for bee in h.bees])
    average_distances = [] 
    for i in range(NB_GEN):
        h.select_bees()
        h.cross_bees()
        # avg = h.average_bees()
        average_distances.append(h.average_bees())
        
    for j in range(NB_GEN):
        h.select_bees()
        h.mutate_bees()
        print(h)
        # avg = h.average_bees()
        average_distances.append(h.average_bees())

    plt.plot(average_distances, label="Average Distance", c ="red", lw = 1) 
    plt.title("Evolution of generation")
    plt.xlabel("Generation")
    plt.ylabel("Average distance")
    plt.legend()

    plt.show()

        
