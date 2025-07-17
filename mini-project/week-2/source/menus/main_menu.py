from menus.utils import clear_screen
from menus.product_menu import show_product_menu
from menus.order_menu import show_orders_menu


# Main menu interface: handles main menu navigation and user actions.
def show_main_menu():
    while True:
        clear_screen()
        print("\n===== Main Menu =====")
        print("0. EXIT")
        print("1. View PRODUCT MENU options")
        print("2. View ORDERS MENU options")

        choice = input("\nSelect an option: ")

        if choice == "0":
            print("Exiting the main menu.")
            return #change to break?
        elif choice == "1":
            pass
            show_product_menu()
        elif choice == "2":
            pass
            show_orders_menu()
        else:
            print("\nInvalid choice. Please try again.")