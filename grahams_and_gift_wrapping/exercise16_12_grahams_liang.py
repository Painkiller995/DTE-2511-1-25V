"""
Graham's algorithm for finding the convex hull of a set of points.

This version preserves the original logic but is refactored to be more Pythonic.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

# Convex hull Grahams
import math


# Return the points that form a convex hull
def get_convex_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]] | None:
    # Step 1
    place_rightmost_lowest_point(points)

    # Step 2
    sort_points_on_angles(points)
    points = discard_ties(points)  # If two points have the same angle, discard the one that is closer to p0

    if len(points) < 3:
        return None

    # Step 3
    stack = [points[0], points[1], points[2]]  # We use a stack for stack

    # Step 4 / 5
    return remove_concave_points(points, stack)


def remove_concave_points(
    points: list[tuple[float, float]], stack: list[tuple[float, float]]
) -> list[tuple[float, float]]:
    index = 3
    while index < len(points):
        top = stack[-1]
        next_to_top = stack[-2]

        if which_side(next_to_top[0], next_to_top[1], top[0], top[1], points[index][0], points[index][1]) <= 0:
            # on the right of the line from next_to_top to top
            # pop the top element off the stack
            stack.pop()
        else:
            # push a new element to the stack
            stack.append(points[index])
            index += 1

    return stack


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    # return math.dist((x1,y1),(x2,y2)) # alternatively


# Is (x2, y2) on the right side of [x0, y0] and [x1, y1]
def which_side(x0: float, y0: float, x1: float, y1: float, x2: float, y2: float) -> float:
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)


# Place the rightmost lowest point as the first element in points
def place_rightmost_lowest_point(points: list[tuple[float, float]]) -> None:
    """
    Places the rightmost and lowest point in the list points at index 0.

    Args:
        points (list): A list of points represented as tuples (x, y).

    Returns:
        None
    """
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

    # Swap points[rightmost_index] with points[0]
    if rightmost_index != 0:
        points[0], points[rightmost_index] = points[rightmost_index], points[0]


# The current implementation of the sort_points_on_angles function uses the selection sort algorithm,
# which has a time complexity of O(n^2). This is inefficient for large datasets.
# To optimize performance, we replace selection sort with Python's built-in sorted() function,
# which uses Timsort and provides a time complexity of O(n log n).
def sort_points_on_angles(points: list[tuple[float, float]]) -> None:
    for i in range(1, len(points) - 1):
        # Find the minimum in the points[i..len(points)-1]
        current_min = points[i]
        current_min_index = i

        for j in range(i + 1, len(points)):
            if (
                compare_angles(points[0][0], points[0][1], current_min[0], current_min[1], points[j][0], points[j][1])
                < 0
            ):
                current_min = points[j]
                current_min_index = j

        # Swap points[i] with points[current_min_index] if necessary;
        if current_min_index != i:
            points[current_min_index] = points[i]
            points[i] = current_min


# Compare two points' angles
def compare_angles(x0: float, y0: float, x1: float, y1: float, x2: float, y2: float) -> int:
    status = which_side(x0, y0, x1, y1, x2, y2)
    if status > 0:  # Left side of the line from rightmost_lowest_point to o
        return 1
    if status <= 0.000001:
        return 0
    return -1


# If two points have the same angle, discard the one that is closer to p0
def discard_ties(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """
    Discards ties from a list of points based on their distances from the first point.

    Args:
        points (list): A list of points represented as tuples (x, y).

    Returns:
        list: A new list of points with ties discarded.

    """
    result = [points[0]]

    i = 1
    while i < len(points):
        max_distance = distance(points[0][0], points[0][1], points[i][0], points[i][1])
        index_of_farthest = i
        k = i + 1
        while (
            k < len(points)
            and compare_angles(points[0][0], points[0][1], points[i][0], points[i][1], points[k][0], points[k][1]) == 0
        ):
            if max_distance < distance(points[0][0], points[0][1], points[k][0], points[k][1]):
                max_distance = distance(points[0][0], points[0][1], points[k][0], points[k][1])
                index_of_farthest = k

            k += 1

        result.append(points[index_of_farthest])
        i = k

    return result


# Example usage
if __name__ == "__main__":
    # Example set of points
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

    # Convex hull for example points
    convex_hull_example = get_convex_hull(example_points)
    print("\nThe convex hull for example points is:")
    print(convex_hull_example)
