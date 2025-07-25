# from utils.utils import clear_screen
from model import products as p
from model import couriers as c
from model import orders as o
from classes.menu_class import Menu


# # Main menu interface: handles main menu navigation and user actions.
# def show_main_menu():
#     while True:
#         clear_screen()
#         print("\n===== Main Menu =====")
#         print("0. EXIT")
#         print("1. View PRODUCT MENU options")
#         print("2. View COURIER MENU options")
#         print("3. View ORDERS MENU options")

#         choice = input("\nSelect an option: ")

#         if choice == "0":
#             print("Exiting the main menu.")
#             return

#         elif choice == "1":
#             #Open the products menu
#             p.product_menu.call_menu()

#         elif choice == "2":
#             #Open the couriers menu
#             c.courier_menu.call_menu()

#         elif choice == "3":
#             #Open tht orders menu
#             o.order_menu.call_menu()

#         else:
#             print("\nInvalid choice. Please try again.")


main_menu_options={
                        "0": ("EXIT", ),
                        "1": (f"View PRODUCT MENU options" , p.product_menu.call_menu),
                        "2": (f"View COURIER MENU options", c.courier_menu.call_menu),
                        "3": (f"View ORDERS MENU options", o.order_menu.call_menu),
                    }

main_menu = Menu (
    title="\n== Main Menu ==\n",
    label="",
    options=main_menu_options
    )
