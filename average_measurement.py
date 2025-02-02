"""
This module solves the average measurement task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

from datetime import datetime

from vehicles import SpeedTicket, Vehicle

ALLOWABLE_LIMIT = 1.05  # 5% above the speed limit


def file_to_dict(file_name: str) -> dict[str, str]:
    """
    Reads a file and returns a dictionary with the data.
    Args:
        - file_name: The name of the file to read.
    """
    try:
        with open(file_name, encoding="utf-8") as file:
            return {line.split(",")[0].strip(): line.split(",")[1].strip() for line in file.readlines()}
    except FileNotFoundError:
        print(f"Please make sure the file {file_name} exists in the current directory.")
        return {}


def find_speeders(
    dict_a: dict[str, str],
    dict_b: dict[str, str],
    speed_limit: int,
    distance: float,
    vehicles: dict[str, Vehicle],
) -> None:
    """
    Finds vehicles that exceed the speed limit and adds speed tickets.

    Args:
        - dict_a: A dictionary with registration numbers and times.
        - dict_b: A dictionary with registration numbers and times.
        - speed_limit: The speed limit.
        - distance: The distance between the two boxes.
        - vehicles: A dictionary with vehicles.
    """

    allowed_limit = speed_limit * ALLOWABLE_LIMIT

    for regnr, time_a in dict_a.items():
        if regnr in dict_b:
            time_b = dict_b[regnr]
            t1 = datetime.strptime(time_a, "%Y-%m-%d %H:%M:%S")
            t2 = datetime.strptime(time_b, "%Y-%m-%d %H:%M:%S")

            time_diff_hours = abs((t2 - t1).total_seconds()) / 3600  # Convert to hours

            avg_speed = distance / time_diff_hours

            if avg_speed > allowed_limit:
                ticket = SpeedTicket(time_a, avg_speed, speed_limit)

                if regnr not in vehicles:
                    vehicles[regnr] = Vehicle(regnr, "Unknown", "Unknown", 0, 0.0, 0.0)

                vehicles[regnr].add_speed_ticket(ticket)


def display_speeders(vehicles: dict[str, Vehicle]) -> None:
    """
    Displays all vehicles with speed tickets.

    Args:
        - vehicles: A dictionary with vehicles.
    """
    for vehicle in vehicles.values():
        if vehicle.speed_tickets:
            for ticket in vehicle.speed_tickets:
                vehicle_info = f"Registration Number: {vehicle.regnr}, Average Speed: {ticket.speed:.2f} km/h"
                if vehicle.brand != "Unknown":
                    vehicle_info = f"Registration Number: {vehicle.regnr}, {vehicle.brand}-{vehicle.model}-{vehicle.model_year}, Average Speed: {ticket.speed:.2f} km/h"
                print(vehicle_info)


def main() -> None:
    """The main function."""
    box_a_data = file_to_dict("box_a.txt")
    box_b_data = file_to_dict("box_b.txt")
    ticketed_vehicles: dict[str, Vehicle] = {}
    find_speeders(box_a_data, box_b_data, speed_limit=60, distance=5, vehicles=ticketed_vehicles)
    display_speeders(ticketed_vehicles)


if __name__ == "__main__":
    main()
