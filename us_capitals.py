"""
This module solves the us capitals task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import os

TARGET_FILE_NAME = "USCapitals.txt"
FILE_ENCODING = "utf-8"


def welcome() -> None:
    """
    Prints a welcome message to the user, after clearing the screen.
    """

    os.system("cls" if os.name == "nt" else "clear")

    print("Welcome to the US Capitals Lookup!\n")
    print("\nYou can type the name of a US state to find its capital.")
    print("Type 'exit' anytime to quit.\n")


def read_capitals(file_name: str) -> dict[str, str]:
    """
    Reads the US capitals from a file and returns a dictionary with the states as keys and the capitals as values

    Args:
        file_name (str): The name of the file to read the capitals from

    Returns:
        dict[str, str]: A dictionary with the states as keys and the capitals as values in lowercase

    """

    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File '{file_name}' not found.")

    with open(file_name, encoding=FILE_ENCODING) as file:
        return {
            state.strip().lower(): capital.strip().lower() for state, capital in (line.split(",", 1) for line in file)
        }


def main() -> None:
    """
    Main function that allows the user to look up US capitals based on state names.
    """

    try:
        capitals = read_capitals(TARGET_FILE_NAME)
    except FileNotFoundError as e:
        print(e)
        return

    welcome()

    while True:
        state = input("Enter a state name: ").strip().lower()
        welcome()

        if state == "exit":
            print("\nThanks for using the US Capitals Lookup! Goodbye!\n")
            break

        capital = capitals.get(state)

        if capital:
            print(f"\nThe capital of {state.title()} is {capital.title()}.\n")
        else:
            print(f"Sorry, I don't recognize '{state}' as a valid state.")

        print("\n" + "-" * 40 + "\n")


if __name__ == "__main__":
    main()
