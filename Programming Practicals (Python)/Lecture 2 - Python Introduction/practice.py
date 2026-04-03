########################################################################################################################

# Writing Programs In Editor
def say_hello():
    print("Hello World")
    
def say_bye():
    print("Goodbye")
    
say_hello()
say_bye()

def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = 35.274 * kilos
    print("The weight in ounces is", ounces)

def count():
    for number in range(10):
        print("Number is now: ", number)
       
kilos_to_ounces()       
count()

########################################################################################################################
