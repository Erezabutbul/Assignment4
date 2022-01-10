import sqlite3
from Repository import repo
import os

from src.Hat import Hat
from src.Supplier import Supplier


def initialize(dir):
    config = open(dir, "r")
    instructions = config.readline(0)
    (numOfHats, numOfSuppliers) = instructions.split(",")
    for i in range(1, numOfHats):
        hat = config.readline(i)
        (id, topping, supplier, quantity) = hat.split(",")
        hatDTO = Hat(id, topping, supplier, quantity)
        repo.hats.insert(hatDTO)

    for j in range(numOfHats + 1, numOfHats + numOfSuppliers):
        supplier = config.readline(j)
        (id, name) = supplier.split(",")
        supplierDTO = Supplier(id, name)
        repo.suppliers.insert(supplierDTO)


if __name__ == '__main__':
    initialize("C:\\Users\\Erez\\PycharmProjects\\Assignment4\\textFiles\\config.txt")
