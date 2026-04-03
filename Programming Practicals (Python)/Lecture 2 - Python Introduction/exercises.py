# Challenge #1 - Display Name
def say_name():
    print("Tristan")
    

# Challenge #2 - Function To Display Text
def say_hello_2():
    print("Hello")
    print("world")


# Challenge #3 - Convert USD to GBP
def dollars_to_pounds():
    exchange_rate = 1.35
    
    input_usd = float(input("Amount in USD: "))
    output_gbp = input_usd * exchange_rate
    
    print("Amount in GBP: ", output_gbp)


# Challenge #4 - Calculate Sum & Difference
def sum_and_difference():
    input_number_one = float(input("Please input the first number: "))
    input_number_two = float(input("Please input the second number: "))
    
    output_sum = input_number_one + input_number_two
    output_difference = input_number_one - input_number_two
    
    print("Sum: ", output_sum)
    print("Difference: ", output_difference)


# Challenge #5 - Calculate Change
def change_counter():
    input_one_pence = int(input("How many 1p coins do you have? "))
    input_two_pence = int(input("How many 2p coins do you have? "))
    input_five_pence = int(input("How many 5p coins do you have? "))
    
    total_change = input_one_pence + (input_two_pence * 2) + (input_five_pence * 5)
    
    print("Total Change: ", total_change)


# Challenge #6 - Display Ten Hello's
def ten_hellos():
    print("Hello World\n" * 10)


# Challenge #7 - Zoom Zoom
def zoom_zoom():
    input_zoom_amount = int(input("Please input an amount of Zoom's: "))
    
    for i in range(1, input_zoom_amount + 1):
        print("zoom ", i)


# Challenge #8 - Count To Number
def count_to():
    input_count_to = int(input("Input a number to count to: "))
    
    for i in range(1, input_count_to + 1):
        print(i)


# Challenge #9 - Count From To Number
def count_from_to():
    input_count_from = int(input("Input a number to start counting from: "))
    input_count_to = int(input("Input a number to count up to: "))
    
    for i in range(input_count_from, input_count_to + 1):
        print(i)


# Challenge #10 - Table Of Kilogram Weights

# def weights_table():
#     conversion_rate = 35.274
#     
#     weight_table_kg = []
#     weight_table_ounces = []
#     
#     for i in range(10, 100 + 1, 10):
#         weight_table_kg.append(i)
#         weight_table_ounces.append(i * conversion_rate)
#         
#     for i in range(10):
#         print("KG: ", weight_table_kg[i], " | Ounces: ", weight_table_ounces[i])

# New Version (Without Lists)
def weights_table():
    conversion_rate = 35.274
    
    for i in range(10, 100 + 1, 10):
        print("KG: ", i, " | Ounces: ", i * conversion_rate)


# Challenge #11 - Calculate Future Value Of Investment
def future_value():
    aer = 3.5
    
    input_initial_amount = float(input("Input your original investment amount: "))
    input_years = int(input("Input the amount of years you are investing for: "))
    
    total_amount = input_initial_amount
    
    for i in range(1, input_years + 1):
        yearly_addition = total_amount * (aer / 100 + 1)
        print("Year ", i, " addition: ", yearly_addition)
        total_amount += yearly_addition
        
    print("Final Amount: ", total_amount)