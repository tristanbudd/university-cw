def sum_list(numbers, count):
    try:
        total = 0
        for i in range(count):
            total += numbers[i]
        return total
    except IndexError:
        print("The list does not have that many numbers. Please try again.")


def get_number():
    try:
        number = int(input("Enter a number: "))
        return number
    except ValueError:
        print("That is not a number. Please try again.")
        return get_number()


def main():
    numbers = []
    while True:
        print("Enter a non-negative number to add to the list.")
        print("Or enter a negative number to stop.")
        number = get_number()
        if number >= 0:
            numbers.append(number)
        else:
            break

    while True:
        print("Enter many numbers from the list would you like to sum up.")
        print("Or enter a negative number to stop.")
        count = get_number()
        if count >= 0:
            total = sum_list(numbers, count)
            print(f"The sum of the first {count} numbers is {total}")
        else:
            break


main()
