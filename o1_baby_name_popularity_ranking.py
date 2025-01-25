"""
This module solves the Baby name popularity ranking task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

The required files are hosted on:
https://liveexample.pearsoncmg.com/data/[filename]
Example:
https://liveexample.pearsoncmg.com/data/babynameranking2001.txt

"""

RECORD_START_YEAR = 2001
RECORD_END_YEAR = 2010


def user_input() -> tuple:
    """
    Get user input for the year, gender, and name with validation.
    """

    while True:
        baby_birth_year = input("Enter the year: ")
        if (
            baby_birth_year.isdigit()
            and RECORD_START_YEAR <= int(baby_birth_year) <= RECORD_END_YEAR
        ):
            break
        print(
            f"Invalid input! Enter a year between {RECORD_START_YEAR} and {RECORD_END_YEAR}."
        )

    while True:
        baby_gender = input("Enter the gender (M/F): ").upper()
        if baby_gender in ["M", "F"]:
            break
        print("Invalid input! Enter 'M' or 'F'.")

    while True:
        baby_name = input("Enter the name: ")
        if baby_name.isalpha():
            break
        print("Invalid input! Enter a valid name with letters only.")

    return baby_birth_year, baby_gender, baby_name


if __name__ == "__main__":
    year, gender, name = user_input()
