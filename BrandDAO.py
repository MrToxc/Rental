import database
from Brand import Brand

class BrandDAO:

    @staticmethod
    def get_all():
        brands = []
        with database.get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id_brand, name, category FROM brand")
            for row in cursor.fetchall():
                brands.append(Brand(row.name, row.category, row.id_brand))
        return brands

    @staticmethod
    def insert(brand):
        with database.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO brand (name, category) OUTPUT INSERTED.id_brand VALUES (?, ?)"
            cursor.execute(sql, (brand.name, brand.category))

            brand.id_brand = cursor.fetchone()[0]
            connection.commit()


    @staticmethod
    def delete(id_brand):
        with database.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "DELETE FROM brand WHERE id_brand = ?"
            cursor.execute(sql, (id_brand,))
            connection.commit()
            return cursor.rowcount > 0