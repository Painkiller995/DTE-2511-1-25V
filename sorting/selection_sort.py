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

    for i in range(number_of_elements):
        min_index = i

        for j in range(i + 1, number_of_elements):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {array}")
    sort(array)
    print(f"Sorted array: {array}")
