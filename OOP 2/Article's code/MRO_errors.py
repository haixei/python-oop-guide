class First:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Second:
    def __init__(self, c):
        self.c = c


class Third(First, Second):
    pass



test_obj = Third(1, 2, 3)
# The third parameter will get highlighted by the IDE


F = type('Tulips', (), {'getFlower': 'tulip'})
E = type('Poppys', (F,), {'getFlower': 'poppy'})
G = type('Garden', (F, E), {})

# This will return:
# TypeError: Cannot create a consistent method resolution order (MRO) for bases Tulips, Poppys
