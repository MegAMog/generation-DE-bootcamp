class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        print(f"Created new person {self.name}.")

    def increment_age(self):
        self.age+=1


    def print(self):
        print(f"{self.name}, {self.age}")


jane=Person("Anna", 25)
print(jane.increment_age())

print(type(jane))
print(jane.age)

jane.print()
print(str)