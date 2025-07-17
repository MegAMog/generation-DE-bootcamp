import os
import time

# Predifined products list
products = ["mocha", "americano", "flat white", "latte"]


# Print the product list. 
# Option: 0 - display indexes and product names, 1 - display numbering from 1 and product names.
def print_products(products: list, option: int):
    print("\n== Product list: ==")
    for idx, product in enumerate(products):
        print(f"{idx+option}. {product}".title())


# Add new product to the product list.
def add_product(new_product: str, products: list):
    product = new_product.lower()

    if product not in products:
        products.append(product)
        print(f"Product '{product}' was successfully added to the product list.")
    else:
        print(f"Product '{product}' wasn't added. It is already in the product list.")


# Update product name by index.
def update_product_by_idx(product_idx: int, new_product: str, products: list):
    if product_idx >= 0 and product_idx < len(products):
        old_product = products[product_idx]
        products[product_idx] = new_product.lower()
        print(
            f"Product with index [{product_idx}] - '{old_product}' - was successfully changed to '{new_product.lower()}'."
        )
    else:
        print(f"Product index [{product_idx}] is out of product list range.")


# Delete product by index.
def del_product_by_index(product_idx: int, products: list):
    if product_idx >= 0 and product_idx < len(products):
        product = products[product_idx]
        chioce=input(f"Are you sure you want to delete '{product}' from product list? [y/n]:")
        if chioce.lower()=='y':
            del products[product_idx]
            print(
                f"Product with index [{product_idx}] - '{product}' - was successfully removed from product list."
            )
        else:
            print("Deletion has been canceled.")
    else:
        print(
            f"Product index [{product_idx}] is out of product list range."
        )


# Clear screen function.
def clear_screen():
    #This solution will not clear screen properly, it will leave opportunity to scroll back.
    os.system('cls' if os.name == 'nt' else 'clear')
    # This solution will clean screen properly, but it looks strange.
    #print("\033c\033[3J")


# Validate input and ask for new untill get value int>0.
def return_int_input(message:str):
    while True:
        user_input = input(message)
        if user_input.isnumeric(): 
            indx = int(user_input)
            break
        else:
            print("Invalid index.")
    return indx


# Main menu interface: handles main menu navigation and user actions.
def main_menu():
    while True:
        clear_screen()
        print("\n===== Main Menu =====")
        print("0. EXIT")
        print("1. View PRODUCT MENU options")

        choice = input("\nSelect an option: ")

        if choice == "0":
            print("Exiting the main menu.")
            return #change to break?
        elif choice == "1":
            product_menu()
        else:
            print("\nInvalid choice. Please try again.")


# Product menu interface: handles product menu navigation and user actions.
def product_menu():
    clear_screen()
    print("\n===== Product Menu =====")
    print("0. RETURN to main menu")
    print("1. PRINT products list")
    print("2. CREATE new product")
    print("3. UPDATE existing product")
    print("4. DELETE product")

    while True:
        choice = input("\nSelect an option from product menu: ")

        if choice == "0":
            return

        elif choice == "1":
            print_products(products, 1)
            time.sleep(3)

        elif choice == "2":
            while True:
                product = input("Enter the product name: ")
                add_product(product, products)

                choice = input(
                    "Would you like to add one more product to the product list? [y/n]: "
                ).lower()
                if choice != "y":
                    break

        elif choice == "3":
            print_products(products, 0)
            indx=return_int_input("Enter an index for product you would like to update: ")
            product = input("Enter new product name: ")
            update_product_by_idx(indx, product, products)

        elif choice == "4":
            print_products(products, 0)
            indx = return_int_input("Enter an index for product you would like to delete: ")
            del_product_by_index(indx, products)
        else:
            print("\nInvalid choice. Please try again.")


#Main program
main_menu()

