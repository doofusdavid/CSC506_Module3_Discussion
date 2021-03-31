from time import process_time
import random


def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        j = i

        # Insert num_list[i] into sorted part
        # stopping once num_list[i] in correct position
        while j > 0 and num_list[j] < num_list[j - 1]:
            # Swap num_list[j] and num_list[j - 1]
            temp = num_list[j]
            num_list[j] = num_list[j - 1]
            num_list[j - 1] = temp
            j -= 1


def partition(numbers, start_index, end_index):
    # Select the middle value as the pivot.
    midpoint = start_index + (end_index - start_index) // 2
    pivot = numbers[midpoint]

    # "low" and "high" start at the ends of the list segment
    # and move towards each other.
    low = start_index
    high = end_index

    done = False
    while not done:
        # Increment low while numbers[low] < pivot
        while numbers[low] < pivot:
            low = low + 1

        # Decrement high while pivot < numbers[high]
        while pivot < numbers[high]:
            high = high - 1

        # If low and high have crossed each other, the loop
        # is done. If not, the elements are swapped, low is
        # incremented and high is decremented.
        if low >= high:
            done = True
        else:
            temp = numbers[low]
            numbers[low] = numbers[high]
            numbers[high] = temp
            low = low + 1
            high = high - 1

    # "high" is the last index in the left segment.
    return high


def quicksort(numbers, start_index, end_index):
    # Only attempt to sort the list segment if there are
    # at least 2 elements
    if end_index <= start_index:
        return

    # Partition the list segment
    high = partition(numbers, start_index, end_index)

    # Recursively sort the left segment
    quicksort(numbers, start_index, high)

    # Recursively sort the right segment
    quicksort(numbers, high + 1, end_index)


# Main program to test the quicksort algorithm.
numbers = [12, 18, 3, 7, 32, 14, 91, 16, 8, 57]
print('UNSORTED:', numbers)
q_time_start = process_time()
quicksort(numbers, 0, len(numbers)-1)
q_time_stop = process_time()
print('SORTED:', numbers)
print('Elapsed Time: ', q_time_stop - q_time_stop)
