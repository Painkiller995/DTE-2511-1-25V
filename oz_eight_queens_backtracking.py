"""
This module solves the Eight Queens Problem using backtracking algorithm.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import tkinter
from tkinter import Frame, Label, PhotoImage

QUEEN_IMAGE = "image/queen.gif"


class EightQueens:
    """A simple GUI application."""

    def __init__(self, title: str, board_size: int = 8) -> None:
        self._root = tkinter.Tk()
        self._root.title(title)

        screen_width = self._root.winfo_screenwidth()
        screen_height = self._root.winfo_screenheight()
        window_size = min(screen_width, screen_height) - min(screen_width, screen_height) // 4
        position_right = (screen_width // 2) - (window_size // 2)
        position_down = (screen_height // 2) - (window_size // 2)
        self._root.geometry(f"{window_size}x{window_size}+{position_right}+{position_down}")

        self.board_size = board_size
        self.queens_positions = [-1] * board_size
        self.square_size = window_size // board_size

        self.queen_image = PhotoImage(file=QUEEN_IMAGE)

        self.board_frame = Frame(self._root)
        self.board_frame.pack(expand=True, fill="both")

        self.solve(0)

        self.draw_board()

    def draw_board(self) -> None:
        """Draw the chess board."""
        for i in range(self.board_size):
            for j in range(self.board_size):
                frame = Frame(self.board_frame, width=self.square_size, height=self.square_size)
                frame.grid(row=i, column=j)
                frame.propagate(False)

                if self.queens_positions[i] == j:
                    label = Label(frame, image=self.queen_image, borderwidth=1, relief="solid")
                else:
                    label = Label(frame, bg="red" if (i + j) % 2 else "white", borderwidth=1, relief="solid")

                label.pack(expand=True, fill="both")

    def is_safe(self, row: int, col: int) -> bool:
        """Check if a queen can be placed at the given position."""
        for i in range(row):
            same_column = self.queens_positions[i] == col
            same_diagonal = abs(i - row) == abs(self.queens_positions[i] - col)
            if same_column or same_diagonal:
                return False
        return True

    def solve(self, row: int) -> bool:
        """Solve the Eight Queens Problem using backtracking."""
        if row == self.board_size:
            return True

        for col in range(self.board_size):
            if self.is_safe(row, col):
                self.queens_positions[row] = col

                if self.solve(row + 1):
                    return True

                self.queens_positions[row] = -1

        return False

    def run(self) -> None:
        """Run the GUI."""
        self._root.mainloop()


if __name__ == "__main__":
    app = EightQueens("Eight Queens Problem")
    app.run()
