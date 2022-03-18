# Our decorator function will change the "init" method
def decorate_init(target):
    def decorator_init(self):
        print('We got decorated! So pretty!')

    def hello(self):
        print('Say hello!')

    target.__init__ = decorator_init
    target.hello = hello
    return target


@decorate_init
class C:
    def __init__(self):
        print('I am undecorated.')


a = C()
a.hello()

