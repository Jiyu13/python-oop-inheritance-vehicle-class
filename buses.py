from vehicles import Vehicle


class Bus(Vehicle):

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

    def fare(self):
        amount = super().fare()
        return amount * 100 * 1.1


school_bus = Bus("School Volvo", 180, 12)
print(school_bus.color)
school_bus.color = "yellow"
print(school_bus.color)

# Check type of an object
print(type(school_bus))
# => <class '__main__.Bus'>

# Determine if School_bus is also an instance of the Vehicle class
print(isinstance(school_bus, Vehicle))  # => True
