names=["Eminem", "Rihanna"]

# for name in names:
#     print(name)
for name in names:
    print(f"Thank you for your music, {name}!")


movies = ['The Godfather', 'Casablanca', 'The Matrix']
print(f"My favorite book is {movies[0]}")


#The Dinner Problem
people=["Joe", "Anna", "Tim"] #, "Liza"]

def print_invintations(people:list):
    for person in people:
        print(f"Hi, {person}! I would like yto invite you for dinner.")

print_invintations(people)

person_not_attending=input("Who can't attend dinner? >>")
person_new_attending=input("Who is going to be new one attending dinner? >>")

for i in range(0, len(people)):
    if people[i]==person_not_attending:
        people[i]=person_new_attending

print(people)
print_invintations(people)

print("New bigger table was found.")
people.insert(0, input("New guest >> "))
people.insert(len(people)//2, input("New guest >> "))
people.append(input("New guest >> "))

print_invintations(people)
