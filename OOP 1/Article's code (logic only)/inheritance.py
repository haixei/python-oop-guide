# Create an inheritance scenario
class X:
    # Initialize the parent class
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # We add a simple method
    def math_on_attributes(self, multiply):
        return (self.a + self.b) * multiply


# Child class Y inherits from a parent class X
class Y(X):
    # Our child class wants to have an attribute "k" and set a default
    # value for "c"
    def __init__(self, a, b, k=25, c="Default value from the child class Y"):
        # "super" refers to the parent class, we simply call its __init__ method!
        super().__init__(a, b, c)
        # The parent class doesn't have attribute "k" so we initialize it here
        self.k = k

    # We can also set defaults on the method, in this case our sum will always be
    # multiplied by 6
    def math_on_attributes(self, multiply=6):
        return (self.a + self.b) * multiply


# Create new object with parameters a, b and c and k will be set to defaults
test_obj_YX = Y(1, 2)
print('You can add a default value to the attribute: ', test_obj_YX.b)
print('Or in the method: ', test_obj_YX.math_on_attributes())

# We define attributes like they are initialised (in our case: a, b, k, c)
# What happens if we want to skip k, that has a default value we don't want to change,
# and access c to change theirs? This is the way:

test_obj2_YX = Y(1, 2, c="We can overwrite the default")
print(test_obj2_YX.c)
