class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
p2 = Person("Alice", 28)

print(f"{p1.name} is {p1.age} years old.")
print(f"{p2.name} is {p2.age} years old.")