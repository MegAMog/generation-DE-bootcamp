# Create, Read, Update, Delete or any other functions for orders
import menus.utils as utils
from orders.model import order_statuses, default_order_status
from tabulate import tabulate #https://pypi.org/project/tabulate/

# Print formatted order list (in table view). 
def print_orders(orders: list[dict]):
    print("\n== Orders list: ==\n")
    #Get list of unique keys across all dictionaries in list.
    unique_keys = set()
    for order in orders:
        unique_keys.update(order.keys())
    
    #Sort unique keys set.
    ordered_keys=sorted(unique_keys)
    
    #Create new list with dict, includes index and all unique keys.
    rows=[]
    for idx, order in enumerate(orders):
        new_row = {'index': idx}
        for key in ordered_keys:
            new_row[key] = order.get(key, "").title()
        rows.append(new_row)

    #Use tabulate function to print order list in nice format
    print(tabulate(rows, headers="keys", tablefmt="grid"))


#Add new order(dict) to existing order list.
#Return new list - copy of original with added order.
def add_order(orders:list, customer_attributes:dict, order_status=default_order_status)->list:
    #Add order attirbutes to order dict.
    order={'order_status':order_status}

    #Add customer attribute to order dict.
    order.update(customer_attributes)
    
    #Create new list with copy of original list + new 
    updated_orders=orders.copy()
    updated_orders.append(order)

    return updated_orders


#Validate order status.
def is_valid_order_status (status:str)->bool:
     if status in order_status:
          return True
     else:
          print(f"Order status should be from avaliable order status list:\n{order_status}")
          return False
     

#Validate order attributes.
def is_valid_order_attribute(attribute_name, attribute_value):
     if attribute_name=='customer_first_name' or attribute_name=='customer_last_name':
          return utils.is_valid_name(attribute_value)
     elif attribute_name=='customer_address':
          return utils.is_valid_address(attribute_value)
     elif attribute_name=='customer_phone_number':
          return utils.is_valid_phone_number(attribute_value)
     elif attribute_name=='order_status':
          return is_valid_order_status(attribute_value)
     else:
          return True
     

#Get input for order attributes and validate each according defined rules (function is_valid_customer_attribute(key, value), is_valid_order_status(key, value)).
#Return updated attributes - dictionary.
#Option: 
# -allow_blank=True - allows blank input, and corresponding key:value will be skipped; 
# -allow_blank=False - requires valid (non-blank and validated) input for each key
def get_valid_input_for_order_attributes(original_attributes:dict, allow_blank=False)->dict:
     updated_attributes={}

     for key in original_attributes.keys():
            while True:
                new_value=input(f"Enter value for {key.replace('_', ' ')}: ").strip().lower()
                if allow_blank and new_value == "":
                    break   
                elif is_valid_order_attribute(key, new_value):
                    updated_attributes[key]=new_value
                    break
     return updated_attributes
