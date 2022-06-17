import FileOperations
import BARNS.customer.barns_cust
import BARNS.order.barns_order

print("\n*********************************************************************************")
print("-------------------WELCOME TO BARNS ONLINE SHOPPING--------------------------------")
print("*********************************************************************************")
print("----------------Don’t have an account?Become a BARNS member, click Enter-----------")
print("*********************************************************************************\n")

while True:
    option = input("Would you like to Signup or Are you an existing customer(signin, login), "
                   "Login as an admin(Admin)?/" "press e to Exit:").lower()

    if option == 'e':
        break
    if option == 'admin':
        admin_password = input("Enter your admin password:")
        if admin_password == 'admin@123':
            BARNS.customer.barns_cust.adminLogin()
            BARNS.customer.barns_cust.adminOption()
        else:
            print("Invalid password", "Try again")

    if option == "signin":
        try:
            FileOperations.cust_signin_header()
            email = input("Enter Email id")
            name = input("Enter User Name")
            password = input("Enter Password")
            address = input("Enter Address")

            row = [[email, name, password, address]]

            FileOperations.cust_signin(row)
        except FileNotFoundError as e:
            print(e)
    elif option == "login":
        try:
            print("****Enter Customer Credentials****, Press Enter")

            cust_email = input("Enter Email id : ")
            cust_password = input("Enter the password : ")
            FileOperations.customer_read(cust_email, cust_password)

            BARNS.customer.barns_cust.customerLogin()
            BARNS.customer.barns_cust.customerOption()

        except FileNotFoundError as e:
            print(e)
    elif option != "login" and option != "signin" and option != "admin":
        break
