from paths import product_file
from classes.table_class import Table
from classes.menu_class import Menu


label='product'
table_name='products'

products = Table (table_name)

product_menu_options= {
                        "0": ("RETURN to main menu", ),
                        "1": (f"PRINT {label} list" , products.print_in_tabulated_view),
                        "2": (f"CREATE new {label}", products.add_item),
                        "3": (f"UPDATE existing {label}", products.update_item_by_index),
                        "4": (f"DELETE {label}", products.delete_item_by_index)
                    }

product_menu = Menu (
    title=f"\n== {label.upper()}s menu ==\n",
    label=label,
    options=product_menu_options
    )
