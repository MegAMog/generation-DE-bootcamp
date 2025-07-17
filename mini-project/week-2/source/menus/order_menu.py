import time
from menus.utils import clear_screen, print_indexed_list
from menus.utils import get_limited_digit_input

from orders import model
from orders import crud


#Orders menu interface: handles product menu navigation and user actions.
def show_orders_menu():
    clear_screen()
    print("\n===== Orders Menu =====")
    print("0. RETURN to main menu")
    print("1. PRINT orders list")
    print("2. CREATE new order")
    print("3. UPDATE existing order status")
    print("4. UPDATE existing order details")
    print("5. DELETE existing order by index")

    while True:
        choice = input("\nSelect an option from orders menu: ")

        if choice == "0":
            return

        elif choice == "1":
            print_indexed_list(lst=model.original_orders, list_title='orders')

        elif choice == "2":
            #Gets pre-defined customer attributes structure from model module.
            customer_attributes=dict.fromkeys(model.customer_attributes.keys(),'')
            
            #Takes inputs for customer attributes and validates the value.
            customer_attributes=crud.get_valid_input_for_order_attributes(original_attributes=customer_attributes, allow_blank=False)

            #Creates new item in order list (dict) with customer attributes and default order status.    
            model.original_orders=crud.add_order(orders=model.original_orders, customer_attributes=customer_attributes, order_status=model.default_order_status)
            print(f"The new order was successfully added to the order list with '{model.default_order_status}' status.")

        elif choice == "3":
            orders=model.original_orders

            #Prints current orders list and asks for valid order index. 
            print_indexed_list(lst=orders, list_title='orders')
            order_index=get_limited_digit_input(limit=len(orders), input_message="Enter an index for order you would like to UPDATE: ")

            #Prints status order list and asks for valid order status index.
            print_indexed_list(lst=model.order_status, list_title="order status")
            status_index=get_limited_digit_input(limit=len(model.order_status), input_message="Enter an index for order status: ")
            new_status=model.order_status[status_index]

            #Saves old order status value to show in message after completition. 
            old_status=orders[order_index].get('order_status')

            #Updates order status in current order list.
            orders[order_index]['order_status']=new_status
            print(f"Order #[{order_index}] successfully changed status from '{old_status}' to '{new_status}'.")

        elif choice == "4":
            orders=model.original_orders

            #Prints current orders list and asks for valid order index. 
            print_indexed_list(lst=orders, list_title='orders')
            order_index=get_limited_digit_input(limit=len(orders), input_message="Enter an index for order you would like to UPDATE: ")

            #Gets value(dict) for choosen order.
            order=orders[order_index]

            #Get valid order attributes and updates choosen order.
            updated_order=crud.get_valid_input_for_order_attributes(original_attributes=order, allow_blank=True)
            orders[order_index].update(updated_order)
            print(f"Order with index [{order_index}] was successfully updated to  \n'{orders[order_index]}'\n.")
 
        elif choice == "5":
            orders=model.original_orders

            #Prints current orders list and asks for valid order index. 
            print_indexed_list(lst=orders, list_title='orders')
            order_index=get_limited_digit_input(limit=len(orders), input_message="Enter an index for order you would like to DELETE: ")
            
            #Gets value(dict) for choosen order to show later in message.
            order=orders[order_index]

            #Confirms deletion and delete choosen order.
            if input(f"Are you sure you want to delete \n'{order}' \nfrom product list? [y/n]:").lower() == 'y':
                del orders[order_index]
                print(f"Order with index [{order_index}]: \n'{order}'\n was successfully removed from order list.")
            else:
                print("Deletion has been canceled.")

        else:
            print("\nInvalid choice. Please try again.")