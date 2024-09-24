import json

class HappyGarden:
    def __init__(self, CHAR_GROUND, CHAR_FLOWER, CHAR_HIVE):
        self.CHAR_GROUND = "🌱"
        self.CHAR_FLOWER = "🌸"
        self.CHAR_HIVE ="🪹"
        
    def generate_empty_matrix(self):
        empty_matrix = [[self.CHAR_GROUND] * 50 for _ in range(50)]
        return empty_matrix

    def put_flower_positions(self, empty_matrix):
        with open("test-flower.json", "r") as f:
            data = json.load(f)

        for item in data:
            x = item['x']
            y = item['y']
            empty_matrix[x][y] = self.CHAR_FLOWER
        return empty_matrix

    def print_garden(self,empty_matrix):
        empty_matrix[25][25] = self.CHAR_HIVE
        for line in empty_matrix:
            print(" ".join(line))   
                 
test = HappyGarden
garden = test.generate_empty_matrix()
garden_flower = test.put_flower_positions(garden)
test.print_garden(garden_flower)