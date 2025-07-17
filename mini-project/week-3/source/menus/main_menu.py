from menus.utils import clear_screen
from menus.sub_menu import show_sub_menu
from menus.order_menu import show_orders_menu
from menus.utils import save_list_to_file
import paths
from products import model as p
from couriers import model as c


# Main menu interface: handles main menu navigation and user actions.
def show_main_menu():
    while True:
        clear_screen()
        print("\n===== Main Menu =====")
        print("0. EXIT")
        print("1. View PRODUCT MENU options")
        print("2. View COURIER MENU options")
        print("3. View ORDERS MENU options")

        choice = input("\nSelect an option: ")

        if choice == "0":
            confirmation=input("Would you like to save the changes you made to the products list? [y/n] :")
            if confirmation.strip().lower()=='y':
                save_list_to_file(paths.product_file, p.original_products)
                print("The products list has been successfully updated.")
            
            confirmation=input("Would you like to save the changes you made to the courier list? [y/n] :")
            if confirmation.strip().lower()=='y':
                save_list_to_file(paths.courier_file, c.original_couriers)
                print("The couriers list has been successfully updated.")

            print("Exiting the main menu.")
            return

        elif choice == "1":
            #Open the products menu
            show_sub_menu(p.original_products, "product")

        elif choice == "2":
            #Open the couriers menu
            show_sub_menu(c.original_couriers, "couriers")

        elif choice == "3":
            #Open tht orders menu
            show_orders_menu()

        else:
            print("\nInvalid choice. Please try again.")