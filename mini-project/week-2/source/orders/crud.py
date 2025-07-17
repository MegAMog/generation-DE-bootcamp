# Create, Read, Update, Delete functions for orders
import menus.utils as utils
from orders.model import order_status, default_order_status

# # PRINT the orders list. 
# # Option: 0 - display indexes and order details, 1 - display numbering from 1 and order details.
# def print_orders(orders: list, option=0):
#     print("\n== Orders list: ==")
#     for idx, order in enumerate(orders):
#         print(f'| {idx+option}', end=" | ")
#         for key, value in order.items():
#             print(f'{key}: {value}', end=" | ")
        # print()

#Add new order to the order list.
#Return new list - copy of original with added order.
def add_order(orders:list, customer_attributes:dict, order_status=default_order_status)->list:
    order={'order_status':order_status}
    order.update(customer_attributes)
    
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
     

#Gets input for order attributes and validate each according defined rules (function is_valid_customer_attribute(key, value), is_valid_order_status(key, value)).
#Returns updated attributes - dictionary.
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
