"""
This module implements the Quick Sort algorithm.

This implementation could be improved in the feature please check github for the latest version.
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

    # Partition the array
    boundary = _partition(arr, start, end)

    # Sort left
    _sort(arr, start, boundary - 1)

    # Sort right
    _sort(arr, boundary + 1, end)


def _partition(arr: list[int], start: int, end: int) -> int:
    """
    Partition the array for the Quick Sort algorithm.

    Args:
        - arr: The list to be partitioned.
        - start: The starting index of the partition.
        - end: The ending index of the partition.

    Returns:
        int: The index of the pivot element after partition.
    """
    pivot = arr[end]
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
