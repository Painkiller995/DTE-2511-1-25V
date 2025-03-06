"""
This module solves the Baby name popularity ranking task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

The required files are hosted on:
https://liveexample.pearsoncmg.com/data/[filename]
Example:
https://liveexample.pearsoncmg.com/data/babynameranking2001.txt

"""

import requests

RECORD_START_YEAR = 2001
RECORD_END_YEAR = 2010
BASE_URL = "https://liveexample.pearsoncmg.com/data/babynamesranking"


def get_user_input() -> tuple[str, str, str]:
    """
    Get user input for the year, gender, and name with validation.

    Returns:
        tuple: A tuple containing the
            - baby_birth_year: The year of the record.
            - baby_gender: The gender of the baby.
            - baby_name: The name of the baby.
    """
    while True:
        baby_birth_year = input("Enter the year: ")
        if baby_birth_year.isdigit() and RECORD_START_YEAR <= int(baby_birth_year) <= RECORD_END_YEAR:
            break
        print(f"Invalid input! Enter a year between {RECORD_START_YEAR} and {RECORD_END_YEAR}.")

    while True:
        baby_gender = input("Enter the gender (M/F): ").upper()
        if baby_gender in ["M", "F"]:
            break
        print("Invalid input! Enter 'M' or 'F'.")

    while True:
        baby_name = input("Enter the name: ").capitalize()
        if baby_name.isalpha():
            break
        print("Invalid input! Enter a valid name with letters only.")

    return baby_birth_year, baby_gender, baby_name


def fetch_ranking_data(url: str) -> list[str]:
    """
    Get the ranking data from the file.

    Args:
        - url: The URL of the file.

    Returns:
        - list: A list of the ranking data.
    """
    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        raise ConnectionError(f"Failed to get the data from {url}")

    return response.text.splitlines()


def find_name_ranking(data: list[str], gender: str, name: str) -> tuple[str, int, int]:
    """
    Parse the ranking data and search for the requested name and gender.

    Args:
        - data: The ranking data.
        - gender: M/F
        - name: The name to search for.

    Returns:
        - tuple: A tuple containing the name, count, and rank.
    """
    for line in data:
        parts = [part.strip() for part in line.split("\t")]

        rank = int(parts[0])

        if gender == "M":
            current_name = parts[1]
            count = int(parts[2].replace(",", ""))
        else:
            current_name = parts[3]
            count = int(parts[4].replace(",", ""))

        if current_name == name:
            return current_name, count, rank

    return "", 0, 0


if __name__ == "__main__":
    input_year, input_gender, input_name = get_user_input()

    FILE_URL = f"{BASE_URL}{input_year}.txt"
    ranking_data = fetch_ranking_data(FILE_URL)

    found_name, found_count, found_rank = find_name_ranking(ranking_data, input_gender, input_name)

    print(
        f"{'Boy' if input_gender == 'M' else 'Girl'} name {found_name or input_name} "
        f"{'is ranked #' + str(found_rank) if found_name else 'not found'} in year {input_year}."
    )
