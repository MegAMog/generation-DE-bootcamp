#Additional useful functions for user interface (CLI)
import os
import csv

# Clear screen function.
def clear_screen():
    #This solution will not clear screen properly, it will leave opportunity to scroll back.
    os.system('cls' if os.name == 'nt' else 'clear')
    # This solution will clean screen properly, but it looks strange.
    #print("\033c\033[3J")


# Validate input and keep asking until gets digits only value <limit.
def get_limited_digit_input(limit:int, input_message:str):
    while True:
        user_input = input(input_message)
        if user_input.isdigit():
            if int(user_input)>=0 and int(user_input)<limit:
                index = int(user_input)
                break
            else:
                print('Invalid index: index is out of possible range.')
        else:
            print('Invalid index: value should contain only digits.')
    return index


#Validate phone number (without country code)
def is_valid_phone_number (phone_number):
    if not phone_number.isdigit():
        return False, "Phone number must contain only digits."
    elif len(phone_number) != 11:
        return False, "Phone number must be exactly 11 digits long."
    else:
        return True, ""


#Validate first and last name
def is_valid_name (name):
    if name.isalpha() and len(name)>1:
        return True, ""
    else:
        return False, "Name must contain only alphabetic characters and be at least 2 characters long."
    

#Validate address
def is_valid_address(address:str)->bool:
    if len(address)>1:
        return True, ""
    else:
        return False, "Address must be at least 2 characters long."


#Validate price - should be float and >=0
def is_valid_price(price)->bool:
    try:
        value = float(price)
        if value<0:
            return False, "Price cannot be negative."
        else:
            return True, ""
    except ValueError:
        return False, "Price must be a valid number."
    

#Validate attributes.
#Need to rewrite it
def is_valid_attribute(attribute_name:str, attribute_value):
     if attribute_name.endswith('first_name') or attribute_name.endswith('last_name'):
          return is_valid_name(attribute_value)
     elif attribute_name=='customer_address':
          return is_valid_address(attribute_value)
     elif attribute_name.endswith('phone_number'):
          return is_valid_phone_number(attribute_value)
     elif attribute_name=='price':
          return is_valid_price(attribute_value)
     else:
          return True, ""
     

#Print indexed list
def print_indexed_list(lst:list, list_title='list')->bool:
    print(f"\n== {list_title.title()}: ==")

    for idx, item in enumerate(lst):
        print(f"{idx}. {item}")


#Return list of dictionary unique keys 
def get_list_of_unique_keys(original_list:list[dict])->list:
    unique_keys = {}
        
    for item in original_list:
        for key in item.keys():
             if key not in unique_keys:
                unique_keys[key] = None   
    
    return unique_keys


#Saves items from list to the file (rewrites file, creates one if it doesn't exist.)
def save_entity_to_csv_file(file_path, entity:list[dict]):
    with open(file_path, 'w') as file:
        header=get_list_of_unique_keys(entity)

        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(entity)