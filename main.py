from beehive import Beehive
from config import NB_GEN, FLOWERS
import matplotlib.pyplot as plt

if __name__ == "__main__":
    h = Beehive(FLOWERS)

    average_distances = []
    best_bees_generation = []

    for i in range(NB_GEN):
        h.cross_bees()
        h.mutate_bees()
        average_distances.append(h.average_bees())

        get_best_bee = min(h.bees, key=lambda bee: bee.get_distance()) #min permet prendre l'objet avec la valeur la plus faible
        best_bees_generation.append(get_best_bee)
    




    master_bee = min(best_bees_generation, key=lambda bee: bee.get_distance()) #min permet prendre l'objet avec la valeur la plus faible
    master_bee_path = master_bee.path
  
    master_bee_path.append((500, 500))  
    master_bee_path.insert(0, (500, 500))

    x, y = zip(*master_bee_path) #* pour décompresser la liste en deux 

    best_bee_distance = master_bee.get_distance()


    plt.figure()

    plt.subplot(1, 2, 1)
    plt.plot(average_distances, label="Average Distance", color="red", lw=1)
    plt.title("Evolution of generation")
    plt.xlabel("Generation")
    plt.ylabel("Average distance")
    plt.legend()
   
    plt.subplot(1, 2, 2)
    plt.plot(x, y, 'o--', color="green", label="Best Bee Path")
    plt.title("Best Bee Path of All Generation")
    plt.text(0.95, 0.95,f"Final Distance: {best_bee_distance:.2f}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()

    plt.show()
