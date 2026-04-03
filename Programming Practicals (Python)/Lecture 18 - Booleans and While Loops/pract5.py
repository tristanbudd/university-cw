### https://docs.google.com/document/d/1DAedbr5NWQulkprhBVfTOzkjh1JyQGL4/edit#heading=h.gjdgxs

from graphix import *
import math

# Challenge #1 - Area & Circumference of Circle
def area_of_circle(radius):
    return math.pi * radius ** 2

def circumference_of_circle(circumference):
    return 2 * math.pi * circumference


# Challenge #2 - Circle Info (Based on user input)
def circle_info():
    radius = float(input("Enter the radius of the circle: "))

    area = area_of_circle(radius)
    circumference = circumference_of_circle(radius)

    print(f"The area of the circle is: {area:.3f}")
    print(f"The circumference of the circle is: {circumference:.3f}")


# Challenge #3 - Draw Circles (w/ Functions)
def draw_circle(win, point, radius, colour):
    circle = Circle(point, radius)
    circle.fill_colour = colour
    circle.draw(win)

def draw_brown_eye_in_centre():
    win = Window("Challenge #3", 400, 400)

    draw_circle(win, Point(200, 200), 120, "white")
    draw_circle(win, Point(200, 200), 60, "brown")
    draw_circle(win, Point(200, 200), 30, "black")

    win.get_mouse()
    win.close()


# Challenge #4 - Draw Block Of Stars
def draw_block_of_stars(columns, rows):
    for i in range(rows):
        for j in range(columns):
            print("*", end="")
        print()


def draw_letter_e():
    draw_block_of_stars(8, 2)
    draw_block_of_stars(2, 2)
    draw_block_of_stars(6, 2)
    draw_block_of_stars(2, 2)
    draw_block_of_stars(8, 2)


# Challenge #5 - Pair of Brown Eyes
def draw_brown_eye(win, point, radius):
    draw_circle(win, point, int(radius), "white")
    draw_circle(win, point, int(radius / 2), "brown")
    draw_circle(win, point, int(radius / 4), "black")


def draw_pair_of_brown_eyes():
    win = Window("Challenge #5", 560, 400)

    draw_brown_eye(win, Point(160, 200), 120)
    draw_brown_eye(win, Point(400, 200), 120)

    win.get_mouse()
    win.close()


# Challenge #6 - Distance Between Co-Ordinates
def distance_between_points(point1, point2):
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)


# Challenge #7 - Distance Calculator (w/ Graphix)
def distance_calculator():
    win = Window("Challenge #7", 400, 400)

    text_box = Text(Point(200, 50), "Click on two points to calculate distance:")
    text_box.draw(win)

    point1 = win.get_mouse()
    point2 = win.get_mouse()

    distance = distance_between_points(point1, point2)
    text_box.text = f"Distance Between Points: {distance:.2f}"

    win.get_mouse()
    win.close()


# Challenge #8 - Draw Blocks (For more complex characters)
def draw_blocks(gap1, width1, gap2, width2, height):
    for i in range(height):
        for j in range(gap1):
            print(" ", end="")
        for j in range(width1):
            print("*", end="")
        for j in range(gap2):
            print(" ", end="")
        for j in range(width2):
            print("*", end="")
        print()

def draw_letter_a():
    draw_blocks(1, 8, 0, 0, 2)
    draw_blocks(0, 2, 6, 2, 2)
    draw_blocks(0, 10, 0, 0, 2)
    draw_blocks(0, 2, 6, 2, 3)


# Challenge #9 - Four pairs of Brown Eyes.
def draw_four_pairs_of_brown_eyes():
    win = Window("Challenge #9", 800, 800)

    for i in range(4):
        eye_centre = win.get_mouse()
        eye_outer = win.get_mouse()

        radius = distance_between_points(eye_centre, eye_outer)

        draw_brown_eye(win, eye_centre, radius)
        draw_brown_eye(win, Point(eye_centre.x + int(radius * 2), eye_centre.y), radius)

    win.get_mouse()
    win.close()


# Challenge #10 - Vision Chart
def display_text_with_spaces(win, point, text, size):
    text = text.upper()
    text = " ".join(text)

    text_box = Text(point, text)
    text_box.size = size
    text_box.draw(win)

def construct_vision_chart():
    win = Window("Challenge #10", 400, 400)

    print("Please enter six strings of text to display on the vision chart:")
    for i in range(6):
        text = input(f"Enter text {i + 1}: ")
        display_text_with_spaces(win, Point(200, 50 + (i * 65)), text, 30 - (i * 5))

    win.get_mouse()
    win.close()


# Challenge #11 - Stick Figure Family
def draw_stick_figure(win, point, size):
    head = Circle(point, size)
    head.draw(win)

    body = Line(Point(point.x, point.y + size), Point(point.x, point.y + size * 3))
    body.draw(win)

    left_arm = Line(Point(point.x, point.y + size * 2), Point(point.x - size, point.y + size * 2))
    left_arm.draw(win)

    right_arm = Line(Point(point.x, point.y + size * 2), Point(point.x + size, point.y + size * 2))
    right_arm.draw(win)

    left_leg = Line(Point(point.x, point.y + size * 3), Point(point.x - size, point.y + size * 5))
    left_leg.draw(win)

    right_leg = Line(Point(point.x, point.y + size * 3), Point(point.x + size, point.y + size * 5))
    right_leg.draw(win)


def draw_stick_figure_family():
    win = Window("Challenge #11", 400, 400)

    draw_stick_figure(win, Point(100, 100), 40)
    draw_stick_figure(win, Point(170, 120), 20)
    draw_stick_figure(win, Point(230, 120), 20)
    draw_stick_figure(win, Point(200, 250), 25)
    draw_stick_figure(win, Point(300, 100), 40)

    win.get_mouse()
    win.close()