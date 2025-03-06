"""
This module solves the count occurrence of words task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""


def process_line(line: str, word_counts: dict[str, int]) -> None:
    """
    Process each line to count the words.

    Args:
        line: The line to process.
        word_counts: The dictionary to store the word counts

    """
    line = replace_punctuation(line)

    words = line.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1


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


def main() -> None:
    """
    Main function to run the program.
    """

    filename = input("Enter a filename: ").strip()

    word_counts: dict[str, int] = {}

    try:
        with open(filename, encoding="utf-8") as input_file:
            for line in input_file:
                process_line(line.lower(), word_counts)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    items = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    for word, count in items[:10]:
        print(word, count, sep="\t")


if __name__ == "__main__":
    main()
