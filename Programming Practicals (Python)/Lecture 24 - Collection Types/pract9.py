from graphix import *
import math

# Challenge #1 - Formatted Date
def display_date(day, month, year):
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    print(f'{day} {month_list[month-1]} {year}.')


# Challenge #2 - Word Lengths (List Input)
def word_lengths(words):
    for i in range(len(words)):
        print(f'{words[i]} {len(words[i])}')


# Challenge #3 - Draw Hexagon (Based on User Inputs)
def draw_hexagon():
    win = Window("Challenge #3", 400, 400)

    hexagon_points = []

    for i in range(6):
        hexagon_points.append(win.get_mouse())

    hexagon = Polygon(hexagon_points)
    hexagon.fill_colour = "red"
    hexagon.outline_colour = ""
    hexagon.draw(win)

    win.get_mouse()
    win.close()


# Challenge #4 - Collect Marks For Test
def test_marks():
    marks = [0] * 6
    i = 0

    while True:
        mark = int(input(f"Input | Enter a mark 0-5 for student {i + 1} or type -1 to exit: "))

        if mark < -1 or mark > 5:
            print("Error | Invalid mark. Please enter a mark between 0 and 5.")
        elif mark == -1:
            break
        else:
            marks[mark] += 1
            i += 1

    for i in range(6):
        print(f"{marks[i]} student(s) got {i} marks")


# Challenge #5 - Draw Bar Chart (Based On List)
def draw_bar_chart(data):
    max_height = max(data)

    for row in range(1, max_height + 1):
        for value in data:
            if value >= row:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()


# Challenge #6 - Unique Module List
def unique_modules(data):
    unique_modules_list = []

    for module in data:
        if module not in unique_modules_list:
            print(module)
            unique_modules_list.append(module)


# Challenge #7 - Street (Worksheet 8) Rework
# Done externally: street2.py


# Challenge #8 - Distance Between Points Rework
def distance_between_points(point1, point2):
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)


# Challenge #9 - Count Individual Characters
def count_characters():
    text = input("Input | Enter a sentence: ")
    character_count = {}

    for character in text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    for character, count in character_count.items():
        print(f"{count} occurrences of '{character}'")


# Challenge #10 - Traced Walk (Worksheet 8) Rework
# Done externally: traced_walk.py


# Challenge #11 - Recommended Friends
def recommend_friends():
    my_friends = input("Enter your friends: ").split(", ")
    friends_of_all = []

    for friend in my_friends:
        their_friends = set(input(f"Enter {friend}'s friends: ").split(", "))

        if not friends_of_all:
            friends_of_all = their_friends
        else:
            friends_of_all &= their_friends

    recommended_friends = friends_of_all - set(my_friends)
    print("Recommended new friends for you: ", ", ".join(recommended_friends))


# Challenge #12 - 2D Traced Walk (Worksheet 10) Rework
# Done externally: traced_walk2d.py

