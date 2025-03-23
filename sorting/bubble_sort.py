"""
This module implements the Bubble Sort algorithm.
Time Complexity: O(n^2) in all cases.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""


def sort(arr: list[int]) -> None:
    """
    Sort the list using the Bubble Sort algorithm.

    Args:
        - arr: The list to be sorted.

    Returns:
        - list: The sorted list.
    """
    number_of_elements = len(arr)

    # Assuming the array is already sorted.
    is_sorted = True

    for i in range(number_of_elements - 1):
        for j in range(number_of_elements - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False

        # If the array is already sorted, break the loop.
        if is_sorted:
            break


if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {array}")
    sort(array)
    print(f"Sorted array: {array}")
