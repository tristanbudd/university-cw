import random

def get_inputs():
    while True:
        input_amount = input("Input | How many times would you like to flip the coin? ")

        if input_amount.isdigit():
            input_amount = int(input_amount)

            if input_amount < 0:
                print("Error | Please enter a positive number.")
            else:
                return input_amount
        else:
            print("Error | Please enter a valid number.")


def simulate_flips(amount):
    heads = 0
    tails = 0

    for _ in range(amount):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1

    return heads, tails


def display_results(results):
    heads, tails = results
    total = heads + tails

    print(f"Heads {heads / total:.2f}, Tails {tails / total:.2f}")


def main():
    display_results(simulate_flips(get_inputs()))


if __name__ == "__main__":
    main()
