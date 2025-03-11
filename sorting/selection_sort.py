"""
This module implements the Selection Sort algorithm.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""


def sort(arr: list[int]) -> None:
    """
    Sort the list using the Selection Sort algorithm.

    Args:
        - arr: The list to be sorted.

    Returns:
        - list: The sorted list.
    """
    number_of_elements = len(arr)

    # Assuming the array is already sorted.
    is_sorted = True

    for i in range(number_of_elements):
        for j in range(number_of_elements):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                is_sorted = False

        if is_sorted:  # If the array is already sorted, break the loop.
            break


if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {array}")
    sort(array)
    print(f"Sorted array: {array}")
