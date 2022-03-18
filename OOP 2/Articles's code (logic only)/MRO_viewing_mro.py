class A:
    def __init__(self, name):
        print('object', name, 'inherits from A.')


class B(A):
    def __init__(self, name):
        print('object', name, 'inherits from B.')
        super().__init__(name)


class C(A):
    def __init__(self, name):
        print('object', name, 'inherits from C.')
        super().__init__(name)


class D(C, B):
    def __init__(self, name):
        print('object', name, 'inherits from D.')
        super().__init__(name)


a = D('a')
print(D.__mro__)
