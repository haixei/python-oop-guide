class A:
    numbers = [1, 2]

    def hello(self, name):
        return 'Hello ' + name + '!'


class B:
    numbers = [3, 4]

    def hello(self, name):
        return 'Hello there ' + name + '!'


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.numbers = A.numbers + B.numbers


c = C()
print(c.hello('Alice'))
print(c.numbers)
