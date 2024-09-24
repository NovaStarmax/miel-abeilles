import random
import time
import json

CHAR_GROUND = "🌱"
CHAR_FLOWER = "🌸"
CHAR_HIVE ="🪹"

# Matrix generation 1000 x 1000
def generate_empty_matrix():
    empty_matrix = [[CHAR_GROUND] * 50 for _ in range(50)]
    return empty_matrix

def put_flower_positions(empty_matrix):
    with open("test-flower.json", "r") as f:
        data = json.load(f)

    for item in data:
        x = item['x']
        y = item['y']
        empty_matrix[x][y] = CHAR_FLOWER
    return empty_matrix

def print_garden(empty_matrix):
    empty_matrix[25][25] = CHAR_HIVE
    for line in empty_matrix:
        print(" ".join(line))

if __name__ == "__main__":
    garden = generate_empty_matrix()
    #print_garden(garden)
    garden_flower = put_flower_positions(garden)
    print_garden(garden_flower)
