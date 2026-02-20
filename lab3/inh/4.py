class Flyer:
    def fly(self):
        print("I can fly!")

class Swimmer:
    def swim(self):
        print("I can swim!")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

donald = Duck()
donald.quack()
donald.fly()
donald.swim()