# Example: accessing the private variable
class X:
    def __init__(self, a):
        # We hint on the fact that the attribute is private
        # by putting a double underscore before its name
        self.__a = a

    def return_a(self):
        return self.__a

    def increase_a(self):
        self.__a += 1
        return self.__a


test_obj = X(24)

# You can access the age only trough the methods we defined in the function
print('Access age trough method: ', test_obj.return_a())
print('Increase age trough method: ', test_obj.increase_a())

# Since in Python private variables are not really private like in other OOP languages.
# The way we defined it provides something more like a hint rather than a rule!
# The thing is.. we can't access the age outside of the class, but we can easily do it within it
# like the following:
print('Increase age trough the class: ', test_obj._X__a)

# You can't access the attribute this way.. double underscore is a signal to the
# developer to not touch it
print(test_obj.__a)