### https://docs.google.com/document/d/1hJGicEI40OGYLNY30aWNOwLSUL5o9XQ5/edit#heading=h.gjdgxs

from graphix import *
from pract6 import calculate_grade, draw_coloured_eye
from pract5 import draw_brown_eye, distance_between_points
import time
import random

# Challenge #1 - Get Persons Name (With Validation)
def get_name():
    while True:
        input_name = input("Input | Please enter a valid name: ")
        
        if not input_name.isalpha():
            print("Error | Please only include alphabetic characters in your name.")
        else:
            break
        
    return input_name
        
        
# Challenge #2 - Working Traffic Light Sequence
def traffic_lights():
    win = Window("Challenge #2", 400, 400)
    
    red = Circle(Point(100, 50), 20)
    red.fill_colour = "red"
    red.draw(win)
    
    amber = Circle(Point(100, 100), 20)
    amber.fill_colour = "black"
    amber.draw(win)
    
    green = Circle(Point(100, 150), 20)
    green.fill_colour = "black"
    green.draw(win)
    
    while True:
        time.sleep(1)
        amber.fill_colour = "orange"
        
        time.sleep(2)
        red.fill_colour = "black"
        amber.fill_colour = "black"
        green.fill_colour = "green"
        
        time.sleep(5)
        amber.fill_colour = "orange"
        green.fill_colour = "black"
        
        time.sleep(2)
        red.fill_colour = "red"
        amber.fill_colour = "black"
        
        
# Challenge #3 - Grade Coursework (Using Pract6 Function)
def calculate_coursework():
    while True:
        # I would use a try except here for int(input(, but want to prove this method also.
        input_grade = input("Input | Please enter your coursework grade: ")
        
        if not input_grade.isdigit():
            print("Error | You must enter a full number as your grade. (Integer)")
        elif int(input_grade) < 0 or int(input_grade) > 20:
            print("Error | Your grade must be between 0 and 20 to assign a valid mark.")
        else:
            break
        
    print(f"Success | Your coursework grade is: {calculate_grade(int(input_grade))}")
        

# Challenge #4 - Calculating Order Price
def order_price():
    total_price = 0
    
    while True:
        input_unit_price = float(input("Input | Please enter the unit price of the product: "))
        input_quantity = int(input("Input | What is the quantity of this product: "))
        
        total_price += (input_unit_price * input_quantity)
        
        input_finished = input("Input | Would you like to add more items (y/n):")
        
        if input_finished.lower() == "y":
            print(f"Total Order Price: £{total_price:.2f}")
            break
        elif not input_finished.lower() == "n":
            print("Error | Invalid Input, Please enter 'Y' or 'N' to the question.")
            break
            
              
# Challenge #5 - Clickable Eye
def clickable_eye():
    win = Window("Challenge #5", 400, 400)
    
    draw_brown_eye(win, Point(200, 200), 100)
    
    while True:
        input_mouse = win.get_mouse()
        distance = distance = distance_between_points(input_mouse, Point(200, 200))
        
        if distance <= 30:
            print("pupil")
        elif distance <= 60:
            print("iris")
        elif distance <= 120:
            print("sclerca (white)")
        else:
            break
        
    win.close()


# Challenge #6 - Temperature Converter
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def temperature_converter():
    while True:
        input_conversion_type = input("Input | Would you like to convert to Fahrenheit or Celsius (f/c): ")

        if input_conversion_type.lower() == "f":
            input_celsius = float(input("Input | Please enter the temperature in Celsius: "))
            print(f"Success | The temperature in Fahrenheit is: {celsius_to_fahrenheit(input_celsius):.2f}")
            break
        elif input_conversion_type.lower() == "c":
            input_fahrenheit = float(input("Input | Please enter the temperature in Fahrenheit: "))
            print(f"Success | The temperature in Celsius is: {fahrenheit_to_celsius(input_fahrenheit):.2f}")
            break
        else:
            print("Error | Invalid Input, Please enter 'F' or 'C' to the question.")

    while True:
        input_another = input("Input | Would you like to convert another temperature (y/n): ")

        if input_another.lower() == "y":
            temperature_converter()
            break
        elif input_another.lower() == "n":
            break
        elif not input_another.lower() == "n":
            print("Error | Invalid Input, Please enter 'Y' or 'N' to the question.")


# Challenge #7 - Table Tennis Scorer
def table_tennis_scorer():
    win = Window("Challenge #7", 400, 400)

    player1_score = 0
    player2_score = 0

    player1_text = Text(Point(100, 200), "0")
    player1_text.draw(win)

    player2_text = Text(Point(300, 200), "0")
    player2_text.draw(win)

    centre_line = Line(Point(200, 0), Point(200, 400))
    centre_line.draw(win)

    while True:
        input_mouse = win.get_mouse()

        if input_mouse.x < 200:
            player1_score += 1
            player1_text.text = str(player1_score)
        elif input_mouse.x > 200:
            player2_score += 1
            player2_text.text = str(player2_score)

        if player1_score >= 11 and player1_score - player2_score >= 2:
            winner_text = Text(Point(100, 300), "Winner")
            winner_text.draw(win)
            break
        elif player2_score >= 11 and player2_score - player1_score >= 2:
            winner_text = Text(Point(300, 300), "Winner")
            winner_text.draw(win)
            break

    win.get_mouse()
    win.close()


