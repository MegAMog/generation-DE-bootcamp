#Create class to work with tables
import os
import psycopg
from dotenv import load_dotenv
from paths import env_path
from tabulate import tabulate #https://pypi.org/project/tabulate/
from utils.utils import is_valid_attribute


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
    def __init__(self, name:str):
        self.name = name.strip().lower()
        self.columns_description = self.get_column_names_and_metadata()
        self.primary_keys = self.get_primary_keys()

        #Get list of SERIAL columns
        self.serial = []
        for description in self.columns_description:
            if description[2]=='nextval':
                self.serial.append((description[0]))


    #Get and return table column names as list of tuples: [(column name, data type, default value)]
    #Default value:
    #-'nextval' if column is SERIAL
    #-value if there is a DEFAULT VALUE
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


    #Get primary key
    def get_primary_keys(self)->list:
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

                table_name=self.name         
                sql = f"SELECT * FROM {table_name} ORDER by 1;"
                cursor.execute(sql)
                
                #Get column names from cursor description
                column_names =[]
                
                for decription in  self.columns_description:
                    column_names.append(decription[0])

                #Get data(all rows) from table and print it out 
                rows = cursor.fetchall()

                if not rows:
                    print(f'Table {table_name} has no data.')
                else:
                    print(f"\n== {table_name.upper()} ==")
                    #Use tabulate function to print order list in nice grid format
                    print(tabulate(rows, headers=column_names, tablefmt="grid"))

                cursor.close()
            
        except Exception as ex:
            print('Failed to:', ex)


    #Add row (created from user input) to table.
    def add_item(self):
        #Get user input for data to INSERT into table
        
        #Get column names, which is not SERIAL
        column_names =[]
        for decription in  self.columns_description:
            if decription[2]!='nextval':
                column_names.append(decription[0])
        
        row=[]
        for column in column_names:
            while True:
                value = input(f"Enter {column.replace('_', ' ')}: ")
                value = value.strip()

                if is_valid_attribute(column, value)[0]:
                    row.append(value)
                    break
                else:
                    print(is_valid_attribute(column, value)[1])

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
                #VALUES(?,?,?) VALUES (%s, %s, %s)
                placeholders = ', '.join(['%s'] * len(column_names))
                
                sql = f"""
                INSERT INTO {self.name} ({columns})
                VALUES ({placeholders})
                """

                cursor.execute(sql, row)
                connection.commit()

                cursor.close()
            
        except Exception as ex:
            print('Failed to:', ex)


    #Delete row from table
    def delete_item_by_index(self):
        #Print out table
        self.print_in_tabulated_view()

        #Get index(primary keys) for row to delete
        delete_conditions={}
        for key in self.primary_keys:
            while True:
                value=input(f"Enter {key} for the row you would like to DELETE: ")
                value=value.strip().lower()

                if key in self.serial:
                    if value.isdigit():
                        delete_conditions[key]=int(value)
                        break
                elif is_valid_attribute(key, value)[0]:
                    delete_conditions[key]=value
                    break

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



    def update_item_by_index(self):
        #Print out table
        self.print_in_tabulated_view()

        #Get index(primary keys) for row to update
        update_conditions={}
        for key in self.primary_keys:
            while True:
                value=input(f"Enter {key} for the row you would like to UPDATE: ")
                value=value.strip().lower()

                if key in self.serial:
                    if value.isdigit():
                        update_conditions[key]=int(value)
                        break
                elif is_valid_attribute(key, value)[0]:
                    update_conditions[key]=value
                    break


        #Get column names, which is not SERIAL
        column_names =[]
        for decription in  self.columns_description:
            if decription[2]!='nextval':
                column_names.append(decription[0])

        
        #Get new values for attributes to update
        update_attributes={}
        for column in column_names:
            while True:
                value = input(f"Enter {column.replace('_', ' ')}: ")
                value = value.strip()

                if not value:
                    break
                elif is_valid_attribute(column, value)[0]:
                    update_attributes[column]=value
                    break
                else:
                    print(is_valid_attribute(column, value)[1])

        
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
                for column in update_attributes.keys():
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

                cursor.execute(sql, list(update_attributes.values())+list(update_conditions.values()))
                # Get list of deleted rows
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


