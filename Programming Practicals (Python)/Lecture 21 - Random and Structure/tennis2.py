from random import random

def get_inputs():
    while True:
        point_win_probability = input("Input | Probability of winning each point: ")

        if 0 <= float(point_win_probability) <= 1:
            point_win_probability = float(point_win_probability)
            break
        else:
            print("Error | Please enter a valid probability.")

    while True:
        number_of_sets = input("Input | Sets to simulate: ")

        if number_of_sets.isdigit() and int(number_of_sets) > 0:
            number_of_sets = int(number_of_sets)
            break
        else:
            print("Error | Please enter a positive number.")

    return point_win_probability, number_of_sets


def simulate_sets(point_win_probability, number_of_sets):
    sets_won_player = 0
    sets_won_opponent = 0
    for _ in range(number_of_sets):
        games_player, games_opponent = simulate_set(point_win_probability)
        if games_player > games_opponent:
            sets_won_player += 1
        else:
            sets_won_opponent += 1
    return sets_won_player, sets_won_opponent


def simulate_set(point_win_probability):
    games_player, games_opponent = 0, 0
    while not set_over(games_player, games_opponent):
        points_player, points_opponent = simulate_game(point_win_probability)
        if points_player > points_opponent:
            games_player += 1
        else:
            games_opponent += 1
    return games_player, games_opponent


def simulate_game(point_win_probability):
    points_player, points_opponent = 0, 0
    while not game_over(points_player, points_opponent):
        if random() < point_win_probability:
            points_player += 1
        else:
            points_opponent += 1
    return points_player, points_opponent


def game_over(points_player, points_opponent):
    return (points_player >= 4 or points_opponent >= 4) and abs(points_player - points_opponent) >= 2


def set_over(games_player, games_opponent):
    return (games_player >= 6 or games_opponent >= 6) and abs(games_player - games_opponent) >= 2


def print_summary(sets_won_player, sets_won_opponent, number_of_sets):
    proportion_player = sets_won_player / number_of_sets
    proportion_opponent = sets_won_opponent / number_of_sets
    
    print(f"Sets won by player: {sets_won_player}, proportion: {proportion_player:.2f}")
    print(f"Sets won by opponent: {sets_won_opponent}, proportion: {proportion_opponent:.2f}")


def main():
    point_win_probability, number_of_sets = get_inputs()
    sets_won_player, sets_won_opponent = simulate_sets(point_win_probability, number_of_sets)
    print_summary(sets_won_player, sets_won_opponent, number_of_sets)


if __name__ == "__main__":
    main()
