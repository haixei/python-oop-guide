# Hurray! This is going to be your first class you create!
# We want to have a few nice birds, maybe in different colors? Let's see
# what can be done..

class Bird:
    def __init__(self, color, name, kind, sound):
        self.color = color
        self.name = name
        self.kind = kind
        self.sound = sound

    def introduction(self):
        # Birds, like any everyone, want to introduce themselves, you can
        # make this method in any way you wish
        return f'Hello, my name is {self.name} and I am a {self.color} {self.kind}'

    def sing(self):
        # And they, of course, sing. Very loudly. At 5am :)
        return self.sound


# This section made me listen to bird sounds and I am not getting paid for it
bird1 = Bird('rainbow', 'Beatrice', 'Peacock', 'Honk honk honk!')
bird2 = Bird('pink', 'Valentina', 'Flamingo', 'Graah Graah Graah!')
bird3 = Bird('white and yellow', 'Tutu', 'Cockatoo', 'AAAAAAAAAAAAAAAAAAAH!!!!')

# Let's test our objects, we can print the values from the attributes or, if a method
# returns a value, we can print that out as well
print(bird1.color)
print(bird2.introduction())
print(bird3.sing())
