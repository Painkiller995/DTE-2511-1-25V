"""
This module solves the Eight Queens Problem using backtracking algorithm.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import threading
import time
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

    def draw_board(self) -> None:
        """Draw the chess board with live updates for queens' positions."""
        for widget in self.board_frame.winfo_children():
            widget.destroy()  # Clear the previous board state

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

        self._root.update_idletasks()  # Force GUI update

    def is_safe(self, desired_row: int, desired_col: int) -> bool:
        """
        Check if a queen can be placed at the given position without being attacked.
        Args:
            desired_row: The row index where the queen is to be placed.
            desired_col: The column index where the queen is to be placed.
        Returns:
            bool: True if the position is safe for the queen, False otherwise.
        The function checks for collisions with other queens already placed in previous rows.
        It ensures that no two queens share the same column or diagonal.
        """

        for current_row in range(desired_row):  # in the first row current_row = 0, range will be skipped
            same_column = self.queens_positions[current_row] == desired_col
            if same_column:
                return False

            # To check the diagonal, we calculate the difference between the rows and the columns
            # If the difference is the same, then the queens are on the same diagonal
            same_diagonal = abs(current_row - desired_row) == abs(self.queens_positions[current_row] - desired_col)
            if same_diagonal:
                return False

        return True

    def solve(self, row: int) -> bool:
        """Solve the Eight Queens Problem using backtracking with live drawing updates."""

        if row == self.board_size:
            return True

        for col in range(self.board_size):
            if self.is_safe(row, col):
                # Place the queen if the position is safe
                self.queens_positions[row] = col

                self._root.after(100, self.draw_board)  # Live draw after placing each queen
                time.sleep(0.1)  # Simulate a delay to allow the GUI to update

                # Recur to place the rest of the queens
                if self.solve(row + 1):
                    return True

                # Backtrack if the current queen placement does not lead to a solution
                self.queens_positions[row] = -1

                self._root.after(100, self.draw_board)  # Live draw after backtracking
                time.sleep(0.1)  # Simulate a delay to allow the GUI to update

        return False

    def solve_in_thread(self) -> None:
        """Run the solver in a separate thread to prevent blocking the GUI."""
        threading.Thread(target=self.solve, args=(0,)).start()

    def run(self) -> None:
        """Run the GUI."""
        self.solve_in_thread()
        self._root.mainloop()


if __name__ == "__main__":
    app = EightQueens("Eight Queens Problem")
    app.run()
