import csv
from paths import courier_file
from menus import utils
from menus.menu_class import Menu
from menus.entity_class import BaseEnity

# Load data from courier csv-file into list of dict
original_couriers=[]
primary_key=''

label='courier'

try:
    with open(courier_file, "r") as file:     
        reader = csv.DictReader(file, skipinitialspace=True)
        
        for row in reader:
            courier={}

            for key, value in row.items():
                value=value.strip()

                if utils.is_valid_attribute(key, value)[0]:
                    courier[key]=value
                else:
                    courier[key]=None
            
            original_couriers.append(courier)

except FileNotFoundError:
    #Create empty file if it doesn't exist
    with open(courier_file, 'w') as file:
        pass
    print(f"File '{courier_file}' not found. Created an empty file.")


couriers = BaseEnity (
    entity_name=label, 
    original_list=original_couriers, 
    primary_key=primary_key)

courier_menu_options= {
                        "0": ("RETURN to main menu", ),
                        "1": (f"PRINT {label} list" , couriers.print_in_tabulated_view),
                        "2": (f"CREATE new {label}", couriers.add_item),
                        "3": (f"UPDATE existing {label}", couriers.update_item_by_index),
                        "4": (f"DELETE {label}", couriers.delete_item_by_index)
                    }

courier_menu = Menu (
    title="\n== COURIERs menu ==\n",
    label=label,
    options=courier_menu_options
    )