# Challenge #8 - Guess The Number
def guess_the_number():
    attempts = 7
    number = random.randint(1, 100)

    for i in range(1, attempts + 1):
        input_guess = int(input("Input | Please guess the number between 1 and 100: "))

        if input_guess < number:
            print(f"Try Again | Your guess was too low. ({attempts - i} attempts remaining)")
        elif input_guess > number:
            print(f"Try Again | Your guess was too high. ({attempts - i} attempts remaining)")
        else:
            print(f"Success | You guessed the correct number after {i} attempts!")
            break

        if i == attempts:
            print(f"Failure | You have run out of attempts, the number was {number}.")
            break


# Challenge #9 - Clickable Box Of Eyes
def clickable_box_of_eyes(rows, columns):
    eye_radius = 50
    eye_radius_gap = eye_radius * 2

    win = Window("Challenge #9", (eye_radius_gap * columns + 100), (eye_radius_gap * rows + 100))

    outer_rectangle = Rectangle(Point(50, 50), Point(eye_radius_gap * columns + 50, eye_radius_gap * rows + 50))
    outer_rectangle.draw(win)

    position_text = Text(Point(int((eye_radius_gap * columns + 100) / 2), int(eye_radius_gap * rows + 75)), "Select an eye to obtain co-ordinates.")
    position_text.draw(win)

    for i in range(rows):
        for j in range(columns):
            draw_coloured_eye(win, Point(50 + (eye_radius_gap * j) + eye_radius, 50 + (eye_radius_gap * i) + eye_radius), eye_radius, "blue")

    while True:
        input_mouse = win.get_mouse()
        
        eye_found = False

        for i in range(rows):
            for j in range(columns):
                distance = distance_between_points(input_mouse, Point(50 + ((eye_radius * 2) * j) + eye_radius, 50 + ((eye_radius * 2) * i) + eye_radius))

                if distance <= eye_radius:
                    position_text.text = f"Eye at row {i + 1} column {j + 1}"
                    eye_found = True

        if (50 < input_mouse.x < eye_radius_gap * columns + 50) or not (50 < input_mouse.y < eye_radius_gap * rows + 50):
            if not eye_found:
                position_text.text = "Between eyes"
        else:
            win.close()
            break


# Challenge #10 - Find The Circle Game
def find_the_circle():
    win = Window("Challenge #10", 400, 400)

    number_of_games = 10
    guesses_per_round = 10
    starting_size = 50
    total_points = 0

    selection_box = Rectangle(Point(50, 50), Point(350, 350))
    selection_box.draw(win)

    round_number = Text(Point(200, 25), "")
    round_number.draw(win)

    hint_box = Text(Point(200, 375), "")
    hint_box.draw(win)

    for i in range(number_of_games):
        circle_guessed = False
        
        round_start_text = Text(Point(200, 180), f"Round {i + 1}")
        round_start_text.size = 20
        round_start_text.draw(win)

        round_text = Text(Point(200, 200), "Left click to start the round.")
        round_text.draw(win)
        
        win.get_mouse()
        
        round_start_text.undraw()
        round_text.undraw()
        
        random_x = random.randint((0 + starting_size * 2), 400 - (starting_size * 2))
        random_y = random.randint((0 + starting_size * 2), 400 - (starting_size * 2))

        last_guess = Point(0, 0)

        circle = Circle(Point(random_x, random_y), int(starting_size - i * (starting_size / 10)))
        circle.fill_colour = ""
        circle.outline_colour = ""
        circle.draw(win)

        for j in range(guesses_per_round):
            round_number.text = f"Round {i + 1} | Guess {j + 1}/{guesses_per_round}"
            
            input_mouse = win.get_mouse()

            if j > 0:
                distance_last = distance_between_points(last_guess, Point(random_x, random_y))
                distance_current = distance_between_points(input_mouse, Point(random_x, random_y))

                if distance_current < distance_last:
                    hint_box.text = "Getting closer"
                elif distance_current > distance_last:
                    hint_box.text = "Getting further away"

            last_guess = input_mouse

            distance = distance_between_points(input_mouse, Point(random_x, random_y))

            if distance <= circle.radius:
                total_points += guesses_per_round - j
                circle_guessed = True
                break
            
        hint_box.text = ""
        round_number.text = ""
            
        round_end_text = Text(Point(200, 180), f"Round {i + 1} Over")
        round_end_text.size = 20
        round_end_text.draw(win)
        
        if circle_guessed:
            round_text2 = Text(Point(200, 200), f"+ {guesses_per_round - j} Points")
        else:
            round_text2 = Text(Point(200, 200), "No Points")
            
        round_text2.draw(win)

        round_text3 = Text(Point(200, 220), "Left click to start the next round.")
        round_text3.draw(win)
        
        win.get_mouse()
        
        round_end_text.undraw()
        round_text2.undraw()
        round_text3.undraw()

        circle.undraw()

    selection_box.undraw()
    round_number.undraw()
    hint_box.undraw()

    game_over = Text(Point(200, 180), "Game Over")
    game_over.size = 20
    game_over.draw(win)

    points_text = Text(Point(200, 200), f"Total Points: {total_points}/{number_of_games * guesses_per_round}")
    points_text.draw(win)

    win.get_mouse()
    win.close()
