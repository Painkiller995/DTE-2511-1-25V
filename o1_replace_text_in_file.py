"""
This module solves the Replace text in file task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

FILE_ENCODING = "utf-8"


def get_user_input() -> tuple:
    """
    Get user input for the file name, old text, and new text.

    Returns:
        tuple: A tuple containing the
            - file_name: The name of the file.
            - old_text : The old text to replace.
            - new_text : The new text to replace with.
    """
    while True:
        file_name = input("Enter the file name (including the extension): ")
        if file_name:
            break
        print("Invalid input! Enter a valid file name.")

    while True:
        old_text = input("Enter the old string to be replaced: ")
        if old_text:
            break
        print("Invalid input! Enter a valid old text.")

    while True:
        new_text = input("Enter the new string to replace the old string with: ")
        if new_text:
            break
        print("Invalid input! Enter a valid new text.")

    return file_name, old_text, new_text


def replace_text_in_file(file_name: str, old_text: str, new_text: str) -> None:
    """
    Replace old text with new text in the file without reading it fully into memory.

    Args:
        - file_name: The name of the file to modify.
        - old_text: The text to replace.
        - new_text: The text to replace with.
    """
    try:
        with open(file_name, "r", encoding=FILE_ENCODING) as file:
            lines = file.readlines()

        modified_lines = [line.replace(old_text, new_text) for line in lines]

        if modified_lines == lines:
            raise ValueError(f"Text '{old_text}' not found in {file_name}.")

        with open(file_name, "w", encoding=FILE_ENCODING) as file:
            file.writelines(modified_lines)

        print(f"Text replaced in {file_name} successfully.")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    input_file_name, input_old_text, input_new_text = get_user_input()
    replace_text_in_file(input_file_name, input_old_text, input_new_text)
