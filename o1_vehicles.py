"""
This module solves the vehicle task.

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

    def __str__(self) -> str:
        """
        Returns a string representation of the vehicle.
        """
        return (
            f"Vehicle Information:\n"
            f"Registration Number: {self.regnr}\n"
            f"Brand: {self.brand}\n"
            f"Model: {self.model}\n"
            f"Model Year: {self.model_year}\n"
            f"Mileage: {self.mileage} km\n"
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
        return super().__str__() + f"\nNumber of Doors: {self.num_doors}"


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
        return super().__str__() + f"\nDrive Type: {self.drive_type}"


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
        return super().__str__() + f"\nPassenger Capacity: {self.passenger_capacity}"
