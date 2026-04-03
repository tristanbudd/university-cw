import random

def get_inputs():
    while True:
        amount_of_steps = input("Input | How many steps should be taken? ")

        if amount_of_steps.isdigit():
            amount_of_steps = int(amount_of_steps)

            if amount_of_steps < 0:
                print("Error | Please enter a positive number.")
            else:
                return amount_of_steps

    return amount_of_steps


def take_a_walk(num_steps):
    point = int(num_steps / 2)
    step_tracker = [0] * num_steps

    for step in range(num_steps):
        random_direction = random.randint(0, 1)

        if random_direction == 1:
            if point + 1 >= num_steps:
                break

            point += 1
        else:
            if point - 1 < 0:
                break

            point -= 1

        step_tracker[point] += 1

    print("Square | Steps")

    for i in range(num_steps):
        print(f"{i + 1} | {step_tracker[i]}")


def main():
    take_a_walk(get_inputs())

if __name__ == "__main__":
    main()
