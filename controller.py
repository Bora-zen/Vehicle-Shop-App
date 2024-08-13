from model import Color, FuelType, Manufacturer, Transmission, Vehicle
# prepared csv module import
import csv
from typing import List
# Klasa për menaxhimin e skedarëve të automjeteve
class VehicleFileManager:
    def __init__(self, file_path):
        self.file_path = file_path
    def import_vehicles_from_file(self, file_path: str) -> List[List[str]]:
        vehicles_data_array = []
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                vehicles_data_array.append(row)
        return vehicles_data_array
    def rewrite_file(self, vehicle_list: List[Vehicle]):
        with open(self.file_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            for vehicle in vehicle_list:
                vehicle_info = self.prepare_the_vehicle_for_rewriting(vehicle)
                csv_writer.writerow(vehicle_info)
    def prepare_the_vehicle_for_rewriting(self, vehicle: Vehicle) -> List[str]:
        return [
            str(vehicle.get_ID()),                   # ID
            vehicle.get_Manufacturer().name,         # Prodhuesi
            vehicle.get_Model(),                     # Modeli
            str(vehicle.get_HorsePower()),           # Fuqia e motorit
            str(vehicle.get_Price()),                # Çmimi
            vehicle.get_Color().name,                # Ngjyra
            str(vehicle.get_Mileage()),              # Kilometrat
            str(vehicle.get_ProductionYear()),       # Viti i prodhimit
            vehicle.get_FuelType().name,             # Tipi i karburantit
            vehicle.get_Transmission().name          # Transmisioni
        ]
class VehicleShopPrinter:
    def print_available_vehicles(self, vehicle_list: List[Vehicle]):
        if not vehicle_list:
            print("\nNo vehicles available.")
            return
        print("\nAvailable Vehicles:")
        for vehicle in vehicle_list:
            print(f"ID: {vehicle.get_ID()}, "
                  f"Manufacturer: {vehicle.get_Manufacturer().name}, "
                  f"Model: {vehicle.get_Model()}, "
                  f"HorsePower: {vehicle.get_HorsePower()}, "
                  f"Price: ${vehicle.get_Price():,.2f}, "
                  f"Color: {vehicle.get_Color().name}, "
                  f"Mileage: {vehicle.get_Mileage()} km, "
                  f"ProductionYear: {vehicle.get_ProductionYear()}, "
                  f"FuelType: {vehicle.get_FuelType().name}, "
                  f"Transmission: {vehicle.get_Transmission().name}")
    def print_vehicle_sold_message(self, vehicle_chosen_id: int):
        print(f"\nVehicle with ID {vehicle_chosen_id} was sold.")
    def print_vehicle_id_to_sell_message(self):
        print("\n\nPlease enter the number (ID) of the vehicle you want to sell: ")
class VehicleShopProcessor:
    def sell_vehicle(self, vehicle_list: List[Vehicle], selected_vehicle_id: int) -> List[Vehicle]:
        return [vehicle for vehicle in vehicle_list if vehicle.get_ID() != selected_vehicle_id]
class VehicleTransformer:
    def transform_data_as_string_array_to_vehicle_objects(self, vehicles_as_string_array: List[str]) -> List[Vehicle]:
        vehicle_list = []
        for vehicle_string in vehicles_as_string_array:
            if isinstance(vehicle_string, list):
                vehicle = self.transform_to_vehicle_object(vehicle_string)
                vehicle_list.append(vehicle)
            else:
                raise TypeError("Expected a list for vehicle data, got: " + str(type(vehicle_string)))
        return vehicle_list
    def transform_to_vehicle_object(self, vehicle_as_string_array: List[str]) -> Vehicle:
        if len(vehicle_as_string_array) != 10:
            raise ValueError("Invalid data format for vehicle")
        vehicle_id = int(vehicle_as_string_array[0])
        manufacturer = self.get_manufacturer_from_string(vehicle_as_string_array[1])
        model = vehicle_as_string_array[2]
        horse_power = int(vehicle_as_string_array[3])
        price = float(vehicle_as_string_array[4])
        color = self.get_color_from_string(vehicle_as_string_array[5])
        mileage = int(vehicle_as_string_array[6])
        production_year = int(vehicle_as_string_array[7])
        fuel_type = self.get_fuel_type_from_string(vehicle_as_string_array[8])
        transmission = self.get_transmission_from_string(vehicle_as_string_array[9])
        return Vehicle(
            ID=vehicle_id,
            Manufacturer=manufacturer,
            Model=model,
            HorsePower=horse_power,
            Price=price,
            Color=color,
            Mileage=mileage,
            ProductionYear=production_year,
            FuelType=fuel_type,
            Transmission=transmission
        )
    def get_manufacturer_from_string(self, manufacturer_as_string: str) -> Manufacturer:
        for manufacturer in Manufacturer:
            if manufacturer.name == manufacturer_as_string:
                return manufacturer
        raise ValueError("Manufacturer not supported: " + manufacturer_as_string)
    def get_color_from_string(self, color_as_string: str) -> Color:
        for color in Color:
            if color.name == color_as_string:
                return color
        raise ValueError("Color not supported: " + color_as_string)
    def get_fuel_type_from_string(self, fuel_type_as_string: str) -> FuelType:
        for fuel_type in FuelType:
            if fuel_type.name == fuel_type_as_string:
                return fuel_type
        raise ValueError("FuelType not supported: " + fuel_type_as_string)
    def get_transmission_from_string(self, transmission_as_string: str) -> Transmission:
        for transmission in Transmission:
            if transmission.name == transmission_as_string:
                return transmission
        raise ValueError("Transmission not supported: " + transmission_as_string)