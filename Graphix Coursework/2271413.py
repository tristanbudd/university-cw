# Programming - Course Work 3
# Student Number: up2271413
# Last Updated: 12/12/2024

from graphix import Window, Point, Rectangle, Circle, update
import time

# Collect the size option input from the user. (With Validation)
def get_size_option():
    size_options = ["5", "7", "9"]

    print("Size Options: " + ", ".join(size_options))

    while True:
        size_option = input("Input | Please enter the size of the board: ")

        if size_option.lower().strip(" ") in size_options:
            return int(size_option)
        else:
            print("Error | Invalid size option, please try again.")


# Collect 3 pattern colour inputs from the user. (With Validation)
def get_pattern_colours():
    colour_options = [
        "red", "green", "blue", "magenta", "orange", "purple"
    ]

    colour_choices = []

    print("Colour Options: " + ", ".join(colour_options))

    for i in range(3):
        while True:
            colour_choice = input(f"Input | Please enter a choice of colour ({i + 1}/3): ")

            if colour_choice.lower() in colour_options:
                if not colour_choice.lower() in colour_choices:
                    colour_choices.append(colour_choice.lower())
                    break
                else:
                    print("Error | Colour already chosen, please try again.")
            else:
                print("Error | Invalid colour option, please try again.")

    return colour_choices


# Draw a rectangle at the specified points with the specified colour.
def draw_rectangle(win, point_a, point_b, colour, outline=""):
    rectangle = Rectangle(point_a, point_b)
    rectangle.fill_colour = colour
    rectangle.outline_colour = outline
    rectangle.outline_width = 3
    rectangle.draw(win)
    return rectangle


# Draw both the blank, penultimate and final digit designs at the specified point.
def draw_patch(win, point, patch_type, colour):
    object_list = []

    if patch_type == 0:
        # Draw a coloured rectangle to represent the non-pattern spaces.
        rectangle = draw_rectangle(win, point, Point(point.x + 100, point.y + 100), colour, "")

        object_list.append(rectangle)
    elif patch_type == 1:
        # Draw the penultimate digit design.
        for i in range(5):
            for j in range(5):
                if (i + j) % 2 == 0:
                    fill_colour = "white"
                else:
                    fill_colour = colour

                point_a = Point(point.x + (i * 20), point.y + (j * 20))
                point_b = Point(point.x + 20 + (i * 20), point.y + 20 + (j * 20))

                rectangle = draw_rectangle(win, point_a, point_b, fill_colour, "")

                object_list.append(rectangle)

                if fill_colour == "white":
                    fill_colour = colour
                else:
                    fill_colour = "white"

                # If around the outer edge, add the circle details.
                if i == 0 or j == 0 or i == 4 or j == 4:
                    for k in range(2):
                        for l in range(2):
                            circle_position = Point(point.x + (i * 20) + (k * 10) + 5, point.y + (j * 20) + (l * 10) + 5)
                            circle = Circle(circle_position, 5)
                            circle.fill_colour = fill_colour
                            circle.outline_colour = ""
                            circle.draw(win)

                            object_list.append(circle)
    elif patch_type == 2:
        # Draw the final digit design.
        rectangle = draw_rectangle(win, point, Point(point.x + 100, point.y + 100), "white", "")

        object_list.append(rectangle)

        for i in range(10):
            point_a = Point(point.x + (i * 10), point.y + 90 - (i * 10))
            point_b = Point(point.x + 100, point.y + 100 - (i * 10))

            rectangle = draw_rectangle(win, point_a, point_b, colour, "")

            object_list.append(rectangle)

    return object_list


# Determine the colour of the grid patch based on the specified pattern. (Based on user input colours)
def determine_color(i, j, size_option, pattern_colours):
    if i == j or i + j == size_option - 1:
        return pattern_colours[0]
    elif i + 1 == j and i + j < size_option or i + j == size_option - 2 and i < j \
            or i + j < size_option and i < j:
        return pattern_colours[2]
    elif i + 1 == size_option - j and i + j > size_option or i + j == size_option and i > j \
            or i + j > size_option and i > j:
        return pattern_colours[2]
    else:
        return pattern_colours[1]


# Determine the pattern of the grid patch based on the specified position. (0 = Blank, 1 = Penultimate, 2 = Final)
def determine_pattern(i, j, size_option):
    if i == 0 or j == 0 or i == size_option - 1 or j == size_option - 1:
        return 0
    elif i == j or i + j == size_option - 1:
        return 2
    else:
        return 1


# Update the grid position with the specified pattern and colour.
def update_position(win, grid_positions, grid_x, grid_y, empty=False, pattern=0, colour=""):
    if empty:
        for object in grid_positions[(grid_x, grid_y)]["objects"]:
            object.undraw()

        grid_positions[(grid_x, grid_y)]["empty"] = True
        grid_positions[(grid_x, grid_y)]["objects"] = draw_patch(win, Point(grid_x * 100, grid_y * 100), 0, "white")
    else:
        if (grid_x, grid_y) in grid_positions and grid_positions[(grid_x, grid_y)]["empty"]:
            for object in grid_positions[(grid_x, grid_y)]["objects"]:
                object.undraw()

            grid_positions[(grid_x, grid_y)]["empty"] = False
            grid_positions[(grid_x, grid_y)]["pattern"] = pattern
            grid_positions[(grid_x, grid_y)]["color"] = colour
            grid_positions[(grid_x, grid_y)]["objects"] = draw_patch(win, Point(grid_x * 100, grid_y * 100), pattern, colour)

    return grid_positions


