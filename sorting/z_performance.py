"""
This module implements the performance comparison of the sorting algorithms.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import random
import time

from bubble_sort import sort as bubble_sort
from insertion_sort import sort as insertion_sort
from merge_sort import sort as merge_sort
from selection_sort import sort as selection_sort


def compare_performance() -> None:
    """
    Compare the performance of different sorting algorithms
    """
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort,
    }

    data = [random.randint(0, 1000) for _ in range(10000)]

    for name, sort_func in algorithms.items():
        start_time = time.time()
        sort_func(data.copy())
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")


if __name__ == "__main__":
    compare_performance()
