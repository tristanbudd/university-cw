from graphix import *
import random

def draw_rectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.fill_colour = colour
    rectangle.outline_colour = colour
    rectangle.draw(win)


def draw_polygon(win, list_of_points, colour):
    polygon = Polygon(list_of_points)
    polygon.fill_colour = colour
    polygon.outline_colour = colour
    polygon.draw(win)


def get_inputs():
    door_colours = {"red", "blue", "green", "yellow", "black", "white", "brown", "pink", "purple", "orange"}
    house_colours = []

    while True:
        house_amount = input("Input | How many houses should be drawn? ")

        if house_amount.isdigit():
            house_amount = int(house_amount)

            if house_amount < 0:
                print("Error | Please enter a positive number.")
            else:
                break
        else:
            print("Error | Please enter a valid number.")

    print("Door Colour Options: ", door_colours)

    for i in range(house_amount):
        while True:
            door_colour = input(f"Input | What colour would you like house number {i + 1}'s door to be? ").lower()

            if door_colour in door_colours:
                house_colours.append(door_colour)
                break
            else:
                print("Error | Please enter a valid colour.")

    while True:
        light_probability = input("Input | What is the probability of a light being on? ")

        if 0 <= float(light_probability) <= 1:
            light_probability = float(light_probability)
            break
        else:
            print("Error | Please enter a valid probability.")

    return house_amount, house_colours, light_probability


def draw_street(win, house_amount):
    draw_rectangle(win, Point(0, 200), Point(house_amount * 200, 400), "black")

    for i in range(0, house_amount * 200, 200):
        draw_rectangle(win, Point(i, 300), Point(i + 100, 320), "white")


def draw_house(win, x, door_colour, light_probability):
    draw_rectangle(win, Point(x + 5, 60), Point(x + 190, 200), "brown")
    draw_polygon(win, [Point(x, 60), Point(x + 95, 0), Point(x + 195, 60)], "pink")
    draw_rectangle(win, Point(x + 30, 110), Point(x + 80, 198), door_colour)

    if random.random() < light_probability:
        window_colour = "yellow"
    else:
        window_colour = "black"

    draw_rectangle(win, Point(x + 110, 112), Point(x + 170, 170), window_colour)


def main():
    house_amount, house_colours, light_probability = get_inputs()

    win = Window("Challenge #5 - Draw Street", house_amount * 200, 400)

    draw_street(win, house_amount)

    for i in range(0, house_amount):
        draw_house(win, i * 200, house_colours[i], light_probability)

    win.get_mouse()
    win.close()


if __name__ == "__main__":
    main()
