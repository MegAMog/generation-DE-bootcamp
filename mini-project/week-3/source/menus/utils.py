#Additional useful functions for user interface (CLI)
import os

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
    if phone_number.isdigit() and len(phone_number) == 11:
        return True
    else:
        return False


#Validate first and last name
def is_valid_name (name)->bool:
    if name.isalpha() and len(name)>1:
        return True
    else:
        return False
    

#Validate address
def is_valid_address(address:str)->bool:
    if len(address)>1:
        return True
    else:
        return False


#Print indexed list
def print_indexed_list(lst:list, list_title='list')->bool:
    print(f"\n== {list_title.title()}: ==")

    for idx, item in enumerate(lst):
        print(f"{idx}. {item}")


#Saves items from list to the file (rewrites file, creates one if it doesn't exist.)
def save_list_to_file(file_path, list:list):
    with open(file_path, 'w') as file:
        for item in list:
            file.write(item+"\n")