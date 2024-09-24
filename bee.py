import json
import random
import time

class Bee:
    def __init__(self, id, distance):
        self.id = id
        self.distance = distance
        
    def list_flower(self):
        position_flower = []
        
        with open("test-flower.json", "r") as f:
            data = json.load(f)

        for item in data:
            x = item['x']
            y = item['y']    
            position_flower.append((x,y))

        return position_flower
    
    def create_all_bees(self, creation):
        self.creation = creation
        random.sample(self.position_flower,len(self.position_flower))
        
test = Bee(1,10,100)
test.list_flower()