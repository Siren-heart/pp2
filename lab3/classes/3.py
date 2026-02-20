class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def human_years(self):
        return self.age * 7

my_dog = Dog("Rex", 3)
my_dog.bark()
print(f"{my_dog.name} is {my_dog.human_years()} in human years.")