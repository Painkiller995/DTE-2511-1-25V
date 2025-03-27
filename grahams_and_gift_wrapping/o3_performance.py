"""
The bottleneck in Liang's Graham's Scan implementation:
- `sort_on_angles()` uses an O(n²) selection sort, making the algorithm significantly slower than necessary.
- Python has a built-in `sorted()` function that uses Timsort (O(n log n)).
- We replace `sort_on_angles()` with a more efficient version.
"""

import random
import time

from Exercise16_11_gift_wrapping_liang import get_convex_hull as gift_wrapping
from Exercise16_12_grahams_liang import get_convex_hull as graham_scan


def generate_random_points(size):
    return [[random.uniform(0, 100), random.uniform(0, 100)] for _ in range(size)]


def measure_time(algorithm, points):
    start_time = time.time()
    algorithm(points)
    end_time = time.time()
    return end_time - start_time


sizes = [100, 1000, 10000]

for size in sizes:
    points = generate_random_points(size)
    time_graham = measure_time(graham_scan, points)
    time_gift_wrapping = measure_time(gift_wrapping, points)
    print("-" * 50)
    print(f"Size: {size}")
    print(f"Graham's Scan: {time_graham:.6f} seconds")
    print(f"Gift Wrapping: {time_gift_wrapping:.6f} seconds")
    print("-" * 50)
