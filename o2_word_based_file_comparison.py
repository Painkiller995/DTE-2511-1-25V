"""
This module solves the word-based file comparison task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import os


def process_file(filename: str) -> set[str]:
    """
    Reads a file and returns a set of unique words in the file.
    """
    word_set = set()

    try:
        with open(filename, encoding="utf-8") as file:
            for line in file:
                line = replace_punctuation(line.lower())
                words = line.split()
                word_set.update(words)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return set()

    return word_set


def replace_punctuation(line: str) -> str:
    """
    Replace punctuation in the line with space.

    Args:
        line: The line to replace punctuation.

    Returns:
        str: The line with punctuation replaced.
    """
    for ch in line:
        if ch in "~@#$%^&*()_-+=~<>?/,.;:!{}[]|'\"":
            line = line.replace(ch, " ")

    return line


def clear_screen() -> None:
    """
    Clears the screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def main() -> None:
    """
    Main function to run the program.
    """

    clear_screen()

    file1 = input("Enter the name of the first file: ")
    file2 = input("Enter the name of the second file: ")

    words_file1 = process_file(file1)
    words_file2 = process_file(file2)

    if not words_file1 or not words_file2:
        return

    union_words = words_file1 | words_file2  # All unique words found in either file (union)
    intersection_words = words_file1 & words_file2  # Words that appear in both files (intersection)
    difference_1 = words_file1 - words_file2  # Words found in file1 but not in file2 (difference)
    difference_2 = words_file2 - words_file1  # Words found in file2 but not in file1 (difference)
    symmetric_difference = words_file1 ^ words_file2  # Words found in only one of the files, not both (symmetric diff)

    clear_screen()
    print(50 * "-")
    print(f"File 1: {file1}")
    print(f"File 2: {file2}")
    print(50 * "-")
    print(f"Number of unique words in both files: {len(union_words)}" if union_words else "")
    print("All unique words in both files:", union_words if union_words else "")
    print("Unique words that appear in both files:", intersection_words if intersection_words else "")
    print("Unique words that appear only in the first file:", difference_1 if difference_1 else "")
    print("Unique words that appear only in the second file:", difference_2 if difference_2 else "")
    print(
        "Unique words that appear in only one of the files, but not both:",
        symmetric_difference if symmetric_difference else "",
    )
    print(50 * "-")


if __name__ == "__main__":
    main()
