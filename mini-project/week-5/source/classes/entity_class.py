from utils.utils import get_limited_digit_input, get_list_of_unique_keys, is_valid_attribute
from tabulate import tabulate #https://pypi.org/project/tabulate/

class BaseEnity():
    def __init__(self, entity_name:str, original_list:list[dict], primary_key:str):
            self.label = entity_name

            #Original list attributes
            self.original_list=original_list
            self.primary_key=primary_key

            #Get unique keys across all dictionaries in original list. 
            self.unique_keys=get_list_of_unique_keys(self.original_list)


    #Print formatted original list of dict (in table view). 
    def print_in_tabulated_view(self):
        print(f"\n== {self.label.capitalize()} list: ==") 

        #Disaplat message if original list is empty or None.
        if not self.original_list:
            print(f"No {self.label} to display.")
            return   
        
        #Create new list with dict, includes index and all unique keys.
        rows=[]
        for idx, item in enumerate(self.original_list):
            new_row = {'index': idx}
            for key in self.unique_keys.keys():
                new_row[key] = item.get(key, "")
            rows.append(new_row)

        #Use tabulate function to print order list in nice format
        print(tabulate(rows, headers="keys", tablefmt="grid"))


    #Add item to original list.
    def add_item(self):
        #Create dict with all unique keys
        new_item=dict.fromkeys(self.unique_keys)

        #Get user input for unique keys
        for key in new_item:
            while True:
                value = input(f"Enter {key.replace('_', ' ')}: ")
                value = value.strip()

                if key==self.primary_key and value=='':
                    print(f"Primary key -{key}- shouldn't be empty.") 
                elif is_valid_attribute(key, value)[0]:
                    new_item[key]=value
                    break
                else:
                    print(is_valid_attribute(key, value)[1])
        
        #Check that primary key value doesn't exist in original list values and only then add new item
        primary_key_values=[]
        if self.primary_key!='':
            for item in self.original_list:
                primary_key_values.append(item.get(self.primary_key))


        if new_item.get(self.primary_key) in primary_key_values and primary_key_values!=[]:
            print(f"Item \n{new_item}\n wasn't added to the {self.label} list. Primary key '{new_item.get(self.primary_key)}' is already in the list.")
        else:
            self.original_list.append(new_item)
            print(f"'Item \n{new_item}'\n was successfully added to the {self.label} list.")


    #Update item by index.
    #Option: 
    # -allow_blank=True - allows blank input, and corresponding key:value will be skipped; 
    # -allow_blank=False - requires valid (non-blank) input for each key       
    def update_item_by_index(self, allow_blank=True):
        #Print original list
        self.print_in_tabulated_view()

        #Get valid index for item to update
        msg="Enter an index of the "+self.label+" you would like to UPDATE: "
        index = get_limited_digit_input(limit=len(self.original_list), input_message=msg)

        #Get new values for attributes to update
        updated_attributes={}
        for key in self.unique_keys:
            while True:
                new_value=input(f"Enter value for {key.replace('_', ' ')}: ")
                new_value=new_value.strip()

                if allow_blank and new_value == "":
                    break   
                elif is_valid_attribute(key, new_value)[0]:
                    updated_attributes[key]=new_value
                    break
                else:
                    print(is_valid_attribute(key, new_value)[1])
        
        #Check that primary key value doesn't exist in original list values and only then update new item
        primary_key_values=[]
        if self.primary_key!='':
            for item in self.original_list:
                primary_key_values.append(item.get(self.primary_key))

        if updated_attributes.get(self.primary_key) in primary_key_values and primary_key_values!=[]:
            print(f"Item with index [{index}] wasn't updated in the {self.label} list. Primary key '{updated_attributes.get(self.primary_key)}' is already in the list.")
        else:
            self.original_list[index].update(updated_attributes)
            print(f"Item with index [{index}] was successfully updated to  \n{self.original_list[index]}")


    #Delete item from original list by index
    def delete_item_by_index(self):
        #Print out original list
        self.print_in_tabulated_view()

        #Get valid index for item to delete
        msg="Enter an index of the "+self.label+" you would like to DELETE: "
        index = get_limited_digit_input(limit=len(self.original_list), input_message=msg)
        
        #Get item value to show in prompt and verify that user wants to delete this item
        item = self.original_list[index]
        confirmation=input(f"Are you sure you want to delete \n{item}\n from {self.label} list? [y/n]:")

        #Remove item if user confirmed deletion
        if confirmation.lower()=='y':
            del self.original_list[index]
            print(f"{self.label.title()} with index [{index}] - '{item}' - was successfully removed from {self.label} list.")
        else:
            print("Deletion has been canceled.")


    def get_list_of_primary_keys(self):
        primary_keys=[]
        for item in self.original_list:
            value=item[self.primary_key]
            primary_keys.append(value)
        
        return primary_keys



class Orders(BaseEnity):
    def __init__(self, entity_name, original_list, primary_key, products:BaseEnity, couriers:BaseEnity):
        super().__init__(entity_name, original_list, primary_key)
        self.products=products
        self.couriers=couriers

        self.status_list=['new', 'confirmed', 'preparing', 'ready for delivery', 'out for delivery', 'delivered', 'cancelled', 'delivery failed', 'refunded']
        self.default_status_id=2
        self.default_status=self.status_list[self.default_status_id]
        

    def add_item(self):
        #Create dict with all unique keys
        new_item=dict.fromkeys(self.unique_keys)

        #Get user input for unique keys
        for key in new_item:
            while True:
                msg=f"Enter {key.replace('_', ' ')}: "

                if key=='order_status':
                    new_item[key]=self.default_status
                    break
                
                elif key=='courier_id':
                    self.couriers.print_in_tabulated_view()
                    print("\n")

                    while True:
                        value=input(f"Enter value for {key}: ")
                        if value.isdigit():
                            break
                    
                    new_item[key]=int(value)
                    break

                elif key=='products_ids':
                    self.products.print_in_tabulated_view()
                    values=''

                    while True:
                        while True:
                            value=input(f"Enter value for {key}:")
                            if value.isdigit():
                                break

                        values+=str(value)
                        choice=input("Would you like to add more products to your basket [y/n]:").lower()
                        if choice=='y':
                            values+=','
                        else:
                            break
                    print("\n")

                    new_item[key]=values
                    break
                
                else:
                    value = input(msg)
                    value = value.strip()

                    if is_valid_attribute(key, value)[0]:
                        new_item[key]=value
                        break
                    else:
                        print(is_valid_attribute(key, value)[1])


        self.original_list.append(new_item)
        print(f"'Item \n{new_item}'\n was successfully added to the {self.label} list.")        


    def update_order_status(self):
        self.print_in_tabulated_view()

        order_idx=get_limited_digit_input(len(self.original_list), "Enter an index for order you would like to UPDATE: ")
        old_status=self.original_list[order_idx].get("order_status")

        print (f"\nAvaliable order statuses: ")
        for idx, status in  enumerate(self.status_list):
            print(f"{idx}. {status}")        
        status_idx=get_limited_digit_input(len(self.status_list), "Enter an index for status you choose: ")

        self.original_list[order_idx]["order_status"]=self.status_list[status_idx]
        print(f"Order #[{order_idx}] successfully changed status from '{old_status}' to '{self.status_list[status_idx]}'.")
