import sqlite3
from Repository import repo
import os

from src.Hat import Hat
from src.Supplier import Supplier


def initialize(dir):
    repo.create_tables()
    config = open(dir, "r")
    text = config.readlines()
    (numOfHats, numOfSuppliers) = text[0].split(",")
    numOfSuppliers = numOfSuppliers[0: len(numOfSuppliers) - 1]  # stripping the '\n'
    for i in range(1, int(numOfHats)+1):
        hat = text[i]
        (id, topping, supplier, quantity) = hat.split(",")
        quantity = quantity[0: len(quantity) - 1]  # stripping the '\n'
        hatDTO = Hat(id, topping, supplier, quantity)
        repo.hats.insert(hatDTO)

    for j in range(int(numOfHats) + 1, int(numOfHats) + int(numOfSuppliers)+1):
        supplier = text[j]
        (id, name) = supplier.split(",")
        name = name[0: len(name) - 1]
        supplierDTO = Supplier(id, name)
        repo.suppliers.insert(supplierDTO)


if __name__ == '__main__':
    initialize("..\\textFiles\\config.txt")
