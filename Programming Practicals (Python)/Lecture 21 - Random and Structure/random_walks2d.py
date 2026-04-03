from graphix import *
from pract5 import distance_between_points
import random

def take_a_walk(num_steps):
    point = Point(0, 0)

    for step in range(num_steps):
        random_direction = random.choice(["N", "S", "E", "W"])

        if random_direction == "N":
            point = Point(point.x, point.y + 1)
        elif random_direction == "S":
            point = Point(point.x, point.y - 1)
        elif random_direction == "E":
            point = Point(point.x + 1, point.y)
        else:
            point = Point(point.x - 1, point.y)

    distance = distance_between_points(Point(0, 0), point)

    return distance


def main():
    print(take_a_walk(5))
    print(take_a_walk(10))
    print(take_a_walk(25))
    print(take_a_walk(50))
    print(take_a_walk(100))


if __name__ == "__main__":
    main()
