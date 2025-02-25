"""
This module solves the ring buffer task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

from typing import Any


class RingBuffer:
    """
    A class that implements a ring buffer.

    """

    def __init__(self, size: int) -> None:
        self._size = size
        self._buffer = [None] * size
        self._head = 0
        self._count = 0

    def append(self, item: Any) -> None:
        """
        Adds an item to the buffer.

        Args:
            item: The item to add to the buffer.
        """
        self._buffer[self._head] = item

        # Calculate the next head position
        # % returns the dividend (self._head + 1) if its smaller than the divisor self._size
        self._head = (self._head + 1) % self._size

        if self._count < self._size:
            self._count += 1

    def __iter__(self) -> Any:
        start = (self._head - self._count) % self._size  # Find the start index of the buffer
        for i in range(self._count):
            index = (start + i) % self._size  # Wrap around when reaching the end
            yield self._buffer[index]

    def read(self) -> list[Any]:
        """
        Returns the items in the buffer without respect to the order they were added.
        """
        return self._buffer

    def __str__(self) -> str:
        return str(self.read())
