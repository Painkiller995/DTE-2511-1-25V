"""
This module solves the triangle exception class task.


This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""


class TriangleError(RuntimeError):
    """
    TriangleError is a custom exception class that is raised when the sides of a triangle are invalid
    """

    def __init__(self, side1: int, side2: int, side3: int) -> None:
        super().__init__("The sides do not form a valid triangle.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_sides(self) -> tuple[int, int, int]:
        """
        Returns the sides of the triangle that caused the exception
        """
        return self.side1, self.side2, self.side3
