from enum import Enum

class Vehicle:
    def __init__(self, ID: int, Manufacturer: 'Manufacturer', Model: str, HorsePower: int, 
                 Price: float, Color: 'Color', Mileage: int, ProductionYear: int,
                 FuelType: 'FuelType', Transmission: 'Transmission'):
        self.__ID = ID
        self.__Manufacturer = Manufacturer
        self.__Model = Model
        self.__HorsePower = HorsePower
        self.__Price = Price
        self.__Color = Color
        self.__Mileage = Mileage
        self.__ProductionYear = ProductionYear
        self.__FuelType = FuelType
        self.__Transmission = Transmission

    # Getters
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

    # Setters
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

class Manufacturer(Enum):
    AUDI = 1
    BMW = 2
    VW = 3
    HONDA = 4
    SKODA = 5

class Color(Enum):
    BLACK = 1
    WHITE = 2
    RED = 3
    YELLOW = 4
    GREY = 5
    BLUE = 6
    BROWN = 7

class FuelType(Enum):
    GASOLINE  = 1
    DIESEL_FUEL = 2
      
class Transmission(Enum):
    AUTOMATIC = 1
    MANUAL = 2
