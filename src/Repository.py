import atexit
import sqlite3

from src.Orders import Orders
from src.Suppliers import Suppliers
from src.Hats import Hats


class Repository:
    def __init__(self):
        self.conn = sqlite3.connect('ROCKER.db')
        self.hats = Hats(self.conn)
        self.suppliers = Suppliers(self.conn)
        self.orders = Orders(self.conn)

    def close(self):
        self.conn.commit()
        self.conn.close()

    def create_tables(self):
        self.conn.executescript("""
                                    CREATE TABLE  hats (id INTEGER PRIMARY KEY,
                                                        topping TEXT NOT NULL,
                                                        supplier INTEGER REFERENCES suppliers(id) ,
                                                        quantity INTEGER NUT NULL;
                                    CREATE TABLE suppliers (id INTEGER PRIMARY KEY, 
                                                            name TEXT NOT NULL;
                                    CREATE TABLE orders(id INTEGER PRIMARY KEY ,
                                                        location TEXT NOT NULL,
                                                        hat INTEGER REFERENCES hats(id); """
                                )


repo = Repository()
atexit.register(repo.close)
