from classes.table_class import Table
from classes.menu_class import Menu
from model.products import products
from model.couriers import couriers
from utils.utils import is_valid_attribute
import psycopg
from tabulate import tabulate


label="order"
table_name='orders'

#Child class (from Table) to specify/redefine some methods to use in orders table 
class Orders(Table):
    def __init__(self, name, products:Table, couriers:Table, order_status:Table):
        super().__init__(name)


    #Get user input for data to INSERT/UPDATE in table
    # -allow_blank=True - allows blank input, and corresponding column:value will be skipped; 
    # -allow_blank=False - requires valid (non-blank) input for each key  
    def get_user_input(self, allow_blank=False):
        #Get column names, which is not SERIAL
        column_names =[]
        #Skip all SERIAL columns + order_date, order_status_id - to use DEFAULT values
        for decription in  self.columns_description:
            if decription[2]!='nextval' and decription[0]!='order_date' and decription[0]!='order_status_id':
                column_names.append(decription[0])
        
        columns = []
        row=[]

        for column in column_names:
                #Get input for product_ids - convert to comma-separated ids of product
                if column=='product_ids':
                    products.print_in_tabulated_view()

                    product_snapshot=[]
                    while True:
                        product_id = input(f"Product id: ")
                        product_id = product_id.strip()

                        if allow_blank and product_id == "":
                            break   
                        elif product_id.isdigit():
                            #Check that user input in avaliable list
                            avaliable_product_ids=products.get_primary_key_values()[0]
                            if int(product_id) in avaliable_product_ids:
                                product_snapshot.append(product_id)
                                
                                add_more=input("Would you like to add more products? [y/n]: ")
                                if add_more.strip().lower()!='y':
                                    break
                            
                            else:
                                print("Product id must be from avaliable list.")  
                        else:
                            print("Product id must be index.")
                    
                    if product_snapshot:
                        value=','.join(product_snapshot)
                        row.append(value)
                        columns.append(column)

                #Get input for courier_id     
                elif column=='courier_id':
                        couriers.print_in_tabulated_view()

                        while True:
                            value = input(f"Enter {column.replace('_', ' ')}: ")
                            value = value.strip()

                            if allow_blank and value == "":
                                break   
                            elif value.isdigit():
                                #Check that user input in avaliable list
                                avaliable_courier_ids=couriers.get_primary_key_values()[0]
                                if int(value) in avaliable_courier_ids:
                                    row.append(int(value))
                                    columns.append(column)
                                    break
                                else:
                                    print("Courier id must be from avaliable list.")

                #Get input for other columns
                else:
                    while True:
                        value = input(f"Enter {column.replace('_', ' ')}: ")
                        value = value.strip()

                        if allow_blank and value == "":
                            break   
                        elif is_valid_attribute(column, value)[0]:
                            row.append(value)
                            columns.append(column)
                            break
                        else:
                            print(is_valid_attribute(column, value)[1])

        return columns, row
    
    #Update order status id
    def update_order_status(self):
        #Print out orders table
        orders.print_in_tabulated_view()
        #Get order_id for row to update
        update_conditions=self.get_user_primary_key_values()

        #Print avaliable list of order status values with ids
        order_status.print_in_tabulated_view()

        row=[]
        column_name='order_status_id'

        while True:
            value = input(f"Enter index for order status: ")
            value = value.strip()

            if value.isdigit():
                 #Check that user input in avaliable list
                avaliable_status_ids=order_status.get_primary_key_values()[0]
                if int(value) in avaliable_status_ids:
                    row.append(int(value))
                    break
                else:
                    print("Order status id must be from avaliable list.")
        
        try:
            #Establish connection with DB and UPDATE row
            with psycopg.connect(f"""
                host={self.host_name}
                port={self.port}
                dbname={self.database_name}
                user={self.user_name}
                password={self.user_password}
                """) as connection:
                
                cursor = connection.cursor()

                #SET clause
                set_clause =f"{column_name} = %s"

                #WHERE clause
                condition=[]
                for item in update_conditions.keys():
                    condition.append(f"{item} = %s")
                
                where_clause = " AND ".join(condition)

                
                sql = f"""
                UPDATE {self.name}
                SET {set_clause}
                WHERE {where_clause}
                RETURNING *;
                """

                cursor.execute(sql, row+list(update_conditions.values()))
                # Get list of updated rows
                updated_rows = cursor.fetchall()

                connection.commit()

                if updated_rows:
                    print(f"Updated {len(updated_rows)} row(s):")
                    print(tabulate(updated_rows, tablefmt="grid"))
                else:
                    print("No rows matched the condition. Nothing was updated.")

                cursor.close()
            
        except Exception as ex:
            print('Failed to:', ex)


    
order_status = Table ('order_status')
orders = Orders (table_name, products, couriers, order_status)


order_menu_options= {
                        "0": ("RETURN to main menu", ),
                        "1": (f"PRINT {label} list" , orders.print_in_tabulated_view),
                        "2": (f"CREATE new {label}", orders.add_item),
                        "3": (f"UPDATE existing {label} status", orders.update_order_status),
                        "4": (f"UPDATE existing {label}", orders.update_item_by_index),
                        "5": (f"DELETE {label}", orders.delete_item_by_index)
                    }


order_menu = Menu (
    title=f"\n== {label.upper()}s menu ==\n",
    label=label,
    options=order_menu_options
    )
