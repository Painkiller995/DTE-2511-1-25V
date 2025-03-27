"""
The current implementation of the sort_on_angles function uses the selection sort algorithm,
which has a time complexity of O(n^2). This is inefficient for large datasets.
To optimize performance, we replace selection sort with Python's built-in sorted() function,
which uses Timsort and provides a time complexity of O(n log n).
"""

import random
import time
from collections.abc import Callable

from Exercise16_11_gift_wrapping_liang import get_convex_hull as get_convex_hull_gift_wrapping
from Exercise16_12_grahams_liang import get_convex_hull as get_convex_hull_grahams


def measure_time(algorithm: Callable, points: list[tuple[float, float]]) -> float:
    """
    Measures the time taken to execute the algorithm on the given points.

    Args:
        algorithm: The algorithm to measure.
        points: The points to run the algorithm on.
    """

    start_time = time.time()
    algorithm(points)
    end_time = time.time()
    return end_time - start_time


def generate_random_list(n: int) -> list[tuple[float, float]]:
    """
    Generates a list of n random points.

    Args:
        n: The number of points to generate.
    """
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]


def main() -> None:
    """
    Main function to compare the performance of Graham's Scan and Gift Wrapping algorithms.
    """
    sizes = [100, 1000]
    for size in sizes:
        random_points = generate_random_list(size)
        time_grahams = measure_time(get_convex_hull_grahams, random_points)
        time_gift_wrapping = measure_time(get_convex_hull_gift_wrapping, random_points)
        print(f"Size: {size}")
        print(f"Graham's Scan: {time_grahams:.6f} seconds")
        print(f"Gift Wrapping: {time_gift_wrapping:.6f} seconds")
        print()


if __name__ == "__main__":
    main()
