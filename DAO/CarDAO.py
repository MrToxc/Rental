from DAO.BrandDAO import BrandDAO
from Database.Mapper import get_all_as_objects, insert, get_by_id_as_object, delete, update
from Objects.Car import Car


class CarDAO:

    @staticmethod
    def get_all():
        return get_all_as_objects(Car)

    @staticmethod
    def get_by_id(id_car):
        return get_by_id_as_object(data_class=Car, id_record=id_car)

    @staticmethod
    def insert(car):
        car.id_car = insert(car)

    @staticmethod
    def delete(car):
        return delete(car)

    @staticmethod
    def update(car):
        return update(car)

    @staticmethod
    def get_brand(car):
        return BrandDAO.get_by_id(id_brand=car.id_brand)
