"""
This module solves the car creation task.

Please make sure the boxes A and B files are in the same directory as this script.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import atexit
import os
import pickle
from typing import Any, cast

import o1_vehicles
from o1_average_measurement import display_speeders, file_to_dict, find_speeders
from o1_vehicles import Vehicle

FILE_NAME = "vehicles.dat"
BOX_A_FILE = "box_a.txt"
BOX_B_FILE = "box_b.txt"

NEW_CAR = 1
NEW_TRUCK = 2
NEW_SUV = 3
FIND_VEHICLE = 4
SHOW_VEHICLES = 5
SPEED_VIOLATIONS = 6
QUIT = 7


def display_menu() -> None:
    """
    Displays a menu.
    """
    print("        MENU")
    print("1) New car")
    print("2) New truck")
    print("3) New SUV")
    print("4) Find vehicles by make")
    print("5) Show all vehicles")
    print("6) Check speed violations")
    print("7) Quit")
    print()


def clear_screen() -> None:
    """
    Clears the console screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def load_vehicles(filename: str) -> dict[str, Vehicle]:
    """
    Loads vehicles from a file.
    Args:
        - filename: The name of the file to load vehicles from.

    Returns:
        A dictionary with the vehicles.
    """
    if os.path.exists(filename):
        with open(filename, "rb") as file:
            return cast(dict[str, Vehicle], pickle.load(file))
    else:
        return {}


def save_vehicles(filename: str, vehicles_dict: dict[str, Vehicle]) -> None:
    """
    Saves vehicles to a file.

    Args:
        - filename: The name of the file to save vehicles to.
        - vehicles_dict: A list of vehicles to save.
    """
    with open(filename, "wb") as file:
        pickle.dump(vehicles_dict, file)


def on_exit(vehicles_dict: dict[str, Vehicle]) -> None:
    """
    Saves the vehicles dictionary to a file when the program exits.

    Args:
        - vehicles_dict: A list of vehicles to save.
    """
    print("Saving vehicles list to vehicles.dat...")
    save_vehicles("vehicles.dat", vehicles_dict)


def get_input(prompt: str, value_type: type = str) -> Any:
    """
    Get input from the user and validate it.
    Args:
        - prompt: The prompt to display to the user.
        - value_type: The type of value to convert the input to.

    Returns:
        The validated value.
    """
    while True:
        user_input = input(f"Enter {prompt}: ")
        if user_input:
            try:
                value = value_type(user_input)
                return value
            except ValueError:
                print(f"Please enter a valid {prompt}.")


def get_vehicle_details() -> tuple[str, str, str, int, int, int]:
    """
    Collect general vehicle details from the user.
    """
    regnr = get_input("registration number").upper()
    brand = get_input("brand").capitalize()
    model = get_input("model")
    model_year = get_input("model year", int)
    mileage = get_input("mileage", int)
    price = get_input("price", int)

    return regnr, brand, model, model_year, mileage, price


def add_new_vehicle(choice: int, vehicles_dict: dict[str, Vehicle]) -> None:
    """
    Adds a new vehicle based on user's choice.
    Args:
        - choice: The type of vehicle to add.
        - vehicles_dict: The dictionary of vehicles to add the new vehicle to.
    """
    if choice == NEW_CAR:
        vehicle_info = get_vehicle_details()
        doors = get_input("number of doors", int)
        new_car = o1_vehicles.Car(*vehicle_info, doors)
        vehicles_dict[new_car.regnr] = new_car

    elif choice == NEW_TRUCK:
        vehicle_info = get_vehicle_details()

        while True:
            drive_type = input("Enter drive type (F, B, 4): ").upper()
            if drive_type in ["F", "B", "4"]:
                break
            print("Invalid drive type. Must be 'F', 'B', or '4'.")

        new_truck = o1_vehicles.Truck(*vehicle_info, drive_type)
        vehicles_dict[new_truck.regnr] = new_truck

    elif choice == NEW_SUV:
        vehicle_info = get_vehicle_details()
        capacity = get_input("passenger capacity", int)
        new_suv = o1_vehicles.SUV(*vehicle_info, capacity)
        vehicles_dict[new_suv.regnr] = new_suv


def show_vehicles(vehicles_dict: dict[str, Vehicle]) -> None:
    """
    Show all vehicles in a clean and concise format.
    Args:
        - vehicles_dict: The dictionary of vehicles to display.
    """
    print("\n\n--- Vehicles in Inventory ---")
    if not vehicles_dict:
        print("No vehicles available.")
    else:
        for _, item in vehicles_dict.items():
            if item.brand == "Unknown":
                continue
            print(f"\n{item}")


def find_vehicle(brand: str, vehicles_dict: dict[str, Vehicle]) -> None:
    """
    Find vehicles by make.
    Args:
        - brand: The make of the vehicle to search for.
        - vehicles_dict: The dictionary of vehicles to display.
    """
    found = False
    for item in vehicles_dict.values():
        if item.brand.lower() == brand.lower():
            print(f"\n{item}.")
            found = True
    if not found:
        print("\nNo vehicles found with that make.")


def find_speed_violations(vehicles_dict: dict[str, Vehicle]) -> None:
    """
    Find vehicles by make.
    Args:
        - vehicles_dict: The dictionary of vehicles to display.
    """
    box_a_data = file_to_dict(BOX_A_FILE)
    box_b_data = file_to_dict(BOX_B_FILE)
    find_speeders(box_a_data, box_b_data, speed_limit=60, distance=5, vehicles=vehicles_dict)


def main() -> None:
    """
    The main function.
    """

    vehicles_dict = load_vehicles(FILE_NAME)

    # Register the on_exit function to save the vehicles list when the program exits.
    atexit.register(on_exit, vehicles_dict)

    choice = 0

    while choice != QUIT:
        try:
            clear_screen()
            display_menu()

            user_input = input("Enter your choice: ")

            if not user_input.isdigit():
                raise ValueError("Please enter a number between 1 and 6.")

            choice = int(user_input)

            if choice < NEW_CAR or choice > QUIT:
                raise ValueError("Please enter a number between 1 and 6.")

            clear_screen()

            if choice in [NEW_CAR, NEW_TRUCK, NEW_SUV]:
                add_new_vehicle(choice, vehicles_dict)
            elif choice == FIND_VEHICLE:
                brand = get_input("car brand")
                find_vehicle(brand, vehicles_dict)
            elif choice == SHOW_VEHICLES:
                show_vehicles(vehicles_dict)
            elif choice == SPEED_VIOLATIONS:
                find_speed_violations(vehicles_dict)
                display_speeders(vehicles_dict)
            elif choice == QUIT:
                print("Exiting the program...")
                break

            input("\nPress Enter to return to the menu...")

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
