### https://docs.google.com/document/d/1v7fo6_cuZ1NuB1CwpwtmzeuVTyNQ0TEipcv8pY9-48Y/edit#heading=h.bfu1gnphpdfw

import math

def average():
    number_1 = int(input("Please enter number 1: "))
    number_2 = int(input("Please enter number 2: "))
    
    average = (number_1 + number_2) / 2
    
    print("The average is: ", average)
    
    
def future_value():
    aer = 3.5
    
    input_initial_amount = float(input("Input your original investment amount: "))
    input_years = int(input("Input the amount of years you are investing for: "))
    
    total_amount = input_initial_amount
    
    for i in range(1, input_years + 1):
        yearly_addition = total_amount * (aer / 100 + 1)
        print("Year ", i, " amount: £", format(yearly_addition, ".2f"))
        total_amount = yearly_addition
        
    print("Final Amount: £", format(total_amount, ".2f"))
    

def hypotenuse():
    length_1 = float(input("Enter the length of side 1: "))
    length_2 = float(input("Enter the length of side 2: "))
    
    output = length_1**2 + length_2**2
    output = math.sqrt(output)
    
    print("The hypotenuse is: ", format(output, "0.2f"))