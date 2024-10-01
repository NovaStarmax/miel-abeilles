import json
from bee import Bee
from beehive import Beehive

def get_flowers():
    position_flowers = []

    with open("flower.json", "r") as f:
        data = json.load(f)

    for item in data:
        x = item['x']
        y = item['y']    
        position_flowers.append((x,y))

    return position_flowers

if __name__ == "__main__":
    flowers = get_flowers()
    h = Beehive(flowers)


    # print("before mutation")
    # print(h)
    #Appelle de beehive 1 fois et aucun appelle de bee

    print("Selected Bees:")
    h.select_bees()
    for i, bee in enumerate(h.selected_bees):
        print(f"Bee {i + 1}: {bee}")
    
    
    # h.mutate_bees()
    # print("After Mutation:")
    # print(h)
    
    h.cross_bees()