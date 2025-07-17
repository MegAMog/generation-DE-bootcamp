# #FOR/WHILE loops
# #for for fixed number of times
# for x in [1, 2, 3, 4, 5]:
#     print(f'current number is {x}')

# pets=['dog', 'cat']
# for pet in pets:
#     print(pet)

# name="Anastasiia"
# for char in name:
#     print(char.lower())

# #while for condition loop
# pet_age=1
# while pet_age<=14:
#     print(f"Dog is {pet_age} old.")
#     pet_age+=1


#  #range
# for x in range(0,4):
#     print(f'current number is {x}')


# #iterate through indexes
# for idx in range(0, len(pets)):
#     pet=pets[idx]
#     print(f'pet at index {idx} is {pet}')


# #nested loops
# adjectives = ["red", "big", "tasty"]
# fruits = ['apple', 'cherry', 'peach']

# for adj in adjectives:
#     for fruit in fruits:
#         print(f'{fruit} is {adj}.'.capitalize())

# #break
# menu=['coffee', 'tea', 'wine', 'bear']
# for item in menu:
#     print(f'{item}')
#     if item=='wine':
#         break

# #continue
# for item in menu:
#     if item=='wine':
#         continue
#     print(f'{item}')


# # for - else
# for item in menu:
#     print(item)
# else: #when the list is finished do other ("finally)")
#     print("List is finished!")


# #DICTONARY
# cat = {
#     'name': 'Nyash',
#     'age': 7,
#     'is_hungry': True
# }

# print(cat)
# print(f'{cat['name']} age = {cat['age']}.')

# cat['weight']=5.5
# print(cat)

# #delete a key-value
# del cat['is_hungry']
# print(cat)

# #.get() - get if does exist
# print(cat.get('is_hungry'))

# #check that key is in dict
# if 'name' in cat:
#     print(f'name = {cat['name']}')
# else:
#     print('No name.')

# print(f'Number od keys in dictionary = [len(cat)]')

# print(cat.items(), end='\n \n \n')
# print(cat.keys())
# print(cat.values())

# cat.clear()
# print(cat)

# cats=[{
#     'name': 'Nyash',
#     'age': 7,
#     'is_hungry': True
# },
# {
#     'name': 'Kitty',
#     'age': 2,
#     'is_hungry': False
# }]

# for cat in cats:
#     print(f'{cat['name']} age = {cat['age']}.')



# #FUNCTIONS
# def add_numbers(a, b):
#     return a+b


# print(add_numbers(1, 0))


# #animal_type='cat' by default
# def describe_pet(pet_name, animal_type='cat'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type} name is {pet_name}")


# #Positional arguments
# describe_pet('Nyash', 'cat')

# #Keyword arguments
# describe_pet(animal_type='cat', pet_name='Nyash')
# describe_pet(pet_name='Nyash', animal_type='cat')


# #arbitrary arguments - stored in tuple
# def dog_dinner(amount, *meats):
#     """What goes into the dog's bowls?"""
#     print(meats) #tuple
#     for meat in meats:
#         print(f"I'm putting {amount} scoops of {meat} in each of your bowls")


# dog_dinner(2, 'chicken', 'kibble', 'gravy', 'bones')


# #arbitrary anmount - dictionary
# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# new_user = build_profile('Antony', 'Foy', Age=41, Height="6'", Location='Manchester', Subject='Cloud')
# print(new_user)

# a=10
# print(a)

# def outer_function():
#     global a
#     a=100
#     b=4
    
#     print(a)

# outer_function()
# print(a)

#
#
#This will return new list, but won't update new_list, list.
# list=["berry", "pineapple"]
# new_list = list.copy()

# def update(original_list, new_item):
#     updated_list = original_list.copy()
#     updated_list.append(new_item)
#     return updated_list

# print(update(new_list, "apple"))
# print(list)
# print(new_list)

# def my_function(a):
#     b = a - 2
#     return b

# c = 3

# if c > 2:
#     d = my_function(5)
#     print(d)


# # file_handle = open('hello.txt', 'a+')

# # text_content = file_handle.read()
# # print(f'Message - {text_content}')
# #  

# file_handle = None 
# try:
#     file_handle = open('people2.txt', 'w')
#     # print(file_handle)
#     # print(type(file_handle))

#     text_content = file_handle.readlines()
#     for line in text_content:
#         print(f'Name - {line.strip()}')

# except FileNotFoundError as e:
#     print(f"Could not find the file: {e}")
          
# except Exception as e:
#     print (f"Unexpected error: {e}")

# finally:
#     if file_handle:
#         print(file_handle)
#         file_handle.close()
#     else:
#         print('---')



# file = open('write.txt', 'w')
# file.write('----- +++ -----')
# file.write('----- --- -----')
# file.close()
