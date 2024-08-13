from enum import Enum

# Vehicle class representing a vehicle with various attributes
class Vehicle:
    def __init__(self, ID: int, Manufacturer: 'Manufacturer', Model: str, HorsePower: int, 
                 Price: float, Color: 'Color', Mileage: int, ProductionYear: int,
                 FuelType: 'FuelType', Transmission: 'Transmission'):
        # Private attributes for encapsulation
        self.__ID = ID                            # Unique ID for the vehicle
        self.__Manufacturer = Manufacturer        # Manufacturer of the vehicle (Enum)
        self.__Model = Model                      # Model name of the vehicle
        self.__HorsePower = HorsePower            # Horsepower of the vehicle
        self.__Price = Price                      # Price of the vehicle
        self.__Color = Color                      # Color of the vehicle (Enum)
        self.__Mileage = Mileage                  # Mileage of the vehicle
        self.__ProductionYear = ProductionYear    # Production year of the vehicle
        self.__FuelType = FuelType                # Fuel type of the vehicle (Enum)
        self.__Transmission = Transmission        # Transmission type of the vehicle (Enum)

    # Getter methods for accessing private attributes
    def get_ID(self) -> int:
        return self.__ID

    def get_Manufacturer(self) -> 'Manufacturer':
        return self.__Manufacturer

    def get_Model(self) -> str:
        return self.__Model

    def get_HorsePower(self) -> int:
        return self.__HorsePower

    def get_Price(self) -> float:
        return self.__Price

    def get_Color(self) -> 'Color':
        return self.__Color

    def get_Mileage(self) -> int:
        return self.__Mileage

    def get_ProductionYear(self) -> int:
        return self.__ProductionYear

    def get_FuelType(self) -> 'FuelType':
        return self.__FuelType

    def get_Transmission(self) -> 'Transmission':
        return self.__Transmission

    # Setter methods for modifying private attributes
    def set_ID(self, ID: int):
        self.__ID = ID

    def set_Manufacturer(self, Manufacturer: 'Manufacturer'):
        self.__Manufacturer = Manufacturer

    def set_Model(self, Model: str):
        self.__Model = Model

    def set_HorsePower(self, HorsePower: int):
        self.__HorsePower = HorsePower

    def set_Price(self, Price: float):
        self.__Price = Price

    def set_Color(self, Color: 'Color'):
        self.__Color = Color

    def set_Mileage(self, Mileage: int):
        self.__Mileage = Mileage

    def set_ProductionYear(self, ProductionYear: int):
        self.__ProductionYear = ProductionYear

    def set_FuelType(self, FuelType: 'FuelType'):
        self.__FuelType = FuelType

    def set_Transmission(self, Transmission: 'Transmission'):
        self.__Transmission = Transmission

# Enum class for vehicle manufacturers
class Manufacturer(Enum):
    AUDI = 1
    BMW = 2
    VW = 3
    HONDA = 4
    SKODA = 5

# Enum class for vehicle colors
class Color(Enum):
    BLACK = 1
    WHITE = 2
    RED = 3
    YELLOW = 4
    GREY = 5
    BLUE = 6
    BROWN = 7

# Enum class for fuel types
class FuelType(Enum):
    GASOLINE = 1        # Gasoline fuel type
    DIESEL_FUEL = 2     # Diesel fuel type

# Enum class for transmission types
class Transmission(Enum):
    AUTOMATIC = 1       # Automatic transmission
    MANUAL = 2          # Manual transmission
