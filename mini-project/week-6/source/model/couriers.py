from paths import courier_file
from classes.table_class import Table
from classes.menu_class import Menu


label='courier'
table_name='couriers'

couriers = Table(table_name)

courier_menu_options= {
                        "0": ("RETURN to main menu", ),
                        "1": (f"PRINT {label} list" , couriers.print_in_tabulated_view),
                        "2": (f"CREATE new {label}", couriers.add_item),
                        "3": (f"UPDATE existing {label}", couriers.update_item_by_index),
                        "4": (f"DELETE {label}", couriers.delete_item_by_index)
                    }

courier_menu = Menu (
    title=f"\n== {label.upper()}s menu ==\n",
    label=label,
    options=courier_menu_options
    )