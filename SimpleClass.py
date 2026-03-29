class Car:
    wheels = 4

    # Constructor
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car: {self.make} {self.model} with {self.wheels} wheels")
# Example usage
if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla")
    my_car.display_info()
