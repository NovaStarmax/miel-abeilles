from beehive import Beehive
from config import NB_GEN, FLOWERS, AVERAGE_DISTANCES
import matplotlib.pyplot as plt

if __name__ == "__main__":
    h = Beehive(FLOWERS)
    
    for i in range(NB_GEN):
        h.select_bees()
        h.cross_bees()
        
        
        h.average_bees()
        AVERAGE_DISTANCES.append(h.average_bees())


        # print(AVERAGE_DISTANCES, "Averageeee")
        if len(AVERAGE_DISTANCES) >= 3:
            # print("ité pour -1 :", i, ":", AVERAGE_DISTANCES[-1])
            # print("ité pour -3:",i, ":", AVERAGE_DISTANCES[-3])
            if AVERAGE_DISTANCES[-1] > AVERAGE_DISTANCES [-3]:
                h.mutate_bees()

        # print(f"Génération {i} : Distance moyenne = {round(average_distance, 2)} km")


    plt.plot(AVERAGE_DISTANCES, label="Average Distance", c ="red", lw = 1) 
    plt.title("Evolution of generation")
    plt.xlabel("Generation")
    plt.ylabel("Average distance")
    plt.legend()


    plt.show()