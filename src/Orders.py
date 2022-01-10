from Order import Order


class Orders:
        def __init__(self, conn):
            self.conn = conn

        def insert(self, orderDTO):
            self.conn.execute("""
                                 INSERT INTO orders (id, location, hat) VALUES (?, ?, ?)""",
                              [orderDTO.id, orderDTO.location, orderDTO.hat])

        def find(self, id):
            c = self.conn.cursor()
            c.execute("""
                         SELECT id,location,hat FROM hats WHERE num = ?""", [id])
            return Order(*c.fetchone())