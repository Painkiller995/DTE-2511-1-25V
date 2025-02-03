"""
This module solves the vehicle class task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""


class Vehicle:
    """Represents a vehicle."""

    def __init__(
        self,
        regnr: str,
        brand: str,
        model: str,
        model_year: int,
        mileage: float,
        price: float,
    ):
        self.regnr = regnr
        self.brand = brand
        self.model = model
        self.model_year = model_year
        self.mileage = mileage
        self.price = price
        self.speed_tickets: list[SpeedTicket] = []

    def add_speed_ticket(self, speed_ticket: "SpeedTicket") -> None:
        """
        Adds a speed ticket to the vehicle.

        Args:
            - speed_ticket: The speed ticket to add.
        """

        if all(speed_ticket.time_stamp != ticket.time_stamp for ticket in self.speed_tickets):
            self.speed_tickets.append(speed_ticket)

    def __str__(self) -> str:
        """
        Returns a string representation of the vehicle.
        """
        return (
            f"Registration Number: {self.regnr}, "
            f"Brand: {self.brand}, "
            f"Model: {self.model}, "
            f"Model Year: {self.model_year}, "
            f"Mileage: {self.mileage} km, "
            f"Price: {self.price} NOK"
        )


class Car(Vehicle):
    """Represents a car."""

    def __init__(
        self,
        regnr: str,
        brand: str,
        model: str,
        model_year: int,
        mileage: float,
        price: float,
        num_doors: int,
    ):
        super().__init__(regnr, brand, model, model_year, mileage, price)
        self.num_doors = num_doors

    def __str__(self) -> str:
        """
        Returns a string representation of the car.
        """
        return super().__str__() + f", Number of Doors: {self.num_doors}"


class Truck(Vehicle):
    """Represents a truck."""

    def __init__(
        self,
        regnr: str,
        brand: str,
        model: str,
        model_year: int,
        mileage: float,
        price: float,
        drive_type: str,
    ):
        super().__init__(regnr, brand, model, model_year, mileage, price)

        if drive_type not in ["F", "B", "4"]:
            raise ValueError("Invalid drive type. Must be 'F', 'B', or '4'.")

        self.drive_type = drive_type

    def __str__(self) -> str:
        """
        Returns a string representation of the truck.
        """
        return super().__str__() + f", Drive Type: {self.drive_type}"


class SUV(Vehicle):
    """Represents a SUV."""

    def __init__(
        self,
        regnr: str,
        brand: str,
        model: str,
        model_year: int,
        mileage: float,
        price: float,
        passenger_capacity: int,
    ) -> None:
        super().__init__(regnr, brand, model, model_year, mileage, price)
        self.passenger_capacity = passenger_capacity

    def __str__(self) -> str:
        return super().__str__() + f", Passenger Capacity: {self.passenger_capacity}"


class SpeedTicket:
    """Represents a speed ticket."""

    def __init__(self, time_stamp: str, speed: float, speed_limit: int):
        self.time_stamp = time_stamp
        self.speed = speed
        self.speed_limit = speed_limit

    def __str__(self) -> str:
        return f"Timestamp: {self.time_stamp}, Speed: {self.speed:.2f} km/h, Speed Limit: {self.speed_limit} km/h"
