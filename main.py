import random
import time

CHAR_GROUND = "."

# Matrix generation 1000 x 1000
def generate_empty_matrix():
    empty_matrix = [[CHAR_GROUND] * 1000 for _ in range(1000)]
    return empty_matrix

# Put Flower on the matrix
def flower(empty_matrix):
    x, y = empty_matrix[0], empty_matrix[1]
    for flower in empty_matrix:
        flower


if __name__ == "__main__":
    generate_empty_matrix()
    print()
