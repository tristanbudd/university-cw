### https://docs.google.com/document/d/1kWsGOUWUT1zaJGyBsW6oJPCBhVzwpwAw/edit#heading=h.gjdgxs

import math

# Challenge #1 - Calculate Speed
def speed_calculator():
    distance = int(input("Please enter the distance travelled (in Kilometers): "))
    duration = int(input("How long was the journey (in Hours): "))
    
    average_speed = distance / duration
    
    print("The average speed of the journey was: ", average_speed, "km/h")
    

# Challenge #2 - Calculate Circumference Of Circle
def circumference_of_circle():
    radius = float(input("What is the radius of the circle: "))
    
    circumference = 2 * math.pi * radius
    
    print("The circumference of the circle is: ", format(circumference, "0.2f"))
    

# Challenge #3 - Calculate Area Of Circle
def area_of_circle():
    radius = float(input("What is the radius of the circle: "))
    
    area = math.pi * radius**2
    
    print("The area of the circle is: ", format(area, "0.2f"))
    

# Challenge #4 - Cost Of Pizza By Diameter
def cost_of_pizza():
    cost_of_ingredients = 3.5
    
    diameter = float(input("What is the diameter of the pizza? (in Centermeters): "))
    
    area = math.pi * (diameter / 2)**2
    total_cost = area * (cost_of_ingredients/100)
    
    print("Total cost of pizza: £", format(total_cost, "0.2f"))
    

# Challenge #5 - Calculate Slope Of Line
def slope_of_line():
    x_1 = int(input("Please input x value 1 (x_1): "))
    y_1 = int(input("Please input y value 1 (y_1): "))
    x_2 = int(input("Please input x value 2 (x_2): "))
    y_2 = int(input("Please input y value 2 (y_2): "))

    slope = (y_2 - y_1) / (x_2 - x_1)
    
    print("The slope of the line is: ", slope)
    
    
# Challenge #6 - Distance Between Points
def distance_between_points():
    x_1 = int(input("Please input x value 1 (x_1): "))
    y_1 = int(input("Please input y value 1 (y_1): "))
    x_2 = int(input("Please input x value 2 (x_2): "))
    y_2 = int(input("Please input y value 2 (y_2): "))

    distance = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    
    print("The distance between the two points is: ", format(distance, "0.2f"))


# Challenge #7 - Calculate Distance Travelled & Fuel Consumption
def travel_statistics():
    fuel_efficiency = 5
    
    average_speed = float(input("What is your average speed? (in km/h): "))
    duration = int(input("How long was your car journey? (in Hours): "))
    
    distance_travelled = average_speed * duration
    fuel_used = distance_travelled / fuel_efficiency
    
    print("Distance Travelled: ", distance_travelled, "km")
    print("Fuel Used: ", fuel_used, " litres")
    

# Challenge #8 - Calculate Sum Of Squared Numbers
def sum_of_squares():
    n = int(input("Enter a number to count up to (in squares): "))
    
    result = 0
    
    for i in range(1, n + 1):
        result += i**2
        
    print("The sum of all of the squares is: ", result)


# Challenge #9 - Average Of Numbers (User Choice)
def average_of_numbers():
    input_amount = int(input("How many numbers would you like to calculate the average of? "))

    total_amount = 0

    for i in range(1, input_amount + 1):
        number = int(input(f"Please input a number {i}: "))

        total_amount += number

    average = total_amount / input_amount

    print("The average of the numbers is: ", average)


# Challenge #10 - Fibonacci Sequence
def fibonacci():
    n = int(input("What number of the Fibonacci Sequence would you like to view? "))

    current_number = 0
    next_number = 1

    for i in range(1, n):
        current_number, next_number = next_number, current_number + next_number

    print(f"The {n}th number in the Fibonacci Sequence is: ", next_number)

    
# Challenge #11 - Calculate Change
def select_coins():
    pence_input = int(input("How much money would you like to convert? (In Pence): "))

    total_remaining = pence_input

    two_pounds = pence_input // 200
    total_remaining = pence_input - (two_pounds * 200)

    one_pound = total_remaining // 100
    total_remaining = total_remaining - (one_pound * 100)

    fifty_pence = total_remaining // 50
    total_remaining = total_remaining - (fifty_pence * 50)

    twenty_pence = total_remaining // 20
    total_remaining = total_remaining - (twenty_pence * 20)

    ten_pence = total_remaining // 10
    total_remaining = total_remaining - (ten_pence * 10)

    five_pence = total_remaining // 5
    total_remaining = total_remaining - (five_pence * 5)

    two_pence = total_remaining // 2
    total_remaining = total_remaining - (two_pence * 2)

    one_pence = total_remaining // 1
    total_remaining = total_remaining - one_pence

    print(two_pounds, "x £2, ", one_pound, "x £1, ", fifty_pence, "x 50p, ", twenty_pence, "x 20p, ", ten_pence, "x 10p, ", five_pence, "x 5p, ", two_pence, "x 2p, ", one_pence, "x 1p Coins")


# Challenge #12B - Bonus Lists Version
def select_coins_2():
    coin_types = [
        "£2", 200,
        "£1", 100,
        "50p", 50,
        "20p", 20,
        "10p", 10,
        "5p", 5,
        "2p", 2,
        "1p", 1
    ]

    pence_input = int(input("How much money would you like to convert? (In Pence): "))

    total_remaining = pence_input

    coins = []

    for i in range(1, len(coin_types), 2):
        coin_amount = total_remaining // coin_types[i]
        total_remaining -= coin_amount * coin_types[i]
        coins.append(f"{coin_amount} x {coin_types[i - 1]}")

    print(*coins, sep=", ")

select_coins_2()
