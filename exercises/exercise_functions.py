#Write a function called display_message() that prints one sentence telling 
# everyone what you are learning about in this module. 
# Call the function, and make sure the message displays correctly

def display_message(module):
    print(f"I am learning {module}.")

module="Functions"
display_message(module)

# Write a function called favorite_book() that accepts one parameter, title. 
# The function should print a message, such as, “One of my favorite books is 
# Alice in Wonderland.” Call the function, making sure to include a book title 
# as an argument in the function call.

def favorite_book(title):
    print(f"\nOne of my favorite books is '{title.title()}'.")

book="Room on the broom"
favorite_book(book)


# Write a function called make_shirt() that accepts a size and the text of a message 
# that should be printed on the shirt. The function should print a sentence summarizing 
# the size of the shirt and the message printed on it. Call the function once using 
# positional arguments to make a shirt. Call the function a second time using keyword 
# arguments.
# Stretch and Challenge: Modify the make_shirt() function so that shirts are large by 
# default with a message that reads, “I love Python.” Make a large shirt and a medium 
# shirt with the default message, and a shirt of any size with a different message. 
def make_shirt(size="L", message="I love Python."):
    print(f"\nYour shirt\n-size is {size},\n-message printed on it is '{message}'.")


#positional arguments
make_shirt(10, "Good luck!")
make_shirt(message="Python", size="M")

make_shirt()
make_shirt(size="M")


# Write a function called describe_city() that accepts the name of a city and its country. 
# The function should print a simple sentence, such as, “Reykjavik is in Iceland.” Give 
# the parameter for the country a default value. Call your function for three different 
# cities, at least one of which is not in the default country.
def describe_city(city_name, country="UK"):
    print(f"{city_name} is in {country}.")

describe_city("London")
describe_city("Kyiv", "Ukraine")


# Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a 
# dictionary containing these two pieces of information. Use the function to make three 
# dictionaries representing different albums. Print each return value to show that the 
# dictionaries are storing the album information correctly. Add an optional parameter to 
# make_album() that allows you to store the number of tracks on an album. If the calling 
# line includes a value for the number of tracks, add that value to the album’s dictionary. 
# Make at least one new function call that includes the number of tracks on an album.

def make_album(artist_name, album_title):
    album ={'artist_name': artist_name, 'albun_title':album_title}
    return album

album1=make_album("OE", "Kvitka")
album2=make_album("Frozen", "Let it go")

print(album1)
print(album2)
album_library=[]

while True:
    print("Lets create album library.")
    artist=input("Enter an artist name : ")
    album=input("Entet an album name : ")
    album_library.append(make_album(artist, album))

    choice=input("Would you like to add one more? [y/n] : ")
    if choice.lower()!='y':
        break

print(album_library)



# Make a list of magician’s names. Pass the list to a function called show_magicians(), 
# which prints the name of each magician in the list. 
# - Write a function called make_great() that modifies the list of magicians by adding 
# the phrase, “the Great” to each magician’s name. 
# - Call show_magicians() to see that the list has actually been modified. 
# - Call the function make_great() with a copy of the list of magicians’ names. 
# Because the original list will be unchanged, return the new list and store it in a 
# separate list. Call show_magicians() with each list to show that you have one list 
# of the original names and one list with the Great added to each magician’s name

magicians=["Oz", "Merlin"]

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

#change values in place
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i]+=" the Great"

#copy() - will create new list
new_magician=magicians.copy()
show_magicians(new_magician)

make_great(new_magician)
show_magicians(new_magician)
show_magicians(magicians)


# Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function 
# call provides, and it should print a summary of the sandwich that is being ordered. 
# Call the function three times, using a different number of arguments each time.

def sandwich(*ingredients):
    print(f"You ordered sandwich with {len(ingredients)} ingredients, including:")
    for ingredient in ingredients:
        print(f"-{ingredient}")

sandwich('tomato', 'chicken', 'cheese')