from Database.Mapper import get_all_as_objects, insert, get_by_id_as_object, delete, update
from Objects.Customer import Customer


class CustomerDAO:

    @staticmethod
    def get_all():
        return get_all_as_objects(Customer)

    @staticmethod
    def get_by_id(id_customer):
        return get_by_id_as_object(data_class=Customer, id_record=id_customer)

    @staticmethod
    def insert(customer):
        customer.id_customer = insert(customer)

    @staticmethod
    def delete(customer):
        return delete(customer)

    @staticmethod
    def update(customer):
        return update(customer)
