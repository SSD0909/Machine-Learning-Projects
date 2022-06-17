import csv
from csv import DictWriter


def cust_signin_header():
    headerlist = ["Email", "Name", "Password", "Address"]
    with open('customer.csv', 'a', newline="") as f:
        dw = csv.DictWriter(f, delimiter=',', fieldnames=headerlist)
        if f.tell() == 0:
            dw.writeheader()


def cust_signin(row):
    with open('customer.csv', 'a', newline="") as f:
        writer = csv.writer(f)
        return writer.writerows(row)


def customer_read(cust_email, cust_password):
    with open('customer.csv', 'r', newline="", encoding="utf8") as f:
        found = 0
        dr = csv.reader(f, delimiter=",")
        next(dr)
        for i in dr:
            if i[0] == cust_email and i[2] == cust_password:
                found = 1
                print("Customer LoggedIn Successfully")
        if found == 0:
            print("Invalid Credentials")
        # for i in dr:
        # if cust_email in i['Email']:
        # return print("Logged In Successfully")
        # else:
        # continue


def product_write():
    fields = ['Product Id', 'Product Name', 'Gender', 'Price']

    outfit = [["1001", "Tops", "Female", 250],
              ["1002", "Pants", "Male", 500],
              ["1003", "Suit", "Male", 750],
              ["1004", "Shorts", "Female", 350],
              ["1005", "Skirts", "Female", 400]]

    with open('products.csv', 'a', newline="") as file:
        csvwriter = csv.writer(file)
        if file.tell() == 0:
            csvwriter.writerow(fields)
            csvwriter.writerows(outfit)


def product_read():
    with open('products.csv', 'r', newline="", encoding="utf8") as file:
        csv_reader = csv.reader(file)
        for lines in csv_reader:
            print(lines)


def new_product_write():
    fields = ['Product Id', 'Product Name', 'Gender', 'Price']

    new_product_id = input("Enter ProductId : ")
    new_product_name = input("Enter ProductName : ")
    new_gender = input("Enter Gender : ")
    new_price = int(input("Enter Price : "))

    row = {'Product Id': new_product_id, 'Product Name': new_product_name, 'Gender': new_gender, 'Price': new_price}
    with open('products.csv', 'a', newline="", encoding="utf-8") as file:
        writerobj = DictWriter(file, fieldnames=fields)
        writerobj.writerow(row)


def remove_product():
    p_id = input("Please Enter the Product id that has to be removed :")
    with open('products.csv', 'r', newline="", encoding="utf8") as f:
        read = csv.reader(f)

        found = 0
        new = []

        for i in read:
            if i[0] != p_id:
                new.append(i)
            else:
                found = 1
            if found == 0:
                print("Invalid")
            else:
                with open('products.csv', 'w', newline="", encoding="utf8") as file:
                    writer = csv.writer(file)
                    writer.writerows(new)
                    print("The Product is deleted")


def cust_order_header():
    headerlist = ["cartItem", "orderNo", "shippingAddress", "custEmail", "Sub_total"]
    with open('order.csv', 'w', newline="") as file:
        dw = csv.DictWriter(file, delimiter=',', fieldnames=headerlist)
        if file.tell() == 0:
            dw.writeheader()
