# Define the class of a car, it can be less complex than in the example
# from the article
class Car:
    def __init__(self, color, brand, locked):
        self.color = color
        self.brand = brand
        self.locked = locked

    # Let's create a method that will lock and unlock the car
    def change_lock(self):
        # The "not" keyword will change the attribute to its opposite,
        # I will assume you know what a boolean is
        self.locked = not self.locked
        return f'Locked status changed to: {self.locked}'


# Let's set the initial value to True, the car comes in locked
car1 = Car('matte black', 'Aston Martin', True)
print(car1.change_lock())

# And we can close it again :)
print(car1.change_lock())
