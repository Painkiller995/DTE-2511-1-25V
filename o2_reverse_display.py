"""
This module solves the reverse display task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import os


def clear_screen() -> None:
    """
    Clears the screen based on the operating system.
    """
    os.system("cls" if os.name == "nt" else "clear")


def reverse_display(value: int) -> None:
    """
    Prints the reversed value of an integer.

    Args:
        value (int): The integer to reverse and display
    """
    if value < 10:
        print(value, end="")
    else:
        print(value % 10, end="")
        reverse_display(value // 10)


if __name__ == "__main__":
    clear_screen()
    print("Welcome to the Reverse Display!\n")
    print("You can type an integer to display it in reverse order.")
    while True:
        user_input = input("Enter an integer: ")

        if not user_input.isdigit():
            print("Please enter a valid integer.")
            continue

        print("Reversed integer: ", end="")
        reverse_display(int(user_input))
        print("\n")
