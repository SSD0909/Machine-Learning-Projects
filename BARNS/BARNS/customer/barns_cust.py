import BARNS.product.barns_product
import BARNS.order.barns_order


def adminLogin():
    print("*********************")
    print("1.Display BARNS Products")
    print("2.Add Products")
    print("3.Remove Product")
    print("4.Logout")
    print("*********************")


def adminOption():
    option = int(input("Please enter admin choice : "))
    if option == 1:
        BARNS.product.barns_product.adminDisplayProducts()
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminOption()
    elif option == 2:
        BARNS.product.barns_product.adminDisplayProducts()
        print("\n***************************************************\n")
        BARNS.product.barns_product.addProducts()
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminOption()
    elif option == 3:
        BARNS.product.barns_product.adminDisplayProducts()
        print("\n***************************************************\n")
        BARNS.product.barns_product.removeProduct()
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminOption()
    elif option == 4:
        logout()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n***************************************************\n")
        adminLogin()
        print("\n***************************************************\n")
        adminOption()


def customerLogin():
    print("*********************\n")
    print("1.Display Products")
    print("2.Place order")
    print("3.Logout")
    print("\n*********************")


def customerOption():
    option = int(input("Please enter customer option : "))
    if option == 1:
        BARNS.product.barns_product.customerDisplayProducts()
        print("\n***************************************************\n")
        customerLogin()
        print("\n***************************************************\n")
        customerOption()
    elif option == 2:
        BARNS.order.barns_order.placeOrder()
        print("\n***************************************************\n")
        customerLogin()
        print("\n***************************************************\n")
        customerOption()
    elif option == 3:
        logout()
    else:
        print("Invalid Choice. Please enter valid choice")


def logout():
    loginCustomer()


def loginCustomer():
    BARNS.product.barns_product.customerDisplayProducts()
    # product_id=int(input("Enter product id"))
