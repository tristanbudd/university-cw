### https://docs.google.com/document/d/16QrG4B9OhdtRUchmyXqJsTu41zvY1xe4/edit?pli=1#heading=h.gjdgxs

from graphix import *

# Challenge #1 - Personal Greeting
def personal_greeting():
    name = input("What is your name? ")
    print(f"Hello {name}, nice to see you!")
   
    
# Challenge #2 - Formal Name Formatting
def formal_name():
    first_name = input("What is your first name? ")
    last_name = input("What is your last / family name? ")
    
    print(f"{first_name[0]}. {last_name}")
    
    
# Challenge #3 - Kilos to Ounces Rework
def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = 35.274 * kilos
    print(f"{kilos} kilos is equal to {ounces:.2f} ounces.")


# Challenge #4 - Generate Email Address
def generate_email():
    first_name = input("What is your first name? ")
    last_name = input("What is your last / family name? ")
    entry_year = input("What year did you start University? ")
    
    print(f"Generated Email: {last_name[:4]}.{first_name[0]}.{entry_year[-2:]}@myport.ac.uk")
    
    
# Challenge #5 - Corresponding Grades
def grade_test():
    grade_list = "FFFFFFDCBAA"

    grade = input("Enter the students' grade: ")

    print(f"Grade: {grade_list[int(grade)]}")
    
    
# Challenge #6 - Display Graphics Letters
def graphic_letters():
    word = input("Enter a word to display: ")
    
    win = Window("Challenge #6", 400, 400)
    
    for char in word:
        mouse_pos = win.get_mouse()
        
        character = Text(mouse_pos, char)
        character.size = 16
        character.draw(win)


# Challenge #7 - Singing A Song
def sing_a_song():
    song_word = input("What word would you like the song to be about? ")
    song_line_amount = int(input("How many lines should the song be? "))
    song_line_length = int(input("How many times should the word repeat on each line? "))
    
    for i in range(song_line_amount):
        print((song_word + " ") * song_line_length)
        
        
# Challenge #8 - Exchange Table (Euros to Pounds)
def exchange_table():
    convert_amount = 20
    conversion_rate = 0.83
    
    print("Euros | Pounds")

    for i in range(1, convert_amount + 1):
        print(f"{i:.2f} | {(i * conversion_rate):.2f}")


# Challenge #9 - Capitalise Initial Letters
def make_initialism():
    phrase = input("Enter a phrase you want to make initialism: ")
    words = phrase.split(" ")

    for word in words:
        print(word[0].upper(), end="")


# Challenge #10 - Capitalise File Contents
def file_in_caps():
    file_name = input("Please enter the name of the file (with format): ")

    f = open(file_name, "r")
    contents = f.read()
    f.close()

    print(contents.upper())


# Challenge #11 - Calculate Total Spending (From File)
def total_spending():
    file_name = "spending.txt"
    spending = 0

    f = open(file_name, "r")
    lines = f.readlines()
    f.close()

    for row in lines:
        row = row.split("\n")
        spending += float(row[0])

    print(f"Total spending: £{spending:.2f}")


# Challenge #12 - Convert Name To Numbers
def name_to_number():
    name = input("Please enter your name: ")
    total = 0

    for char in name:
        total += (ord(char) - 64)

    print(f"Total: {total}")


# Challenge #13 - Rainfall Chart
def rainfall_chart():
    file_name = "rainfall.txt"

    f = open(file_name, "r")
    lines = f.readlines()
    f.close()

    for row in lines:
        row = row.split(" ")
        print(row[0], end=" ")

        for i in range(int(row[1])):
            print("*", end="")

        print()


# Challenge #13b - Rainfall Chart (With Graphics)
def rainfall_graphics():
    file_name = "rainfall.txt"

    f = open(file_name, "r")
    lines = f.readlines()
    f.close()

    text_x = 65
    text_y = 50
    gap = 20

    win = Window("Rainfall Chart", 560, 265)

    count = 0
    for row in lines:
        row = row.split(" ")

        message = Text(Point(text_x, text_y + (gap * count)), row[0])
        message.draw(win)

        for i in range(int(row[1])):
            bar = Rectangle(Point(text_x + 50, text_y + (gap * count) - 10), Point(text_x + 50 + 10, text_y + (gap * count) + 10))
            bar.fill_colour = "black"
            bar.draw(win)
            bar.move(i * 10, 0)

        count += 1


# Challenge #14 - Rainfall In Inches
def rainfall_in_inches():
    file_name = "rainfall.txt"

    f = open(file_name, "r")
    lines = f.readlines()
    f.close()

    for row in lines:
        row = row.split(" ")
        print(f"{row[0]}: {int(row[1]) * 0.0393701:.2f} inches")


# Challenge #15 - UNIX wc Command
def wc():
    file_name = input("Please enter the name of the file (with format): ")

    f = open(file_name, "r")
    lines = f.readlines()
    f.close()

    line_count = len(lines)
    word_count = 0
    char_count = 0

    for row in lines:
        words = row.split(" ")
        word_count += len(words)
        char_count += len(row)

    print(f"{line_count} {word_count} {char_count} {file_name}")
