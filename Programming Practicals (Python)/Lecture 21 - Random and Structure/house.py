from graphix import Window, Point, Rectangle, Polygon

def main():
    door_colour, lights_on = get_inputs()
    draw_house(door_colour, lights_on)


def get_inputs():
    door_colours = {"red", "blue", "green", "yellow", "black", "white", "brown", "pink", "purple", "orange"}

    while True:
        print("Door Colour Options: ", door_colours)
        door_colour = input("Input | What colour should the door be? ").lower()

        if door_colour in door_colours:
            break
        else:
            print("Error | Please enter a valid colour.")

    while True:
        lights_on = input("Input | Should the lights be on? (y/n) ")

        if lights_on.lower() == "y":
            lights_on = True
            break
        elif lights_on.lower() == "n":
            lights_on = False
            break
        else:
            print("Error | Please enter a valid option.")

    return door_colour, lights_on


def draw_house(door_colour, lights_on):
    win = Window("House", 200, 200)
    list_of_points = [Point(0, 60), Point(100, 0), Point(200, 60)]
    roof = Polygon(list_of_points)
    roof.fill_colour = "pink"
    roof.outline_colour = "pink"
    roof.draw(win)

    # draw wall and door
    draw_rectangle(win, Point(2, 60), Point(198, 198), "brown")
    draw_rectangle(win, Point(30, 110), Point(80, 198), door_colour)

    # draw window
    if lights_on:
        window_colour = "yellow"
    else:
        window_colour = "black"

    draw_rectangle(win, Point(110, 110), Point(170, 170), window_colour)

    win.get_mouse()
    win.close()


def draw_rectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.fill_colour = colour
    rectangle.outline_colour = colour
    rectangle.draw(win)


main()