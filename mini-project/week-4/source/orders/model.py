import csv
from paths import order_file
from menus import utils
from menus.menu_class import Menu
from menus.entity_class import Orders
from products.model import products
from couriers.model import couriers

#Order statuses list (enum - ?, change to order status id)
order_statuses=['new', 'confirmed', 'preparing', 'ready for delivery', 'out for delivery', 'delivered', 'cancelled', 'delivery failed', 'refunded']

#Set deafult status
default_order_status_id=2
default_order_status=order_statuses[default_order_status_id]

#Original list of orders, each item(order) is dictionary
original_orders=[]
primary_key=''
label="order"

#Customer attributes structure
customer_attributes={
    'customer_first_name':'', 
    'customer_last_name':'', 
    'customer_address':'', 
    'customer_phone_number':''}

try:
    with open(order_file, "r") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        
        for row in reader:
            order = {}
            
            for key, value in row.items():
                value=value.strip()

                if key=='order_status':
                    if value in order_statuses:
                        order[key]=value
                    else:
                        order[key]=default_order_status

                elif utils.is_valid_attribute(key, value)[0]:
                    order[key]=value

                else:
                    order[key]=None

            original_orders.append(order)

except FileNotFoundError:
    #Create empty file if it doesn't exist
    with open(order_file, 'w') as file:
        pass
    print(f"File '{order_file}' not found. Created an empty file.")


orders = Orders (
    entity_name=label, 
    original_list=original_orders, 
    primary_key=primary_key,
    products=products,
    couriers=couriers)

order_menu_options= {
                        "0": ("RETURN to main menu", ),
                        "1": (f"PRINT {label} list" , orders.print_in_tabulated_view),
                        "2": (f"CREATE new {label}", orders.add_item),
                        "3": (f"UPDATE existing {label} status", orders.update_order_status),
                        "4": (f"UPDATE existing {label}", orders.update_item_by_index),
                        "5": (f"DELETE {label}", orders.delete_item_by_index)
                    }

order_menu = Menu (
    title="\n== ORDERs menu ==\n",
    label=label,
    options=order_menu_options
    )