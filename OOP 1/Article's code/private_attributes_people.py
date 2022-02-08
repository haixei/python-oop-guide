# Example: accessing the private variable
class Person:
    def __init__(self, age):
        # We hint on the fact that the attribute is private
        # by putting a double underscore before its name
        self.__age = age

    def return_age(self):
        return self.__age

    def increase_age(self):
        self.__age += 1
        return self.__age


Alice = Person(24)

# You can access the age only trough the methods we defined in the function
print('Access age trough method: ', Alice.return_age())
print('Increase age trough method: ', Alice.increase_age())

# Since in Python private variables are not really private like in other OOP languages.
# The way we defined it provides something more like a hint rather than a rule!
# The thing is.. we can't access the age outside of the class, but we can easily do it within it
# like the following:
print('Increase age trough the class: ', Alice._Person__age)

# You can't access the attribute this way.. double underscore is a signal to the
# developer to not touch it
print(Alice.__age)