import unittest

from Objects.Customer import Customer
from DAO.CustomerDAO import CustomerDAO
from DAO.ContractDAO import ContractDAO
from Objects.Contract import Contract


class TestContractDAO(unittest.TestCase):

    def test_insert_update_delete_find(self):
        customer = Customer("Jan", "Novak", "janovak@seznam.cz")
        CustomerDAO.insert(customer)
        try:
            self.contract_test(customer)
        finally:
            CustomerDAO.delete(customer)

    def contract_test(self, customer: Customer):
        contract = Contract(1000.0, customer.id_customer)
        ContractDAO.insert(contract)
        try:
            self.assertTrue(contract.id_contract is not None and contract.id_contract >= 0)
            contracts = ContractDAO.get_all()
            self.assertTrue(contract in contracts)
            contract.total_price = 2000.0
            ContractDAO.update(contract)
            self.assertTrue(contract in ContractDAO.get_all())
            self.assertTrue(contract == ContractDAO.get_by_id(contract.id_contract))
            self.assertTrue(contract.id_customer == customer.id_customer)
            self.assertTrue(ContractDAO.get_customer(contract) == customer)
        finally:
            ContractDAO.delete(contract)
        self.assertTrue(contract not in contracts)
        contract.total_price = 3000.0
        self.assertFalse(contract in ContractDAO.get_all())


if __name__ == '__main__':
    unittest.main()