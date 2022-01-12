import atexit
import os.path
import sqlite3

from src.Order import Order
from src.Orders import Orders
from src.Suppliers import Suppliers
from src.Hats import Hats


class Repository:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.hats = Hats(self.conn)
        self.suppliers = Suppliers(self.conn)
        self.orders = Orders(self.conn)
        self.orderCounter = 1

    def close(self):
        self.conn.commit()
        self.conn.close()

    def create_tables(self):
        self.cursor.executescript("""
                                    CREATE TABLE hats (id INT PRIMARY KEY,
                                                        topping TEXT NOT NULL,
                                                        supplier INT,
                                                        quantity INT NOT NULL,
                                                        FOREIGN KEY(supplier) REFERENCES suppliers(id));
                                    CREATE TABLE suppliers (id INT PRIMARY KEY, 
                                                            name TEXT NOT NULL);
                                    CREATE TABLE orders(id INT PRIMARY KEY ,
                                                        location TEXT NOT NULL,
                                                        hat INT,
                                                        FOREIGN KEY(hat) REFERENCES hats(id)); """
                                  )

    def executeOrder(self, location, topping):
        self.cursor.execute("""
                            SELECT id,supplier
                            FROM hats
                            WHERE topping=?
                            ORDER BY supplier
                            LIMIT 1""", [topping])
        list = self.cursor.fetchone()
        idOfhat = list[0]
        supplier = list[1]
        order = Order(self.orderCounter, location, idOfhat)
        self.cursor.execute("""INSERT INTO orders VALUES(?,?,?)""", [order.id, order.location, order.hat])
        repo.orderCounter += 1
        self.cursor.execute("""SELECT quantity FROM hats WHERE id =?""", [idOfhat])
        quantity = self.cursor.fetchone()[0]
        if quantity == 1:
            self.cursor.execute("""DELETE FROM hats WHERE id=?""", [idOfhat])
        else:
            self.cursor.execute("""
                                 UPDATE hats SET quantity =? WHERE id =?""", [(int(quantity) - 1), idOfhat])
        Summary = open("summary.txt", "a")
        self.cursor.execute("""SELECT name FROM suppliers WHERE id=?""", [supplier])
        supplierName = self.cursor.fetchone()[0]
        Summary.write(str(topping) + "," + str(supplierName) + "," + str(location) + "\n")


repo = Repository()
atexit.register(repo.close)
