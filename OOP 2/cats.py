class Test1:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Test2:
    def __init__(self, c):
        self.c = c


class Merged(Test1, Test2):
    def __init__(self, a, b, c):
        Test1.__init__(self, a=a, b=b)
        Test2.__init__(self, c=c)


obj1 = Merged(1, 2, 3)
print(obj1.a)


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
