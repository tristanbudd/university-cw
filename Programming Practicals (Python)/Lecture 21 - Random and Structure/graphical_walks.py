from graphix import *
from pract5 import distance_between_points
import random

def get_number_of_walks():
    while True:
        input_amount = input("Input | How many walks should be drawn? ")

        if input_amount.isdigit():
            input_amount = int(input_amount)

            if input_amount < 0:
                print("Error | Please enter a positive number.")
            else:
                return input_amount


def draw_frame(num_walks):
    win = Window("Graphical Random Walk", 200, 200)

    outer_circle = Circle(Point(100, 100), 100)
    outer_circle.fill_colour = "white"
    outer_circle.outline_colour = "black"
    outer_circle.draw(win)

    point = Point(100, 100)

    for i in range(num_walks):
        while True:
            random_direction = random.choice(["N", "S", "E", "W"])

            starting_point = Point(point.x, point.y)

            if random_direction == "N":
                point = Point(point.x, point.y + 5)
            elif random_direction == "S":
                point = Point(point.x, point.y - 5)
            elif random_direction == "E":
                point = Point(point.x + 5, point.y)
            else:
                point = Point(point.x - 5, point.y)

            if distance_between_points(Point(100, 100), point) < 100:
                line = Line(starting_point, point)
                line.draw(win)
                break

    win.get_mouse()
    win.close()


def main():
    draw_frame(get_number_of_walks())



if __name__ == "__main__":
    main()
