"""
This module implements the Insertion Sort algorithm.
Time Complexity: O(n^2) in all cases.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""


def sort(arr: list[int], left: int = 0, right: int | None = None) -> None:
    """
    Sort the list using the Insertion Sort algorithm.

    Args:
        - arr: The list to be sorted.

    Returns:
        None: The list is sorted in-place.
    """

    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        current_element = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_element


if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {array}")
    sort(array)
    print(f"Sorted array: {array}")
