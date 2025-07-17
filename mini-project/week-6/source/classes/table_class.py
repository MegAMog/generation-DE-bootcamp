#Create class to work with tables
import os
import psycopg
from dotenv import load_dotenv
from paths import env_path
from tabulate import tabulate #https://pypi.org/project/tabulate/
from utils.utils import is_valid_attribute, format_case

#Main class for managing and manipulating tables
class Table():
    # Load environment variables from .env file
    load_dotenv(dotenv_path=env_path)

    host_name = "localhost"
    port = os.getenv("HOST_PORT", "5434")
    database_name = os.environ.get("POSTGRES_SCHEMA")
    user_name = os.environ.get("POSTGRES_USER")
    user_password = os.environ.get("POSTGRES_PASSWORD")

    #Table:
    #1. name - table name
    #2. columns_description - column names, data type, column default value (will return nextval if column is SERIAL)
    #3. primary_key_columns - column names, that are PRIMARY KEYs in table
    #4. primary_key_values - nested list holding sets of primary key values for each primary key column, in order
    #5. serial_columns - column names, that are SERIAL in table
    def __init__(self, name:str):
        self.name = name.strip().lower()
        self.columns_description = self.get_column_names_and_metadata()
        self.primary_key_columns = self.get_primary_key_columns()
        self.primary_key_values = self.get_primary_key_values()

        #Get list of SERIAL columns from columns_description
        self.serial_columns = []
        for description in self.columns_description:
            if description[2]=='nextval':
                self.serial_columns.append((description[0]))

        
    #Get user input for data to INSERT/UPDATE in table (all columns except SERIAL)
    # -allow_blank=True - allows blank input, and corresponding column:value will be skipped; 
    # -allow_blank=False - requires valid (non-blank) input for each key  
    def get_user_input(self, allow_blank=False):
        #Get column names, which is not SERIAL
        column_names =[]
        for decription in  self.columns_description:
            if decription[2]!='nextval':
                column_names.append(decription[0])
        
        columns = []
        row=[]

        #Prompt user to enter valid values for each non-SERIAL column in the table
        for column in column_names:
            while True:
                value = input(f"Enter {column.replace('_', ' ')}: ")
                value = value.strip()

                if allow_blank and value == "":
                    break   
                else:
                    valid, message = is_valid_attribute(column, value)
                    if valid:
                        formated_value=format_case(column, value)
                        row.append(formated_value)
                        columns.append(column)
                        break
                    else:
                        print(message)

        return columns, row


    #Get and return table column names as list of tuples: [(column name, data type, default value)]
    #Note that default value:
    #-'nextval' if column is SERIAL
    #-exact value if there is a DEFAULT VALUE
    #-None if DEFAULT VALUE wasn't set
    def get_column_names_and_metadata(self)->list:
        try:
            #Establish connection with DB and retrieve all data
            with psycopg.connect(f"""
                host={self.host_name}
                port={self.port}
                dbname={self.database_name}
                user={self.user_name}
                password={self.user_password}
                """) as connection:
                
                cursor = connection.cursor()

                sql = f"""
                SELECT column_name, data_type, 
                CASE
                    WHEN column_default like 'nextval%' THEN 'nextval'
                    ELSE column_default
                END as column_default
                FROM information_schema.columns
                WHERE table_name = '{self.name}'
                ORDER BY ordinal_position;
                """

                cursor.execute(sql)
                columns_description=cursor.fetchall()
    
                cursor.close()
                return columns_description

        except Exception as ex:
            print('Failed to:', ex)
            return []


    #Get the list of primary key column names. Return list of primary key column names as strings.
    def get_primary_key_columns(self)->list:
        try:
            #Establish connection with DB and retrieve all data
            with psycopg.connect(f"""
                host={self.host_name}
                port={self.port}
                dbname={self.database_name}
                user={self.user_name}
                password={self.user_password}
                """) as connection:
                
                cursor = connection.cursor()

                sql = f"""
                SELECT column_name
                FROM information_schema.key_column_usage
                WHERE table_name = '{self.name}'
                and constraint_name LIKE '%pkey'
                ORDER BY ordinal_position;
                """

                cursor.execute(sql)
                rows=cursor.fetchall()
                primary_keys=[]

                for row in rows:
                    primary_keys.append(row[0])

                cursor.close()

                return primary_keys

        except Exception as ex:
            print('Failed to:', ex)
            return []


    #Returns a list of primary key values corresponding to the primary key columns.
    def get_primary_key_values(self)->list:  
        try:
            #Establish connection with DB and retrieve all data
            with psycopg.connect(f"""
                host={self.host_name}
                port={self.port}
                dbname={self.database_name}
                user={self.user_name}
                password={self.user_password}
                """) as connection:
                
                cursor = connection.cursor()
                columns=', '.join(self.primary_key_columns)

                sql = f"""
                SELECT {columns}
                FROM {self.name};
                """

                cursor.execute(sql)
                rows=cursor.fetchall()

                # Transpose rows to get primary key values
                # https://www.geeksforgeeks.org/python/python-transpose-elements-of-two-dimensional-list/
                primary_key_values=[]
                primary_key_values = [list(col) for col in zip(*rows)]

                cursor.close()
                return primary_key_values

        except Exception as ex:
                print('Failed to:', ex)
                return []


    #Print data from table in nice tabulated view.
    def print_in_tabulated_view(self):
        try:
            #Establish connection with DB and retrieve all data
            with psycopg.connect(f"""
                host={self.host_name}
                port={self.port}
                dbname={self.database_name}
                user={self.user_name}
                password={self.user_password}
                """) as connection:
                
                cursor = connection.cursor()
       
                sql = f"SELECT * FROM {self.name} ORDER by 1;"
                cursor.execute(sql)
                
                #Get column names from cursor description
                column_names =[]
                for decription in cursor.description:
                    column_names.append(decription[0])

                #Get data(all rows) from table and print it out 
                rows = cursor.fetchall()

                if not rows:
                    print(f'Table {self.name} has no data.')
                else:
                    print(f"\n== {self.name.upper()} ==")
                    #Use tabulate function to print order list in nice grid format
                    print(tabulate(rows, headers=column_names, tablefmt="grid"))

                cursor.close()
            
        except Exception as ex:
            print('Failed to:', ex)


    # Insert a new row into the table using values collected from user input
    def add_item(self):
        #Get user input for data to INSERT into table
        column_names, row = self.get_user_input(allow_blank=False)

        try:
            #Establish connection with DB and INSERT row
            with psycopg.connect(f"""
                host={self.host_name}
                port={self.port}
                dbname={self.database_name}
                user={self.user_name}
                password={self.user_password}
                """) as connection:
                
                cursor = connection.cursor()

                columns = ', '.join(column_names)
                
                #VALUES (%s, %s, %s)
                placeholders = ', '.join(['%s'] * len(column_names))
                
                sql = f"""
                INSERT INTO {self.name} ({columns})
                VALUES ({placeholders})
                RETURNING *;
                """

                cursor.execute(sql, row)
                connection.commit()

                 # Get list of inserted rows
                inserted_rows = cursor.fetchall()
                print(f"Inserted {len(inserted_rows)} row(s):")
                print(tabulate(inserted_rows, tablefmt="grid"))

                cursor.close()
            
        except Exception as ex:
            message=str(ex)
            if 'duplicate key value' in message:
                print("Row with this unique field already exists. Please check your input.")

                #https://www.geeksforgeeks.org/python/python-get-the-string-after-occurrence-of-given-substring/
                start_idx=message.find("DETAIL:")
                details = message[start_idx + len("DETAIL:"):] if start_idx != -1 else ""
                if details:
                    print(f"Details: {details}")

            else:
                print('Failed to:', ex)


    #Prompt user to input valid values for each primary key column.
    #Note: for the current db - entity id (ex. product_id)
    def get_user_primary_key_values(self):
        #Get index(primary keys) for row to UPDATE/DELETE
        conditions={}

        for key in self.primary_key_columns:
            while True:
                value=input(f"Enter {key}: ")
                value=value.strip().lower()

                if is_valid_attribute(key, value)[0]:
                    if key in self.serial_columns:
                        conditions[key]=int(value)
                    else:
                        conditions[key]=value
                    break

        return conditions
    

    #Delete row by primary key value (id) from table.
    def delete_item_by_index(self):
        #Print out table
        self.print_in_tabulated_view()

        #Get index(primary keys) for row to delete
        delete_conditions = self.get_user_primary_key_values()

        try:
            #Establish connection with DB and DELETE row
            with psycopg.connect(f"""
                host={self.host_name}
                port={self.port}
                dbname={self.database_name}
                user={self.user_name}
                password={self.user_password}
                """) as connection:
                
                cursor = connection.cursor()

                values = list(delete_conditions.values())

                condition=[]
                for item in delete_conditions.keys():
                    condition.append(f"{item} = %s")
                
                placeholder = " AND ".join(condition)

                sql = f"""
                DELETE 
                FROM {self.name}
                WHERE {placeholder}
                RETURNING *;
                """

                cursor.execute(sql, values)

                # Get list of deleted rows
                deleted_rows = cursor.fetchall()

                connection.commit()

                if deleted_rows:
                    print(f"Deleted {len(deleted_rows)} row(s):")
                    print(tabulate(deleted_rows, tablefmt="grid"))
                else:
                    print("No rows matched the condition. Nothing was deleted.")

                cursor.close()
            
        except Exception as ex:
            print('Failed to:', ex)


    #Update row by primary key value (id) from table.
    #Using user input for values to update. 
    def update_item_by_index(self):
        #Print out table
        self.print_in_tabulated_view()

        #Get index(primary keys) for row to update
        update_conditions=self.get_user_primary_key_values()

        #Get user input for data to UPDATE into table
        column_names, row = self.get_user_input(allow_blank=True)
        
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
                set_lst=[]
                for column in column_names:
                    set_lst.append(f"{column} = %s")
                
                set_clause =', '.join(set_lst)

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


    #Return row (as list) where column=value
    def get_row_by_column_value(self, column_name:str, value)->list:  
        try:
            #Establish connection with DB and retrieve all data
            with psycopg.connect(f"""
                host={self.host_name}
                port={self.port}
                dbname={self.database_name}
                user={self.user_name}
                password={self.user_password}
                """) as connection:
                
                cursor = connection.cursor()

                sql = f"""
                SELECT *
                FROM {self.name}
                WHERE {column_name}=%s;
                """

                cursor.execute(sql, (value,))
                rows=cursor.fetchall()
                result=[]

                for row in rows:
                    result.append(list(row))

                cursor.close()
                return result

        except Exception as ex:
                print('Failed to:', ex)
                return []