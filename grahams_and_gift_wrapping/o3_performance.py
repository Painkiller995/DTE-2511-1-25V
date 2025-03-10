"""
This module provides a function to draw points on a grid.
"""


def draw_points(points: list[list[float]]) -> None:
    """
    Draws the given points on a grid.

    Args:
        points (list[list[float]]): A list of points where each point is represented by a list of two floats [x, y].
    """
    max_x_cord: int = 0
    max_y_cord: int = 0

    for point in points:
        if max_x_cord < point[0]:
            max_x_cord = int(point[0])
        if max_y_cord < point[1]:
            max_y_cord = int(point[1])

    for y in range(max_y_cord, -1, -1):
        for x in range(max_x_cord + 1):
            point = [float(x), float(y)]
            if point in points:
                print(f" {x},{y} ", end="")
            else:
                print("     ", end="")
        print()


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

draw_points(example_points)
