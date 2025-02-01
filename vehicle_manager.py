"""
This module solves the car creation task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import atexit
import os
import pickle
from typing import Any, cast

import vehicles

FILE_NAME = "vehicles.dat"

NEW_CAR = 1
NEW_TRUCK = 2
NEW_SUV = 3
FIND_VEHICLE = 4
SHOW_VEHICLES = 5
QUIT = 6


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
    print("6) Quit")
    print()


def clear_screen() -> None:
    """
    Clears the console screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def load_vehicles(filename: str) -> list[vehicles.Vehicle]:
    """
    Loads vehicles from a file.
    Args:
        - filename: The name of the file to load vehicles from.

    Returns:
        A list of vehicles.
    """
    if os.path.exists(filename):
        with open(filename, "rb") as file:
            return cast(list[vehicles.Vehicle], pickle.load(file))
    else:
        return []


def save_vehicles(filename: str, vehicles_list: list[vehicles.Vehicle]) -> None:
    """
    Saves vehicles to a file.

    Args:
        - filename: The name of the file to save vehicles to.
        - vehicles_list: A list of vehicles to save.
    """
    with open(filename, "wb") as file:
        pickle.dump(vehicles_list, file)


def on_exit(vehicles_list: list[vehicles.Vehicle]) -> None:
    """
    Saves the vehicles list to a file when the program exits.

    Args:
        - vehicles_list: A list of vehicles to save.
    """
    print("Saving vehicles list to vehicles.dat...")
    save_vehicles("vehicles.dat", vehicles_list)


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


def add_new_vehicle(choice: int, vehicles_list: list[vehicles.Vehicle]) -> None:
    """
    Adds a new vehicle based on user's choice.
    Args:
        - choice: The type of vehicle to add.
        - vehicles_list: List of existing vehicles.
    """
    if choice == NEW_CAR:
        vehicle_info = get_vehicle_details()
        doors = get_input("number of doors", int)
        new_car = vehicles.Car(*vehicle_info, doors)
        vehicles_list.append(new_car)

    elif choice == NEW_TRUCK:
        vehicle_info = get_vehicle_details()

        while True:
            drive_type = input("Enter drive type (F, B, 4): ").upper()
            if drive_type in ["F", "B", "4"]:
                break
            print("Invalid drive type. Must be 'F', 'B', or '4'.")

        new_truck = vehicles.Truck(*vehicle_info, drive_type)
        vehicles_list.append(new_truck)

    elif choice == NEW_SUV:
        vehicle_info = get_vehicle_details()
        capacity = get_input("passenger capacity", int)
        new_suv = vehicles.SUV(*vehicle_info, capacity)
        vehicles_list.append(new_suv)


def show_vehicles(vehicles_list: list[vehicles.Vehicle]) -> None:
    """
    Show all vehicles in a clean and concise format.
    """
    print("\n\n--- Vehicles in Inventory ---")
    if not vehicles_list:
        print("No vehicles available.")
    else:
        for idx, item in enumerate(vehicles_list, 1):
            print(f"\n{idx}. {item}")


def find_vehicle(brand: str, vehicles_list: list[vehicles.Vehicle]) -> None:
    """
    Find vehicles by make.
    Args:
        - brand: The make of the vehicle to search for.
        - vehicles_list: List of vehicles to search.
    """
    found = False
    for item in vehicles_list:
        if item.brand.lower() == brand.lower():
            print(f"\n{item}.")
            found = True
    if not found:
        print("\nNo vehicles found with that make.")


def main() -> None:
    """
    The main function.
    """

    vehicles_list = load_vehicles(FILE_NAME)

    # Register the on_exit function to save the vehicles list when the program exits.
    atexit.register(on_exit, vehicles_list)

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
                add_new_vehicle(choice, vehicles_list)
            elif choice == FIND_VEHICLE:
                brand = get_input("car brand")
                find_vehicle(brand, vehicles_list)
            elif choice == SHOW_VEHICLES:
                show_vehicles(vehicles_list)
            elif choice == QUIT:
                print("Exiting the program...")
                break

            input("\nPress Enter to return to the menu...")

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
