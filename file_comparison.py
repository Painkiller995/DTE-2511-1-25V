"""
This module solves the file comparison task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import os


def clear_screen() -> None:
    """
    Clears the screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome() -> None:
    """
    Prints a welcome message to the user, after clearing the screen.
    """
    clear_screen()

    print("Welcome to the US Capitals Lookup!\n")
    print("\nYou can type the name of a US state to find its capital.")
    print("Type 'exit' anytime to quit.\n")


def main() -> None:
    """
    Main function that allows the user to look up US capitals based on state names.
    """


if __name__ == "__main__":
    main()
