"""
This module solves the average measurement task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

FILE_ENCODING = "utf-8"


def file_to_dict(file_name: str) -> dict[str, str]:
    """
    Reads a file and returns a dictionary with the data.
    Args:
        - file_name: The name of the file to read.
    """
    with open(file_name, "r", encoding=FILE_ENCODING) as file:
        return {
            line.split(",")[0].strip(): line.split(",")[1].strip()
            for line in file.readlines()
        }


class SpeedTicket:
    def __init__(self, data: dict[str, str]) -> None:
        self.data = data

    def find_speeders(
        dict_a: dict[str, str],
        dict_b: dict[str, str],
        speed_limit: int,
        distance: int,
    ) -> dict[str, str]:
        return {}


if __name__ == "__main__":
    target = "./boxes/box_a.txt"
    data = file_to_dict(target)
