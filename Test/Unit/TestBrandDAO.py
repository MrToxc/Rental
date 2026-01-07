import unittest
from BrandDAO import BrandDAO
from Brand import Brand


class TestBrandDAO(unittest.TestCase):
    def test_insert_delete_find(self):
        bmw = Brand("BMW", "Luxury")
        BrandDAO.insert(bmw)
        try:
            self.assertTrue(bmw.id_brand is not None and bmw.id_brand >= 0)
            brands = BrandDAO.get_all()
            self.assertTrue(bmw in brands)
        finally:
            BrandDAO.delete(bmw.id_brand)









if __name__ == '__main__':
    unittest.main()