#Print the numbers 0 to 10 using a for loop.
for number in range (10):
    print(f'Current number is {number}.')

#Print the numbers 0 to 10 using a while loop.
number=0
while number<10:
    print(f'Current number is {number}.')
    number+=1

#Print the list of numbers below using a for loop.
numbers_list = [0, 2, 8, 20, 43, 82, 195, 204, 367]
for number in numbers_list:
    print(f'Number= {number}')
else:
    print('Done!')

# Take the below two lists and use a nested for loop to determine if any 
# elements from the first list are in the second. If it finds a match, 
# print out the name of the element.
list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]

for x in list1:
    for y in list2:
        if x.lower()==y.lower():
            print(f'{x} from first list is in the second.')


#6. Using a while loop, on every iteration generate a random number. If 
# it's a multiple of 5, **break** from the loop. If it's a multiple of 3,
# end the current iteration with **continue** and print a message to show 
# you are skipping. If it's neither, print the number and continue the loop.
import random

while True:
    number=random.randint(1,100)
    if number%5==0:
        print(f"{number} is multiple of 5. Breaking the loop.")
        break
    elif number%3==0:
        print (f"{number} is multiple of 3, so ending current iteration.")
        continue
    else:
        print(f"Generated number = {number}.")

