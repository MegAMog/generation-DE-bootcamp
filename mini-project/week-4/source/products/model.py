import csv
from paths import product_file
from menus import utils
from menus.menu_class import Menu
from menus.entity_class import BaseEnity

# Load data from product csv-file into list of dict
original_products = []
primary_key='product_name'
label='product'

try:
    with open(product_file, "r") as file:
        reader = csv.DictReader(file, skipinitialspace=True)

        for row in reader:
            product={}

            for key, value in row.items():
                value=value.strip()

                if key=='price':
                    if utils.is_valid_price(value)[0]:
                        product[key]=float(value)
                    else:
                        product[key]=0.0

                elif utils.is_valid_attribute(key, value)[0]:
                    product[key]=value

                else:
                    product[key]=None
            
            original_products.append(product)

except FileNotFoundError:
    #Create empty file if it doesn't exist.
    with open(product_file, 'w') as file:
        pass
    print(f"File '{product_file}' not found. Created an empty file.")


products = BaseEnity (
    entity_name=label, 
    original_list=original_products, 
    primary_key=primary_key)

product_menu_options= {
                        "0": ("RETURN to main menu", ),
                        "1": (f"PRINT {label} list" , products.print_in_tabulated_view),
                        "2": (f"CREATE new {label}", products.add_item),
                        "3": (f"UPDATE existing {label}", products.update_item_by_index),
                        "4": (f"DELETE {label}", products.delete_item_by_index)
                    }

product_menu = Menu (
    title="\n== PRODUCTs menu ==\n",
    label="product",
    options=product_menu_options
    )