# Move a patch in the specified direction. (With Animation)
def move_patch(win, point, direction, grid_positions, window_size):
    grid_x = int(point.x // 100)
    grid_y = int(point.y // 100)

    new_point = None

    if direction == "up":
        if point.y - 100 >= 0:
            if (grid_x, grid_y - 1) in grid_positions and grid_positions[(grid_x, grid_y - 1)]["empty"]:
                new_point = Point(point.x, point.y - 100)
    elif direction == "down":
        if point.y + 100 < window_size:
            if (grid_x, grid_y + 1) in grid_positions and grid_positions[(grid_x, grid_y + 1)]["empty"]:
                new_point = Point(point.x, point.y + 100)
    elif direction == "left":
        if point.x - 100 >= 0:
            if (grid_x - 1, grid_y) in grid_positions and grid_positions[(grid_x - 1, grid_y)]["empty"]:
                new_point = Point(point.x - 100, point.y)
    elif direction == "right":
        if point.x + 100 < window_size:
            if (grid_x + 1, grid_y) in grid_positions and grid_positions[(grid_x + 1, grid_y)]["empty"]:
                new_point = Point(point.x + 100, point.y)

    if not new_point or grid_positions[(grid_x, grid_y)]["empty"]:
        return grid_positions

    # Clearing the new position and transferring the patch information.
    new_grid_x = int(new_point.x // 100)
    new_grid_y = int(new_point.y // 100)

    grid_positions[(new_grid_x, new_grid_y)]["empty"] = False
    grid_positions[(new_grid_x, new_grid_y)]["pattern"] = grid_positions[(grid_x, grid_y)]["pattern"]
    grid_positions[(new_grid_x, new_grid_y)]["color"] = grid_positions[(grid_x, grid_y)]["color"]
    for object in grid_positions[(new_grid_x, new_grid_y)]["objects"]:
        object.undraw()
    grid_positions[(new_grid_x, new_grid_y)]["objects"] = grid_positions[(grid_x, grid_y)]["objects"]

    # Animation of the patch moving to the new position.
    move_distance_x = int((new_point.x - point.x) / 4)
    move_distance_y = int((new_point.y - point.y) / 4)

    for _ in range(4):
        time.sleep(0.25)
        for object in grid_positions[(grid_x, grid_y)]["objects"]:
            object.move(move_distance_x, move_distance_y)

    # Setting old position to empty.
    grid_positions = update_position(win, grid_positions, grid_x, grid_y, True)

    # Redrawing the new position with the transferred patch.
    for object in grid_positions[(new_grid_x, new_grid_y)]["objects"]:
        object.draw(win)

    return grid_positions


def main():
    grid_positions = {}

    # Collecting user inputs.
    size_option = get_size_option()
    window_size = size_option * 100
    pattern_colours = get_pattern_colours()

    win = Window("Course Work 3 - UP2271413", window_size, window_size)

    # Creating the original grid with the specified patterns and colours.
    for i in range(size_option):
        for j in range(size_option):
            colour = determine_color(i, j, size_option, pattern_colours)
            pattern = determine_pattern(i, j, size_option)

            grid_positions[(i, j)] = {
                "color": colour,
                "pattern": pattern,
                "objects": draw_patch(win, Point(i * 100, j * 100), pattern, colour),
                "empty": False
            }

    # Challenge Feature - User interface to modify the grid.
    while True:
        grid_choice = win.get_mouse()

        grid_x = int(grid_choice.x // 100)
        grid_y = int(grid_choice.y // 100)

        if grid_x < size_option and grid_y < size_option:
            grid_position = Point(grid_x * 100, grid_y * 100)

            selection = draw_rectangle(win, grid_position, Point(grid_position.x + 100, grid_position.y + 100), "", "black")

            while True:
                # Collecting user inputs for the grid modification.
                action_choice = win.get_key()

                if action_choice.lower() == "x":
                    if (grid_x, grid_y) in grid_positions and not grid_positions[(grid_x, grid_y)]["empty"]:
                        grid_positions = update_position(win, grid_positions, grid_x, grid_y, True)
                elif action_choice.lower() == "up":
                    grid_positions = move_patch(win, grid_position, "up", grid_positions, window_size)
                elif action_choice.lower() == "down":
                    grid_positions = move_patch(win, grid_position, "down", grid_positions, window_size)
                elif action_choice.lower() == "left":
                    grid_positions = move_patch(win, grid_position, "left", grid_positions, window_size)
                elif action_choice.lower() == "right":
                    grid_positions = move_patch(win, grid_position, "right", grid_positions, window_size)
                elif action_choice.lower() == "1" or action_choice.lower() == "2" or action_choice.lower() == "3":
                    grid_positions = update_position(win, grid_positions, grid_x, grid_y, False, 1, pattern_colours[int(action_choice) - 1])
                elif action_choice.lower() == "4" or action_choice.lower() == "5" or action_choice.lower() == "6":
                    grid_positions = update_position(win, grid_positions, grid_x, grid_y, False, 2, pattern_colours[int(action_choice) - 4])
                elif action_choice.lower() == "7" or action_choice.lower() == "8" or action_choice.lower() == "9":
                    grid_positions = update_position(win, grid_positions, grid_x, grid_y, False, 1, pattern_colours[int(action_choice) - 7])
                elif action_choice.lower() == "escape":
                    selection.undraw()
                    break

                selection.undraw()
                selection = draw_rectangle(win, grid_position, Point(grid_position.x + 100, grid_position.y + 100), "", "black")


if __name__ == "__main__":
    main()
