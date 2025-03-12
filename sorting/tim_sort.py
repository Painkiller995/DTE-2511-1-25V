"""
This module implements the Tim Sort algorithm.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""


def insertion_sort(arr: list[int], start: int, end: int) -> None:
    """
    Sort the list using the Insertion Sort algorithm.

    Args:
        - arr: The list to be sorted.
        - start: The starting index of the partition.
        - end: The ending index of the partition.

    Returns:
        None: The list is sorted in-place.
    """
    for i in range(start + 1, end + 1):
        current_element = arr[i]
        j = i - 1

        while j >= start and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_element


def merge_sort(arr: list[int], start: int, middle: int, end: int) -> None:
    """
    Sort the list using the Merge Sort algorithm.

    Args:
        - arr (list[int]): The list to be sorted.
        - start (int): The starting index of the partition.
        - middle (int): The middle index of the partition.
        - end (int): The ending index of the partition.

    Returns:
        None: The list is sorted in-place.
    """

    if start >= end:
        return

    # Divide the array into two halves
    left_half = arr[start : middle + 1]
    right_half = arr[middle + 1 : end + 1]

    # Merge the two halves
    merge(arr, left_half, right_half, start)


def merge(arr: list[int], left_half: list[int], right_half: list[int], start: int) -> None:
    """
    Merge two halves of the array.

    Args:
        - arr (list[int]): The list to be sorted.
        - left_half (list[int]): The left half of the list.
        - right_half (list[int]): The right half of the list.
        - start (int): The starting index of the partition.
    """

    i = j = 0
    k = start
    # Copy data to temp arrays left_half[] and right_half[]
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1


def sort(arr: list[int]) -> None:
    """
    Sort the list using the Tim Sort algorithm.

    Args:
        - arr: The list to be sorted.
    """
    min_run = 4
    number_of_elements = len(arr)

    # Sort individual sub arrays of size min_run
    for i in range(0, number_of_elements, min_run):
        end = min((i + min_run - 1), number_of_elements - 1)
        insertion_sort(arr, i, end)

    # Merge the sorted sub arrays
    size = min_run
    while size < number_of_elements:
        for start in range(0, number_of_elements, 2 * size):
            middle = min(number_of_elements - 1, start + size - 1)
            end = min((start + 2 * size - 1), number_of_elements - 1)
            merge_sort(arr, start, middle, end)
        size *= 2


if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {array}")
    sort(array)
    print(f"Sorted array: {array}")
