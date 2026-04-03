# Using https://www.programiz.com/dsa for info about sorting types.

import random

"""
Question #1

Implement Selection Sort:
Recall that in each iteration, Selection Sort finds the minimum or maximum in the
unsorted part of the array and moves it to the sorted part. Repeat until the array is
fully sorted.

O(n²) | In-place | Not stable
"""
def selection_sort(data):
    array_length = len(data)

    for i in range(array_length):
        min_index = i

        for j in range(i + 1, array_length):
            if data[j] < data[min_index]:
                min_index = j

        # Careful as need to do this at the exact same time to avoid overriding.
        data[i], data[min_index] = data[min_index], data[i]

    return data


"""
Question #2

Implement Insertion Sort:
Recall that in each iteration, Insertion Sort takes an element from the unsorted part,
finds its correct position in the sorted part, and inserts it. Repeat until the array is fully
sorted.

Best O(n), Worst O(n²) | In-place | Stable
"""
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j = j - 1

        data[j + 1] = key

    return data


"""
Question #3

Implement Bubble Sort:
Recall that in each iteration, Bubble Sort compares adjacent elements in the unsorted
part and swaps them if needed. After each pass, the last element of the unsorted part
is in its final position. Repeat until the array is fully sorted.

O(n²) | In-place | Stable
"""
def bubble_sort(data):
    for i in range(len(data)):
        for j in range(0, (len(data) - i) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data


"""
Question #4:

Implement Linear Search for an Array or List, sequentially checking each
element of the array or list to find a target value.

O(n) | Works on unsorted data
"""
def linear_search(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i

    return -1


"""
Question #5

Implement Binary Search for a Sorted Array (Iterative Method), halving the
search space at each step.

O(log n) | Sorted data only
"""
def binary_search(data, value):
    low = 0
    high = len(data) - 1

    while low <= high:
        middle = (low + high) // 2

        # print(data[low:high+1], low, middle, high)

        if data[middle] == value:
            return middle
        elif value > data[middle]:
            low = middle + 1
        else:
            high = middle - 1

    return low


"""
Question #6

Implement Binary Search for a Sorted Array (Recursive Method) and
compare its performance with the iterative method in Ex 5 using arbitrary
sorted arrays.

O(log n) | Sorted data only
"""
def binary_search_recursive(data, value, low, high):
    if high >= low:
        middle = low + (high - low) // 2

        if value == data[middle]:
            return middle
        elif value > data[middle]:
            return binary_search_recursive(data, value, middle + 1, high)
        else:
            return binary_search_recursive(data, value, low, middle - 1)
    else:
        return -1


"""
Question #7:

(Advanced) Implement Ternary Search for a Sorted Array, a method that
perform searching by dividing a sorted array into three equal parts instead of
two. Assess and compare its performance with binary search using arbitrary
sorted arrays.

O(log₃ n) | Sorted data only
"""
def ternary_search(arr, value):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == value:
            return mid1
        if arr[mid2] == value:
            return mid2

        if value < arr[mid1]:
            high = mid1 - 1
        elif value > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1

    return -1


def main():
    large_dataset = random.sample(range(1, 1001), 20)

    print("Original dataset:", large_dataset)

    # Sorting tests
    print("Selection Sort:", selection_sort(large_dataset.copy()))
    print("Insertion Sort:", insertion_sort(large_dataset.copy()))
    print("Bubble Sort:", bubble_sort(large_dataset.copy()))

    # Searching tests
    sorted_dataset = sorted(large_dataset)
    target = sorted_dataset[10]

    print("Sorted dataset:", sorted_dataset)
    print(f"Linear Search for {target}:", linear_search(sorted_dataset, target))
    print(f"Binary Search for {target}:", binary_search(sorted_dataset, target))
    print(f"Binary Search Recursive for {target}:", binary_search_recursive(sorted_dataset, target, 0, len(sorted_dataset) - 1))
    print(f"Ternary Search for {target}:", ternary_search(sorted_dataset, target))

if __name__ == "__main__":
    main()