from bee import Bee
from beehive import Beehive


if __name__ == "__main__":
    print("#####################################################################################")
    b = Bee(0)
    h = Beehive()
    flowers = b.get_flowers()
    list_bees = h.create_bees(flowers)
    distances = b.get_distance(list_bees)
    for i, distance in enumerate(distances, start=1):
        print(f"Bee {i}: {distance} km")
    
    print("#####################################################################################")