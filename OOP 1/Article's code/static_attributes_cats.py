# Example: creating and using a static member
class Cat:
    # This is our static attribute! It is the same for
    # each instance of the class but we can overwrite it,
    # let's see how that works!
    sound = "Meow!"

    def __init__(self, color, name):
        # Instance attributes
        self.color = color
        self.name = name

    def make_sound(self):
        return self.sound


george = Cat("ginger", "George")
salem = Cat("black", "Salem")


# Both cats make the same sound
print(george.make_sound(), salem.make_sound())

# Let's change the static variable
Cat.sound = "MEOW!!"

# It changes for both of them
print(george.make_sound(), salem.make_sound())

# Salem is sad because he didn't get enough snacks..
# let's change his sound to reflect that, in this case
# it will change only for him!
salem.sound = "Meow :("
print(george.make_sound(), salem.make_sound())
