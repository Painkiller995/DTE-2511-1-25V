"""
This module implements the Quick Sort algorithm with an improved pivot selection strategy.

Time Complexity: O(n^2) in the worst case, O(n log n) on average.

This implementation chooses the pivot as the median of three (first, middle, last elements),
which helps avoid worst-case performance on already sorted or nearly sorted lists.

Check GitHub for the latest version:
https://github.com/Painkiller995/DTE-2511-1-25V

"""


def sort(arr: list[int]) -> None:
    """
    Sort the list using the Quick Sort algorithm.

    Args:
        - arr: The list to be sorted.
    """
    _sort(arr, 0, len(arr) - 1)


def _sort(arr: list[int], start: int, end: int) -> None:
    """
    Private helper function to sort the list using the Quick Sort algorithm.

    Args:
        - arr: The list to be sorted.
        - start: The starting index of the partition.
        - end: The ending index of the partition.
    """
    if start >= end:
        return

    # Partition the array and get the pivot index
    boundary = _partition(arr, start, end)

    # Recursively sort elements before and after partition
    _sort(arr, start, boundary - 1)
    _sort(arr, boundary + 1, end)


def _median_of_three(arr: list[int], start: int, end: int) -> int:
    """
    Selects the pivot using the median-of-three method.
    Picks the median of the first, middle, and last elements.

    Args:
        - arr: The list of numbers.
        - start: The starting index.
        - end: The ending index.

    Returns:
        int: The index of the median-of-three pivot.
    """
    mid = (start + end) // 2  # The middle index
    a, b, c = arr[start], arr[mid], arr[end]  # The three elements

    # Determine the median value and return its index
    if (a <= b <= c) or (c <= b <= a):
        return mid
    elif (b <= a <= c) or (c <= a <= b):
        return start
    else:
        return end


def _partition(arr: list[int], start: int, end: int) -> int:
    """
    Partition the array using the median-of-three pivot selection.

    Args:
        - arr: The list to be partitioned.
        - start: The starting index of the partition.
        - end: The ending index of the partition.

    Returns:
        int: The index of the pivot element after partition.
    """
    # Select pivot using median-of-three method
    pivot_index = _median_of_three(arr, start, end)
    pivot = arr[pivot_index]

    # Swap pivot with the last element (standard Quicksort practice)
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    boundary = start - 1
    for i in range(start, end):
        if arr[i] <= pivot:
            boundary += 1
            arr[i], arr[boundary] = arr[boundary], arr[i]

    # Place the pivot in its correct position
    arr[boundary + 1], arr[end] = arr[end], arr[boundary + 1]

    return boundary + 1  # Return the correct pivot index


if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {array}")
    sort(array)
    print(f"Sorted array: {array}")
