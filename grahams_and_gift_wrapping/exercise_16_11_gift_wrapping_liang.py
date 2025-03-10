"""
Gift wrapping algorithm to find the convex hull of a set of points

This version preserves the original logic but is refactored to be more Pythonic.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import math
import random


# Return the points that form a convex hull
def get_convex_hull(points: list[list[float]]) -> list[list[float]]:
    # Step 1
    start_point = get_rightmost_lowest_point(points)

    convex_hull = [start_point]
    current_point = start_point

    # Step 2 and Step 3
    while True:
        next_point = points[0]
        for i in range(1, len(points)):
            side = which_side(
                current_point[0], current_point[1], next_point[0], next_point[1], points[i][0], points[i][1]
            )

            if side < 0:  # Right side of the line
                next_point = points[i]
            elif side == 0:
                if distance(points[i][0], points[i][1], current_point[0], current_point[1]) > distance(
                    next_point[0], next_point[1], current_point[0], current_point[1]
                ):
                    next_point = points[i]

        if next_point[0] == start_point[0] and next_point[1] == start_point[1]:
            break  # Convex hull is complete
        else:
            convex_hull.append(next_point)
            current_point = next_point

    return convex_hull


# Return the rightmost lowest point in the list
def get_rightmost_lowest_point(points: list[list[float]]) -> list[float]:
    rightmost_index = 0
    rightmost_x = points[0][0]
    rightmost_y = points[0][1]

    for i in range(1, len(points)):
        if rightmost_y > points[i][1]:
            rightmost_y = points[i][1]
            rightmost_x = points[i][0]
            rightmost_index = i
        elif rightmost_y == points[i][1] and rightmost_x < points[i][0]:
            rightmost_x = points[i][0]
            rightmost_index = i

    return points[rightmost_index]


# Calculate the distance between two points
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Determine which side (x2, y2) is relative to the line formed by (x0, y0) and (x1, y1)
def which_side(x0: float, y0: float, x1: float, y1: float, x2: float, y2: float) -> float:
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)


# Example usage
if __name__ == "__main__":
    # Generate 50 random points
    random_points = []
    for _ in range(50):
        x, y = random.random() * 100, random.random() * 100
        random_points.append([x, y])

    # Example set of points
    example_points = [
        [5.0, 2.0],
        [1.0, 1.0],
        [4.0, 2.0],
        [6.0, 4.0],
        [4.0, 3.0],
        [5.0, 6.0],
        [2.0, 4.0],
        [3.0, 6.0],
        [1.0, 3.0],
    ]

    # Convex hull for random points
    convex_hull_random = get_convex_hull(random_points)
    print("The convex hull for random points is:")
    print(convex_hull_random)

    # Convex hull for example points
    convex_hull_example = get_convex_hull(example_points)
    print("\nThe convex hull for example points is:")
    print(convex_hull_example)
