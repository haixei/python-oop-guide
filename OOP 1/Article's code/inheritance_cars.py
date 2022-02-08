# Define the class
class Car:
    def __init__(self, color, owner, model, brand, maxspeed):
        self.color = color
        self.brand = brand
        self.model = model
        self.owner = owner
        self.maxspeed = maxspeed
        self.locked = True

    def beep(self):
        return "Beep boop! *loudly*"

    def greet(self, custom_message):
        # Below you can see one of the ways to include a variable in a string,
        # it's useful when you need to add it somewhere in-between
        return f'{custom_message} {self.owner}!'


# Create an instance of the class, now our new object and its properties can be easily accessed
car1 = Car("silver", "Alice", "Mercedes-Benz", "EQS", 250)

# Let's use the method of the object to receive a greeting
print(car1.greet("Howdy"))


# Define a new class called "Tesla" and give it the parent class "Car"
class Tesla(Car):
    # Give the class default values
    def __init__(self, color, owner, model, brand="Tesla", maxspeed=220):
        super().__init__(color, owner, model, brand, maxspeed)

    # Custom Tesla message
    def greet(self, custom_message="Tesla welcomes you"):
        return f'{custom_message} {self.owner}!'


# Let's create a new instance and check if the brand got set to the default value
car2 = Tesla("red", "Ola", "Model X")
print(car2.brand)
print(car2.greet())

# Next up, we can still change the default value of the instance to something else
# Note: when you create a new object you want the order of the values to match the orders of the parameters.
# You might wonder, what happens if I want to skip the 3rd parameter and change the 4th? It is as simple as that:
car3 = Tesla("blue", "Alice", "Model S", maxspeed=250)

# We skipped the brand that was set to default to Tesla and changed the model. All the values can be changed from
# default at the moment. Let's use the greet method again with a custom greeting and see if the model changed.
print(car3.greet("Hi there"))
print(car3.maxspeed)
