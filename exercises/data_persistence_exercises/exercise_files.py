
people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

# with open("people.txt", "w") as file:
#     for person in people:
#         file.write(person + "\n")

file = None
try:
    file = open("people.txt", 'w')

    for person in people:
        file.write(person + "\n")

except FileNotFoundError as e:
    print(f'Could not open file: {e}')

finally:
    if file:
        file.close()
        print("File was pupulated with people names.")


with open("people_rep.txt", "w") as file:
    for person in people*3:
        file.write(person + "\n")
