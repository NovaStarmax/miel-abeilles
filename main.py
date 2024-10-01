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

# if __name__ == "__main__":
#     print("#####################################################################################")
#     flowers = get_flowers()
#     h = Beehive(flowers)
#     # b = Bee(flowers)

#     for i, bee in enumerate(h.list_bees()):
#         print(f"Bee {i + 1}: {bee}")

#     # for i, bee in enumerate(h.list_bees()):
#     #     print(f"Bee {i + 1}: {round(bee.get_distance(), 2)} km")
#     # print(b.path())

#     print(h.select_bees())
#     h.mutate_bees()
#     # str(h.sort_bees())
  
#     # for bee in h.bees:
#     #     print(f"Bee: {bee}, Distance: {round(bee.get_distance(), 2)}")
    
#     print("#####################################################################################")

if __name__ == "__main__":
    flowers = get_flowers()
    h = Beehive(flowers)


    # print("before mutation")
    # print(h)


    # print("Selected Bees:")
    # selected_bees = h.select_bees()
    # for i, bee in enumerate(selected_bees):
    #     print(f"Bee {i + 1}: {bee}")
    
    
    h.mutate_bees()
    print("After Mutation:")
    print(h)