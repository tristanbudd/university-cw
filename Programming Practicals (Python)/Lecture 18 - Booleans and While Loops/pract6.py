### https://docs.google.com/document/d/1J8KJNBE8xnBrM2EENRD2RdPD6VaL-gHQ/edit#heading=h.gjdgxs

from graphix import *
from pract5 import distance_between_points
import math
import random

# Challenge #1 - Fast Food Order Pricing
def fast_food_order_price():
    price = float(input("How much is the sub-total for the order? "))
    
    if price < 20:
        price += 2.50
    
    print(f"The total price of your order is: £{price:.2f}")
    
    
# Challenge #2 - Temperature Suggestions
def what_to_do_today():
    temperature = float(input("Please input the current temperature (In Celsius): "))
    
    if temperature > 25:
        print("Suggestion: Swim in the sea.")
    elif 10 <= temperature <= 25:
        print("Suggestion: Shop at Gunwharf Quays.")
    elif temperature < 10:
        print("Suggestion: Watch a film at home.")
        
        
# Challenge #3 - Square Roots In Range
def display_square_roots(start, end):
    for i in range(start, end + 1):
        print(f"The square root of {i} is: {math.sqrt(i):.3f}")
    
        
# Challenge #4 - Calculating Letter Grade
def calculate_grade(mark):
    if 16 <= mark <= 20:
        return "A"
    elif 12 <= mark <= 15:
        return "B"
    elif 8 <= mark <= 11:
        return "C"
    elif 0 <= mark < 8:
        return "F"
    else:
        return "X"
    

# Challenge #5 - Draw Peas In Pod (With User Input)
def peas_in_a_pod():
    pea_amount = int(input("How many peas would you like to draw: "))
    
    win = Window("Challenge #5", (pea_amount * 100), 100)
    
    for i in range(pea_amount):
        pea = Circle(Point(50 + (100 * i), 50), 50)
        pea.fill_colour = "green"
        pea.outline_colour = ""
        pea.draw(win)
    
    win.get_mouse()
    win.close()
    

# Challenge #6 - Calculate Ticket Price (With User Input)
def ticket_price(distance, age):
    total_cost = 10.00 # Base Ticket Price
    total_cost += 0.15 * distance
    
    if age >= 60 or age <= 15:
        total_cost = total_cost * 0.6
    
    return total_cost


# Challenge #7 - Square Of Numbers
def numbered_square(n):
    for i in reversed(range(n)):
        for j in range(1, n + 1):
            print(i + j, end=" ")
        print("")        
    
    
# Challenge #8 - Draw Coloured Eye (With User Input & Validation)
def draw_circle(win, point, radius, colour):
    circle = Circle(point, radius)
    circle.fill_colour = colour
    circle.draw(win)
    
def draw_coloured_eye (win, point, radius, colour):
    draw_circle(win, point, int(radius), "white")
    draw_circle(win, point, int(radius / 2), colour)
    draw_circle(win, point, int(radius / 4), "black")
    
def eye_picker():
    accepted_colours = {"blue", "grey", "green", "brown"}
    
    x = int(input("Please enter the X co-ordinate of the eye: "))
    y = int(input("Please enter the Y co-ordinate of the eye: "))
    
    radius = int(input("Please the radius of the eye: "))
    
    print(accepted_colours)
    colour = input("Please input a colour from the above choices: ")
    
    if not (0 < x < 400) or not (0 < y < 400):
        print("Invalid Co-Ordinates. Both must be over 0 and under 400.")
        return
    elif colour.lower() not in accepted_colours:
        print("Invalid Colour, please select one from the list.")
        return
        
    win = Window("Challenge #8", 400, 400)
    
    draw_coloured_eye(win, Point(x, y), radius, colour)
    
    win.get_mouse()
    win.close()
    
    
# Challenge #9 - Drawing Pattern
def draw_patch_window():
    win = Window("Digram Number #3 (UP2271413)", 200, 200)

    for i in range(10):
        rectangle = Rectangle(Point(0 + (i * 10), 90 - (i * 10)), Point(100, 100 - (i * 10)))
        rectangle.fill_colour = "red"
        rectangle.outline_colour = ""
        rectangle.draw(win)

    win.get_mouse()
    win.close()


# Challenge #10 - Draw Patches (With Function Parameters)
def draw_patch(win, x, y, colour):
    for i in range(10):
        rectangle = Rectangle(Point(x + (i * 10), y + 90 - (i * 10)), Point(x + 100, y + 100 - (i * 10)))
        rectangle.fill_colour = colour
        rectangle.outline_colour = ""
        rectangle.draw(win)

def draw_patchwork():
    win = Window("Challenge #10", 300, 200)

    for i in range(3):
        draw_patch(win, 100 * i, 0, "blue")
        draw_patch(win, 100 * i, 100, "blue")

    win.get_mouse()
    win.close()


# Challenge #11 - Draw Coloured Eyes (With Colour & User Input)
def eyes_all_around():
    colour_list = {"blue", "grey", "green", "brown"}

    win = Window("Challenge #11", 500, 500)

    for i in range(30):
        mouse = win.get_mouse()

        colour = colour_list.pop()
        colour_list.add(colour)
        draw_coloured_eye(win, mouse, 30, colour)

    win.get_mouse()
    win.close()


# Challenge #12 - Archery Game
def archery_game():
    inner_circle_size = 50
    middle_circle_size = inner_circle_size * 2
    outer_circle_size = inner_circle_size * 3

    win = Window("Challenge #12", 400, 400)

    outer_circle = Circle(Point(200, 200), outer_circle_size)
    outer_circle.fill_colour = "blue"
    outer_circle.draw(win)

    middle_circle = Circle(Point(200, 200), middle_circle_size)
    middle_circle.fill_colour = "red"
    middle_circle.draw(win)

    inner_circle = Circle(Point(200, 200), inner_circle_size)
    inner_circle.fill_colour = "yellow"
    inner_circle.draw(win)

    total_points = 0

    for i in range(5):
        mouse = win.get_mouse()

        random_offset_x = random.randint(-10, 10)
        random_offset_y = random.randint(-10, 10)

        hit_position = Point(mouse.x + random_offset_x, mouse.y + random_offset_y)

        circle = Circle(hit_position, 5)
        circle.fill_colour = "black"
        circle.draw(win)

        distance = distance_between_points(hit_position, Point(200, 200))

        if distance <= inner_circle_size:
            total_points += 10
        elif distance <= middle_circle_size:
            total_points += 5
        elif distance <= outer_circle_size:
            total_points += 2

    points_text = Text(Point(200, 30), f"Total Points: {total_points}")
    points_text.draw(win)

    win.get_mouse()
    win.close()