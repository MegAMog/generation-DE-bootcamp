car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year' : 1964,
    'isNew': False
}

#Add a new key-value pair to the below car dictionary for the `colour`. 
# Print out the `colour` to verify it worked.
car['colour']='blue'
print(f'Car colour is {car.get('colour')}.')
# if 'colour' in car:
#     print(f'Car colour is {car['colour']}.')
# else:
#     print("No colour attribute.")


#Update the value of the `model` in the car dictionary. 
# Print out the new value to verify it worked.
old_model=car['model']
car['model']='Focus'
print(f"Old model '{old_model}' was updated to '{car['model']}'.")


#Delete the `model` key-pair from the car dictionary. 
# Print out the entire dictionary to verify it worked.
if 'model' in car:
    del car['model']
    print(f'Model was deleted. New dictionary {car}.')
else:
    print("No model attribute.")


#Use the `items()` function to loop through the dictionary and print 
# each key-value pair like so:  key: x, value: y.
for key, value in car.items():
    print(f'key: {key}, value: {value}')


