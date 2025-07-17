import traceback
foods = ['latte', 'flat white', 'tea', 'wine']

try:
    for food in foods:
        print(food)
    
    print(1/0)
except ZeroDivisionError as  e:
    print('Couldnt get scores:', e)
    traceback.print_exception(e)
except TypeError as e:
    print("could not get food: ", e)