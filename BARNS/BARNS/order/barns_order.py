import csv
import random
from typing import Union

import BARNS.customer.barns_cust
import BARNS.product.barns_product
import FileOperations


def customer_id():
    BARNS.product.barns_product.customerDisplayProducts()


def placeOrder():
    global shippingAddress, custEmail, orderNo, cartItem, row
    BARNS.product.barns_product.customerDisplayProducts()
    FileOperations.cust_order_header()
    cartDict = {}
    cartOrder: dict[str, dict[str, Union[str, int]]] = {}

    with open('products.csv', 'r', newline="") as f:
        next(f)
        f_list = list(f.readlines())
        # print(f_list)
    for product in f_list:
        productId = product.split(",")[0]
        productName = product.split(",")[1]
        productGender = product.split(",")[2]
        productPrice = product.split(",")[3]
        # print(f"{productId}: {productPrice}")
        cartDict.update({productId: int(productPrice)})

    option = input("Do you wish to proceed shopping ,Please enter your choice Y/N :").lower()
    finalCart = []
    while option == 'y':
        cartItem = input("Please Enter the Product Id you would like to shop :")
        shippingAddress = input("Please Enter your Shipping Address :")
        custEmail = input("Please re enter your registered email id :")
        orderNo = random.randint(0, 10)
        finalCart.append(cartItem)

        if cartItem.title() in cartDict:
            cartOrder.update(
                {cartItem: {'OrderNo': orderNo, 'Shipping Address': shippingAddress, 'custEmail': custEmail,
                            'Sub_total': cartDict[cartItem]}})

        else:
            print("Product Unavailable")
        option = input("Do you wish to continue shopping ? (Y/N) ")
    else:
        print("\n\n")
        print("********BILL SUMMARY***")
        print("\n")

        print('cartItem', 'orderNo', 'shippingAddress', 'custEmail', 'Sub_total')
        # Create an empty list for adding the subtotal
        total = []

        for key in cartOrder:
            print(
                f"{key} {cartOrder[key]['OrderNo']} {cartOrder[key]['Shipping Address']} {cartOrder[key]['custEmail']} {cartOrder[key]['Sub_total']}")

            row = [finalCart, orderNo, shippingAddress, custEmail, total]
            total.append(cartOrder[key]['Sub_total'])

        with open('order.csv', 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(row)
            # print(cartOrder[key]['Sub_total'])

        print("The Total Purchase Price is:", sum(total))

        print("\n \n End of shopping, Hope to see you back soon!!")
