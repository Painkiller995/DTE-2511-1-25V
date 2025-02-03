"""
This module solves the Triangle custom exception task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""


class TriangleError(RuntimeError):
    """Exception raised when a triangle is invalid."""

    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        super().__init__(f"Invalid triangle sides: {side1}, {side2}, {side3}")


class Triangle:
    """A class representing a triangle."""

    def __init__(self, side1: float, side2: float, side3: float):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

        if not self.is_valid_triangle():
            raise TriangleError(side1, side2, side3)

    def is_valid_triangle(self) -> bool:
        """Check if the sides can form a valid triangle."""
        return (
            self._side1 + self._side2 > self._side3
            and self._side1 + self._side3 > self._side2
            and self._side2 + self._side3 > self._side1
        )

    def __str__(self):
        return f"Triangle with sides ({self._side1}, {self._side2}, {self._side3})"


def main():
    """Main function."""
    try:
        triangle = Triangle(3, 4, 5)  # Valid triangle
        print(triangle)

        triangle = Triangle(1, 2, 3)  # Invalid triangle
        print(triangle)
    except TriangleError as e:
        print(e)


if __name__ == "__main__":
    main()
