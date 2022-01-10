from src.Hat import Hat


class Hats:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, hatDTO):
        self.conn.execute("""
                             INSERT INTO hats (id,topping,supplier,quantity) VALUES (?, ?, ?, ?)""",
                          [hatDTO.id, hatDTO.topping, hatDTO.supplier, hatDTO.quantity])

    def find(self, id):
        c = self.conn.cursor()
        c.execute("""
                     SELECT id,topping,supplier,quantity FROM hats WHERE num = ?""", [id])
        return Hat(*c.fetchone())
