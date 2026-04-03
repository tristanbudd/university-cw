class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"MyPoint({self.x}, {self.y})"


def test_my_point():
    point_a = MyPoint(10, 25)
    point_b = MyPoint(50, 300)

    print("Position of point_a:", point_a)
    print("Position of point_b:", point_b)

    point_a.move(5, 5)
    print("New point a x axis: ", point_a.x)
    print("New point a y axis: ", point_a.y)

    point_b.x = 100
    print("New point b x axis: ", point_b.x)

    print("Position of point_a:", point_a)
    print("Position of point_b:", point_b)


class Square:
    def __init__(self, p1, side):
        self.p1 = p1
        self.side = side
        self.p2 = MyPoint(p1.x + side, p1.y + side)

        # Challenge #1 - Adding Instance Variables.
        self.outline_colour = "black"
        self.fill_colour = "white"

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    # Challenge #2 - Get Perimeter & Get Area Functions.
    def get_perimeter(self):
        return self.side * 4

    def get_area(self):
        return self.side ** 2

    # Challenge #3 - Get Centre Function.
    def get_centre(self):
        return MyPoint(self.p1.x + self.side // 2, self.p1.y + self.side // 2)

    def __str__(self):
        return f"Square({self.p1}, {self.side})"


def test_square():
    p = MyPoint(100, 50)
    square = Square(p, 50)

    # Challenge #1 - Add and Modify Instance Variables.
    colour_outline = "red"
    colour_fill = "blue"

    print(f"square's fill colour is {square.fill_colour}")
    print(f"square's outline colour is {square.outline_colour}")

    print(f"Changing squares outline colour to {colour_outline} ...")
    square.outline_colour = colour_outline

    print(f"square's outline colour is {square.outline_colour}")

    print(f"Changing squares fill colour to {colour_fill} ...")
    square.fill_colour = colour_fill

    print(f"square's fill colour is {square.fill_colour}")

    # Challenge #2 - Get Perimeter & Get Area Functions.
    print(f"square's perimeter is {square.get_perimeter()}")
    print(f"square's area is {square.get_area()}")

    # Challenge #3 - Get Centre Function.
    print(f"square's centre is {square.get_centre()}")


# Challenge #4 - MyCircle Class.
class MyCircle:
    def __init__(self, point, radius):
        self.centre = point
        self.radius = radius

        self.outline_colour = "black"
        self.fill_colour = "white"

    def move(self, dx, dy):
        self.centre.move(dx, dy)

    def __str__(self):
        return f"Circle({self.centre}, {self.radius})"


def test_circle():
    p = MyPoint(100, 100)
    circle = MyCircle(p, 50)

    print(circle)

    colour_outline = "orange"
    colour_fill = "red"
    move_x, move_y = 200, 200

    print(f"circle's fill colour is {circle.fill_colour}")
    print(f"circle's outline colour is {circle.outline_colour}")

    print(f"Changing circles outline colour to {colour_outline} ...")
    circle.outline_colour = colour_outline

    print(f"circle's outline colour is {circle.outline_colour}")

    print(f"Changing circles fill colour to {colour_fill} ...")
    circle.fill_colour = colour_fill

    print(f"circle's fill colour is {circle.fill_colour}")

    print(f"circle's current centre is {circle.centre}")

    print(f"Moving circles centre point to: {move_x}, {move_y}")
    circle.move(move_x, move_y)

    print(f"circle's current centre is {circle.centre}")


# Challenge #5 - Bank Account Class.
class BankAccount:
    def __init__(self, name):
        self.holder_name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def __str__(self):
        return f"Bank account for {self.holder_name} has £{self.balance}"


def test_bank_account():
    account = BankAccount("Alicia Keys")

    print(f"Account holder's name is {account.holder_name}")
    print(f"Account balance is £{account.balance}")

    print("Depositing £100 ...")
    account.deposit(100)
    print(account)

    print("Withdrawing £50 ...")
    account.withdraw(50)
    print(account)

    print("Withdrawing £100 ...")
    account.withdraw(100)
    print(account)


# Challenge #6 - Hotel Room Class.
class HotelRoom:
    def __init__(self, room_number):
        self.room_number = room_number
        self.guest_name = ""

    def check_in(self, guest_name):
        self.guest_name = guest_name

    def check_out(self):
        self.guest_name = ""

    def is_occupied(self):
        return self.guest_name != ""

    def __str__(self):
        if self.is_occupied():
            return f"Room number {self.room_number} is occupied by {self.guest_name}"
        else:
            return f"Room number {self.room_number} is vacant"


def test_hotel_room():
    room = HotelRoom(101)

    print(room)
    room.check_in("Winston")
    print(room)
    room.check_out()
    print(room)


# Challenge #7 - Grade Book Class.
class GradeBook:
    def __init__(self):
        self.grades = {}

    def add_grade(self, module_name, grade):
        self.grades[module_name] = grade

    def remove_grade(self, module_name):
        if module_name in self.grades:
            del self.grades[module_name]

    def get_grade(self, module_name):
        if module_name not in self.grades:
            return "No grade found for this module."
        else:
            return self.grades[module_name]

    def get_grade_average(self):
        if len(self.grades) == 0:
            return 0
        else:
            return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        if len(self.grades) == 0:
            return "No grades have been added yet."
        else:
            grades = "Here are your grades: "

            for module, grade in self.grades.items():
                grades += f"{module}: {grade}"
                if module != list(self.grades.keys())[-1]:
                    grades += ", "

            return grades


def test_grade_book():
    grade_book = GradeBook()

    print(grade_book)
    print("Adding grades ...")
    grade_book.add_grade("Maths", 90)
    grade_book.add_grade("English", 80)
    print(grade_book)

    print(f"Average grade is {grade_book.get_grade_average()}")
    print(f"Maths grade is {grade_book.get_grade('Maths')}")
    print(f"English grade is {grade_book.get_grade('English')}")

    print("Removing Maths grade ...")
    grade_book.remove_grade("Maths")
    print(grade_book)


# Challenge #8 - Smartphone Class.
class SmartPhone:
    def __init__(self, colour, memory):
        self.colour = colour
        self.memory = memory
        self.apps = ["Phone", "Messages", "Camera"]

        self.apps[0] = self.apps[0] + " (current)"

    def install_app(self, app_name):
        if app_name not in self.apps:
            self.apps.append(app_name)

    def uninstall_app(self, app_name):
        if app_name in self.apps:
            self.apps.remove(app_name)

    def switch_app(self):
        if len(self.apps) > 1:
            current_index = 0

            for app in self.apps:
                if app.rfind(" (current)"):
                    self.apps[current_index] = app.replace(" (current)", "")
                    self.apps[current_index + 1] += " (current)"
                    break

                current_index += 1

    def __str__(self):
        output = f"A {self.colour} smartphone with {self.memory} GB of memory\n\nInstalled apps:\n"
        for app in self.apps:
            output += f"- {app}\n"

        if len(self.apps) < 1:
            output += "- None\n"

        return output


def test_smartphone():
    phone = SmartPhone("black", 128)

    print(phone)

    print("Installing Spotify app ...")
    phone.install_app("Spotify")
    print(phone)

    print("Switching to the second app ...")
    phone.switch_app()
    print(phone)

    print("Uninstalling Spotify app ...")
    phone.uninstall_app("Spotify")
    print(phone)


def main():
    while True:
        choice = int(input("Which challenge would you like to run? (1-8) (9 - To Exit) "))

        if 1 <= choice <= 2:
            test_square()
        elif choice == 3:
            test_square()
        elif choice == 4:
            test_circle()
        elif choice == 5:
            test_bank_account()
        elif choice == 6:
            test_hotel_room()
        elif choice == 7:
            test_grade_book()
        elif choice == 8:
            test_smartphone()
        elif choice == 9:
            break
        else:
            print("Error | Invalid choice, please try again. (Number between 1 & 9)")


if __name__ == "__main__":
    main()
