"""
This module provides a function to draw points on a grid using integers.
"""


def draw_points(points: list[tuple[float, float]]) -> None:
    """
    Draws the points on a grid using integers.

    Args:
        points (list[tuple[float, float]]): A list of points where each point is represented by a tuple of two floats [x, y].
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


# Example usage
example_points: list[tuple[float, float]] = [
    (5.0, 2.0),
    (1.0, 1.0),
    (4.0, 2.0),
    (6.0, 4.0),
    (4.0, 3.0),
    (5.0, 6.0),
    (2.0, 4.0),
    (3.0, 6.0),
    (1.0, 3.0),
]

draw_points(example_points)
