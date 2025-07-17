# Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function 
# call provides, and it should print a summary of the sandwich that is being ordered. 
# Call the function three times, using a different number of arguments each time.

def sandwich(*ingredients):
    print(f"You ordered sandwich with {len(ingredients)} ingredients, including:")
    for ingredient in ingredients:
        print(f"-{ingredient}")