from graphix import *
from pract5 import distance_between_points
import random

def get_inputs():
    while True:
        amount_of_steps = input("Input | How many steps should be taken? ")

        if amount_of_steps.isdigit():
            amount_of_steps = int(amount_of_steps)

            if amount_of_steps < 0:
                print("Error | Please enter a positive number.")
            else:
                return amount_of_steps

    return amount_of_steps


def take_a_walk(num_steps):
    point = [4, 4]
    step_tracker = [[0 for _ in range(9)] for _ in range(9)]

    for step in range(num_steps):
        random_direction = random.choice(["N", "S", "E", "W"])

        if random_direction == "N":
            point[1] += 1
        elif random_direction == "S":
            point[1] -= 1
        elif random_direction == "E":
            point[0] += 1
        else:
            point[0] -= 1

        if point[0] < 0 or point[0] >= 9 or point[1] < 0 or point[1] >= 9:
            break

        step_tracker[point[1]][point[0]] += 1

    for i in range(9):
        for j in range(9):
            print(f"{step_tracker[i][j]}", end=" ")
        print()


def main():
    take_a_walk(get_inputs())


if __name__ == "__main__":
    main()
