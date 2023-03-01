class Vehicle:

    # define a class attribute
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def fare(self):
        return self.capacity * 100


model1X = Vehicle("Model X", 240, 18)
print(model1X.color)

