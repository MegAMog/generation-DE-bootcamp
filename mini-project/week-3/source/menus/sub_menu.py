from menus.utils import clear_screen
from menus.utils import get_limited_digit_input, print_indexed_list

# Parametrized function for sub menu interface: handles product/couriers menu navigation and user actions.
# Pararmeters:
# - original list (product, couriers)
# - text label to show in prompts and titles.
def show_sub_menu(original_list:list, list_label:str):
    label=list_label.strip().lower()

    while True:
        clear_screen()

        print(f"\n===== {label.title()} Menu =====")
        print("0. RETURN to main menu")
        print(f"1. PRINT {label} list")
        print(f"2. CREATE new {label}")
        print(f"3. UPDATE existing {label}")
        print(f"4. DELETE {label}")

        choice = input(f"\nSelect an option from {label} menu: ")

        if choice == "0":
            return

        elif choice == "1":
            #Print out list
            print_indexed_list(original_list, label)
            input()

        elif choice == "2":
            #Add new items to list
            while True:
                new_item = input(f"Enter new {label} name: ").strip().lower()

                #Skip adding item if it already exists in list or add item if doesn't.
                if new_item in original_list:
                    print(f"'{new_item}' wasn't added to the {label} list. It's already in the list.")  
                else:
                    original_list.append(new_item)
                    print(f"'{new_item}' was successfully added to the {label} list.")

                confirmation = input(f"Would you like to add one more items to the {label} list? [y/n]: ").lower()
                if confirmation != "y":
                    break

        elif choice == "3":
            #Print out list
            print_indexed_list(original_list, label)

            #Get valid index for item to update and new value
            msg="Enter an index of the "+label+" you would like to UPDATE: "
            index=get_limited_digit_input(limit=len(original_list), input_message=msg)
            new_item = input(f"Enter new {label} name: ").lower().strip()
            
            #Save old item to show in prompt later
            old_item=original_list[index]
            
            #Skip update if same value already exists in list or update item if doesn't.
            if new_item in original_list:
                print(f"{label.title()} wasn't updated. '{new_item}' already exists in the list.")
            else:
                original_list[index]=new_item
                print(f"{label.title()} '{old_item}' was successfully updated to '{new_item}'.")   
            
            input()

        elif choice == "4":
            #Print out list
            print_indexed_list(original_list, label)

            #Get valid index for item to delete
            msg="Enter an index of the "+label+" you would like to DELETE: "
            index = get_limited_digit_input(limit=len(original_list), input_message=msg)
            
            #Get item value to show in prompt and verify that user wants to delete this item
            new_item = original_list[index]
            confirmation=input(f"Are you sure you want to delete '{new_item}' from {label} list? [y/n]:")

            #Remove item if user confirmed deletion
            if confirmation.lower()=='y':
                del original_list[index]
                print(f"{label} with index [{index}] - '{new_item}' - was successfully removed from {label} list.")
            else:
                print("Deletion has been canceled.")
            
            input()

        else:
            print("\nInvalid choice. Please try again.")