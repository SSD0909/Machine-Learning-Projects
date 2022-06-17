import BARNS.customer.barns_cust
import FileOperations

rows = []


def customerDisplayProducts():
    FileOperations.product_write()
    FileOperations.product_read()


def adminDisplayProducts():
    FileOperations.product_write()
    FileOperations.product_read()


def addProducts():
    FileOperations.new_product_write()
    adminDisplayProducts()


def removeProduct():
    FileOperations.remove_product()
    adminDisplayProducts()


def logout():
    BARNS.customer.barns_cust.adminLogin()
