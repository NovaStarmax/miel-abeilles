from beehive import Beehive
from config import NB_GEN, FLOWERS
import matplotlib.pyplot as plt

if __name__ == "__main__":
    h = Beehive(FLOWERS)
    print([bee.distance for bee in h.bees])
    average_distances = [] 
    for i in range(NB_GEN):
        h.select_bees()
        h.cross_bees()
        for j in range():
            h.mutate_bees()
        # avg = h.average_bees()
        # # print(i, avg)
        # average_distances.append(avg)


        # # print(AVERAGE_DISTANCES, "Averageeee")
        # if len(average_distances) >= 3:
        # # # #     # print("ité pour -1 :", i, ":", AVERAGE_DISTANCES[-1])
        # # # #     # print("ité pour -3:",i, ":", AVERAGE_DISTANCES[-3])
        #     # if average_distances[-1] > average_distances[-3]:
        #         # print("mutate")
        #         # h.cross_bees()
        #         h.mutate_bees()

        # print(f"Génération {i} : Distance moyenne = {round(average_distance, 2)} km")
        avg = h.average_bees()
        # print(i, avg)
        average_distances.append(avg)
        print(len(h.bees))

    # print(average_distances)

    plt.plot(average_distances, label="Average Distance", c ="red", lw = 1) 
    plt.title("Evolution of generation")
    plt.xlabel("Generation")
    plt.ylabel("Average distance")
    plt.legend()


    plt.show()