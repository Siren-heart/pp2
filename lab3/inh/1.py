class Animal:
    def eat(self):
        print("This animal is eating.")

class Cat(Animal):
    def meow(self):
        print("Meow!")

my_cat = Cat()

my_cat.meow()
my_cat.eat()