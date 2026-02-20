class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

my_car = Car("Toyota", "Corolla")
my_car.display_info()