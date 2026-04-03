from graphix import *

def mystery_1():
    win = Window()
    rectangle = Rectangle(Point(100, 100), Point(200,200))
    rectangle.fill_colour = "blue"
    rectangle.draw(win)
    circle = Circle(Point(200, 200), 100)
    circle.fill_colour = "red"
    circle.draw(win)