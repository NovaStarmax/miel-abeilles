# from beehive import Beehive
# from config import NB_GEN, FLOWERS



# if __name__ == "__main__":
    
#     h = Beehive(FLOWERS)
#     # print("base", h)
#     for i in range(NB_GEN):
#         h.select_bees()
#         # print("selected",i, h)
#         # for j in range(4):
#         h.cross_bees()
       
#         # h.mutate_bees()
#         print("Génération_average", i, ":", round(h.average_bees(), 2), "km")
#         # print("cross", i, h)

from beehive import Beehive
from config import NB_GEN, FLOWERS
import matplotlib.pyplot as plt

if __name__ == "__main__":
    h = Beehive(FLOWERS)
    average_distances = [] 
    
    for i in range(NB_GEN):
        h.select_bees()
        h.cross_bees()
        h.mutate_bees() # a revoir, source du pb
        
        h.average_bees()
        average_distances.append(h.average_bees())
        
        # print(f"Génération {i} : Distance moyenne = {round(average_distance, 2)} km")


    plt.plot(average_distances, label="Average Distance", c ="red", lw = 1) 
    plt.title("Evolution of generation")
    plt.xlabel("Generation")
    plt.ylabel("Average distance")
    plt.legend()


    plt.show()