### https://docs.google.com/document/d/1sPkmvk39DaChoiqpdgo4UlfT0YZw3ah0/edit

from graphix import *
import math

# Challenge #1 - Finish the Stick Figure
def draw_stick_figure():
    win = Window("Challenge #1", 400, 400)

    head = Circle(Point(200, 120), 40)
    head.draw(win)

    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)

    left_arm = Line(Point(200, 180), Point(160, 210))
    left_arm.draw(win)

    right_arm = Line(Point(200, 180), Point(240, 210))
    right_arm.draw(win)

    left_leg = Line(Point(200, 240), Point(160, 300))
    left_leg.draw(win)

    right_leg = Line(Point(200, 240), Point(240, 300))
    right_leg.draw(win)


# Challenge #2 - Draw Circle (Based On User Input)
def draw_circle():
    radius = int(input("Enter the radius of the circle: "))

    win = Window("Challenge #2", 400, 400)

    circle = Circle(Point(200, 200), radius)
    circle.draw(win)


# Challenge #3 - Draw an Archery Target
def draw_archery_target():
    inner_circle_size = 50
    middle_circle_size = inner_circle_size * 2
    outer_circle_size = inner_circle_size * 3

    win = Window("Challenge #3", 400, 400)

    outer_circle = Circle(Point(200, 200), outer_circle_size)
    outer_circle.fill_colour = "blue"
    outer_circle.draw(win)

    middle_circle = Circle(Point(200, 200), middle_circle_size)
    middle_circle.fill_colour = "red"
    middle_circle.draw(win)

    inner_circle = Circle(Point(200, 200), inner_circle_size)
    inner_circle.fill_colour = "yellow"
    inner_circle.draw(win)


# Challenge #4 - Draw Rectangle (Based On User Width & Height Input)
def draw_rectangle():
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))

    win = Window("Challenge #4", 400, 400)

    rectangle = Rectangle(Point(200 - (width // 2), 200 - (height // 2)), Point(200 + (width // 2), 200 + (height // 2)))
    rectangle.draw(win)


# Challenge #5 - Draw Blue Circle (Based On User Press)
def blue_circle():
    win = Window("Challenge #5", 400, 400)

    mouse = win.get_mouse()

    circle = Circle(mouse, 100)
    circle.fill_colour = "blue"
    circle.draw(win)


# Challenge #6 - Draw Line Between Two Points
def draw_line():
    win = Window("Challenge #6", 400, 400)

    point_1 = win.get_mouse()
    point_2 = win.get_mouse()

    line = Line(point_1, point_2)
    line.draw(win)

# Challenge #6b - Allow Up To 10 Lines
def ten_lines():
    win = Window("Challenge #6b", 400, 400)

    for i in range(10):
        point_1 = win.get_mouse()
        point_2 = win.get_mouse()

        line = Line(point_1, point_2)
        line.draw(win)


# Challenge #7 - Plot 10 Strings
def plot_strings():
    win = Window("Challenge #7", 400, 400)

    message = Text(Point(200, 30), "Enter a string, then click somewhere to place the text.")
    message.draw(win)

    input_box = Entry(Point(200, 50), 10)
    input_box.draw(win)

    for i in range(10):
        text = Text(win.get_mouse(), input_box.text)
        text.draw(win)

        input_box.text = ""


# Challenge #8 - Draw 10 Coloured Rectangles
def ten_coloured_rectangles():
    win = Window("Challenge #8", 400, 400)

    message = Text(Point(200, 30), "Please enter the name of the colour you want the rectangle.")
    message.draw(win)

    input_box = Entry(Point(200, 50), 10)
    input_box.draw(win)

    for i in range(10):
        point_1 = win.get_mouse()
        point_2 = win.get_mouse()

        rectangle = Rectangle(point_1, point_2)
        rectangle.fill_colour = input_box.text
        rectangle.draw(win)

        input_box.text = ""


# Challenge #9 - Draw Stick Figure In 5 Clicks
def five_click_stick_figure():
    win = Window("Challenge #9", 400, 400)

    head_center = win.get_mouse()
    head_outer = win.get_mouse()

    head_radius = math.sqrt((head_outer.x - head_center.x)**2 + (head_outer.y - head_center.y)**2)

    head = Circle(head_center, int(head_radius))
    head.draw(win)

    body_top = Point(head_center.x, int(head_center.y + head_radius))
    body_bottom = win.get_mouse()

    body = Line(body_top, body_bottom)
    body.draw(win)

    arm_data = win.get_mouse()

    arm_left = Point(arm_data.x, arm_data.y)
    arm_right = Point(int(head_center.x + (head_center.x - arm_data.x)), arm_data.y)

    arm = Line(arm_left, arm_right)
    arm.draw(win)

    leg_data = win.get_mouse()

    leg_left = Line(body_bottom, leg_data)
    leg_left.draw(win)

    leg_right_bottom = Point(int(body_bottom.x + (body_bottom.x - leg_data.x)), leg_data.y)
    leg_right = Line(body_bottom, leg_right_bottom)
    leg_right.draw(win)
