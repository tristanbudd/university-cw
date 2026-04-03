"""
Question #1

Develop both a recursive and an iterative algorithm to calculate the N-th
Fibonacci number, F(N). Compare their time complexities. The Fibonacci
sequence is defined as F(N+2) = F(N) + F(N+1), with F(1) = F(2) = 1. Note that
F(1) and F(2) are defined as 0 and 1 respectively in some literature.
"""
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

"""
Question #2

Create a recursive algorithm to find the greatest common divisor (GCD) of
two positive integers. If the integers are equal, the GCD is that integer.
Otherwise, the GCD is the GCD of their positive difference and the smaller
number.
"""
def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

"""
Question #3

Recall that during the division phase, Merge Sort divides the array into halves
recursively until each part has at most one element. Then merges the sorted halves
into a single sorted array until there is only one sorted group.
"""
def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_half = merge_sort(data[:mid])
    right_half = merge_sort(data[mid:])

    return merge(left_half, right_half)

"""
Question #4

Recall that Quick Sort recursively selects a pivot and partitions the array into two
groups based on comparisons with the pivot. The pivot is placed in its correct position,
and the process repeats until all subgroups contain at most one element.
"""
def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

"""
Question #5

Design an algorithm to check if an input string is a palindrome, that is a
string reads the same forwards and backwards (e.g., "hannah", "12321"). For
recursion, the base case is when the string has 1 or 2 characters (or none).
"""
def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

"""
Question #6

(Advanced) Develop an algorithm to solve a Sudoku puzzle given a valid,
partially filled grid. The goal is to fill the 9x9 grid such that every row, column,
and 3x3 subgrid contains all digits from 1 to 9. The input here is an arbitrary
valid Sudoku grid.
"""
def solve_sudoku(board):
    def is_valid(num, row, col):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    for num in range(1, 10):
                        if is_valid(num, r, c):
                            board[r][c] = num
                            if backtrack():
                                return True
                            board[r][c] = 0
                    return False
        return True

    backtrack()
    return board


def main():
    print("Fibonacci Iterative (10):", fibonacci_iterative(10))
    print("Fibonacci Iterative (20):", fibonacci_iterative(20))

    print("GCD (48, 18):", gcd(48, 18))
    print("GCD (56, 98):", gcd(56, 98))

    print("Merge Sort ([38, 27, 43, 3, 9, 82]):", merge_sort([38, 27, 43, 3, 9, 82]))
    print("Merge Sort ([5, 3, 8, 6, 2]):", merge_sort([5, 3, 8, 6, 2]))

    print("Quick Sort ([38, 27, 43, 3, 9, 82]):", quick_sort([38, 27, 43, 3, 9, 82]))
    print("Quick Sort ([5, 3, 8, 6, 2]):", quick_sort([5, 3, 8, 6, 2]))

    print("Is Palindrome ('hannah'):", is_palindrome('hannah'))
    print("Is Palindrome ('hello'):", is_palindrome('hello'))

    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    solved_board = solve_sudoku(sudoku_board)
    print("Solved Sudoku Board:")

    for row in solved_board:
        print(row)


if __name__ == "__main__":
    main()
