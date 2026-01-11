import database
from DAO.CustomerDAO import CustomerDAO
from Objects.Contract import Contract

class ContractDAO:

    @staticmethod
    def get_all():
        return database.get_all_as_objects(Contract)

    @staticmethod
    def get_by_id(id_contract):
        return database.get_by_id_as_object(data_class=Contract, id_record=id_contract)

    @staticmethod
    def insert(contract):
        contract.id_contract = database.insert(contract)

    @staticmethod
    def delete(contract):
        return database.delete(contract)

    @staticmethod
    def update(contract):
        return database.update(contract)

    @staticmethod
    def get_customer(contract):
        return CustomerDAO.get_by_id(contract.id_customer)

