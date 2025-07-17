
#Part 1
print('part 1:'.upper())
#Strings
first_name='anastasiia'
print(first_name.title())

last_name='Marchenko'
print(first_name.title()+' '+last_name.upper())

print(f'Hi, my name is {first_name.title()} {last_name.title()}.')


#Integers
x=1
y=10
product_xy=x*y
print(product_xy)
print(f'The product of {x} and {y} is {product_xy}.')

#Lists
people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

person_3nd_start=people[2]
print(person_3nd_start)

person_3rd_end=people[-3]
print(person_3rd_end)

people_new=people[2:-1]
print(people_new)
print(people_new[0]==people_new[-1])

#Input
first_name=input("What is your first name? >> ")
print(f'Your name is {first_name}.')

x=int(input('x='))
y=int(input('y='))
product_xy=x*y
print(f'The product of {x} and {y} is {product_xy}.')

x=int(input('x='))
y=int(input('y='))
print(f'{x} is equal {y}? >> {x==y}')


#Part 2
print("_________________")
print("part 2:".upper())
#Input and Numbers
x=int(input('x='))
if (x%2!=0):
    print(f'{x} is odd.')
elif (x%4==0):
    print(f'{x} is multiple of 4.')
else:
    print(f'{x} is even.')

x=int(input('x='))
if (x%3==0):
    print('fizz')
elif (x%5==0):
    print('buzz')

#Temperature Conversion
print("\ncelsius-fahrenheit converter".upper())
option=input("Choose convert option: \nc-convert from fahrenheit to celsius, \nf-convert from celsius to fahrenheit\n>> ").lower()
temperature_input=float(input("Temperature >> "))

if option=='c':
    temperature_converted=(temperature_input - 32) * (5/9)
    print(f'{temperature_input:.1f}F is {temperature_converted:.1f}C')
elif option=='f':
    temperature_converted=(temperature_input * 1.8) + 32
    print(f'{temperature_input:.1f}C is {temperature_converted:.1f}F')
else:
    print("Wrong convert option. Next time try to choose c or f for it.")


#Bank Loan programm:
# > A bank will offer a customer a loan if they are old enough and have a large enough salary. Ask the user for input of both their age and their salary.
# - If the user is over 21 and has a salary of at least £21000, offer them a loan of up to £50,000.
# - If the user is over 30 and has a salary of at least £35000, offer them a loan of up to £75,000.
# - If the user is over 30 and has a salary of at least £50000, offer them a loan of up to £100,000.
# - If none of the above, do not offer them a loan.
print("\nbank offer system:".upper())
age=int(input('How old are you? >> '))
salary=int(input("How much do you earn? >> "))
if age>30 and salary>=50000:
    offer=100000
elif (age>30 and salary>=35000):
    offer=75000
elif (age>21 and salary>=21000):
    offer=50000
else:
    offer=0

if offer>0:
    print(f"We could offer you a loan up to £{offer:,}.")
else:
    print("Sorry, we could not offer you a loan.")