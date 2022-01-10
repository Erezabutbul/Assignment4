from Supplier import Supplier


class Suppliers:
        def __init__(self, conn):
            self.conn = conn

        def insert(self, supplierDTO):
            self.conn.execute("""
                                 INSERT INTO suppliers (id, name) VALUES (?, ?)""",
                              [supplierDTO.id, supplierDTO.name])

        def find(self, id):
            c = self.conn.cursor()
            c.execute("""
                         SELECT id,name FROM hats WHERE num = ?""", [id])
            return Supplier(*c.fetchone())