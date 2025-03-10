"""
This module provides a function to draw points on a grid using integers.
"""

import random
import time
from typing import Callable

from exercise16_12_grahams_liang import get_convex_hull as get_convex_hull_grahams
from exercise_16_11_gift_wrapping_liang import get_convex_hull as get_convex_hull_gift_wrapping


def draw_points(points: list[tuple[float, float]]) -> None:
    """
    Draws the points on a grid using integers in the console.

    Args:
        points: A list of points represented as tuples (x, y).
    """
    max_x, max_y = 0, 0

    int_points = []
    for x, y in points:
        x_int, y_int = int(x), int(y)
        int_points.append((x_int, y_int))
        if x_int > max_x:
            max_x = x_int
        if y_int > max_y:
            max_y = y_int

    point_set = set(int_points)

    for y in range(max_y, -1, -1):
        for x in range(0, max_x + 1):
            if (x, y) in point_set:  # using set O(1) lookup
                print(f" {x},{y} ", end="")
            else:
                print("     ", end="")
        print()


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
    return [(random.random(), random.random()) for _ in range(n)]


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
