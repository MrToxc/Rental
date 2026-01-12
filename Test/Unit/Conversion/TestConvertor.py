import unittest
from pathlib import Path

from Conversion.Convertor import convert_csv_to_data_objects
from Database.Config import find_file
from Objects.Brand import Brand
from Objects.Car import Car


class TestConvertor(unittest.TestCase):

    def test_convert_csv_to_brand(self):
        brand_csv = find_file("Test/TestData/brand.csv")
        self.assertTrue(Path(brand_csv).resolve().exists())

        brands = convert_csv_to_data_objects(brand_csv, Brand)
        self.assertTrue(len(brands) == 10)
        self.assertTrue(brands[0].id_brand is "1")
        self.assertTrue(brands[0].name == "Škoda")


    def test_convert_csv_to_car(self):
        car_csv = find_file("Test/TestData/car.csv")
        self.assertTrue(Path(car_csv).resolve().exists())

        cars = convert_csv_to_data_objects(car_csv, Car)
        self.assertTrue(len(cars) == 10)
