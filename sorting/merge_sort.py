"""
This module implements the Merge Sort algorithm.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""


def sort(arr: list[int]) -> None:
    """
    Sort the list using the Merge Sort algorithm.

    Args:
        - arr (list[int]): The list to be sorted.

    Returns:
        None: The list is sorted in-place.
    """

    if len(arr) <= 1:
        return

    # Divide the array into two halves
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Sort each half
    sort(left_half)
    sort(right_half)

    # Merge the two halves
    merge(arr, left_half, right_half)


def merge(arr: list[int], left_half: list[int], right_half: list[int]) -> None:
    """
    Merge two halves of the array.

    Args:
        - arr (list[int]): The list to be sorted.
        - left_half (list[int]): The left half of the list.
        - right_half (list[int]): The right half of the list.
    """

    i = j = k = 0
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


if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {array}")
    sort(array)
    print(f"Sorted array: {array}")
