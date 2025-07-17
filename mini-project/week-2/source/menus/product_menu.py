from menus.utils import clear_screen
from menus.utils import get_limited_digit_input, print_indexed_list

from products import crud, model


# Product menu interface: handles product menu navigation and user actions.
def show_product_menu():
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
            print_indexed_list(lst=model.original_products, list_title="products list")

        elif choice == "2":
            while True:
                product = input("Enter new product name: ").lower().strip()

                result=crud.add_product(products=model.original_products, new_product=product)
                model.original_products=result[0]
                status=result[1]

                if status:
                    print(f"Product '{product}' was successfully added to the product list.")
                else:
                    print(f"Product '{product}' wasn't added to the product list. It's already in the list.")    

                user_input = input("Would you like to add one more product to the product list? [y/n]: ").lower()
                if user_input != "y":
                    break

        elif choice == "3":
            print_indexed_list(lst=model.original_products, list_title="products list")

            index=get_limited_digit_input(limit=len(model.original_products), input_message="Enter an index of the product you would like to UPDATE: ")
            product = input("Enter new product name: ").lower().strip()
            old_product=model.original_products[index]
            
            result=crud.update_product_by_index(products=model.original_products, product_index=index, new_product=product)
            status=result[1]
            if status:
                model.original_products=result[0]
                print(f"Product '{old_product}' was successfully updated to '{product}'.")
            else:
                print(f"Product wasn't updated. '{product}' already exists in the list.")   

        elif choice == "4":
            print_indexed_list(lst=model.original_products, list_title="products list")
            index = get_limited_digit_input(limit=len(model.original_products), input_message="Enter an index of the product you would like to DELETE: ")
            
            product = model.original_products[index]
            user_input=input(f"Are you sure you want to delete '{product}' from product list? [y/n]:")
            if user_input.lower()=='y':
                del model.original_products[index]
                print(f"Product with index [{index}] - '{product}' - was successfully removed from product list.")
            else:
                print("Deletion has been canceled.")

        else:
            print("\nInvalid choice. Please try again.")