# Define the class
class Car:
    def __init__(self, color, owner, brand, model):
        self.color = color
        self.brand = brand
        self.model = model
        self.owner = owner
        self.locked = True

    def beep(self):
        return "Beep boop! *loudly*"

    def greet(self, custom_message):
        # Below you can see one of the ways to include a variable in a string,
        # it's useful when you need to add it somewhere in-between
        return f'{custom_message} {self.owner}!'

    # Allow to lock and unlock the car
    def change_lock(self):
        self.locked = not self.locked
        return f'Locked status changed to: {self.locked}'


# Create an instance of the class, now our new object and its properties can be easily accessed
car1 = Car("silver", "Alice", "Mercedes-Benz", "EQS")

# Let's use the method of the object to open the car and receive a greeting
print(car1.change_lock())
print(car1.greet("Howdy"))


# Define a new class called "Tesla" and give it the parent class "Car"
class Tesla(Car):
    # Give the class default values
    def __init__(self, color, owner, brand="Tesla", model="Model X"):
        super().__init__(color, owner, brand, model)

    # Custom Tesla message
    def greet(self, custom_message="Tesla welcomes you"):
        return f'{custom_message} {self.owner}!'


# Let's create a new instance and check if the brand got set to the default value
car2 = Tesla("red", "Ola")
print(car2.brand)

# Next up, we can still change the default value of the instance to something else
# Note: when you create a new object you want the order of the values to match the orders of the parameters.
# You might wonder, what happens if I want to skip the 3rd parameter and change the 4th? It is as simple as that:
car3 = Tesla("blue", "Alice", model="Model S")

# We skipped the brand that was set to default to Tesla and changed the model. All the values can be changed from
# default at the moment. Let's use the greet method again with a custom greeting and see if the model changed.
print(car3.greet("Hi there"))
print(car3.model)
