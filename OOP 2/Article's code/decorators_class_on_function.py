class Users(object):
    def __init__(self, target):
        self.target = target
        self.users = []

    def __call__(self, first, second):
        full_name = self.target(first, second)
        self.users.append(full_name)
        print('Hello ' + full_name + '!')


@Users
def add_name(first, second):
    return first + ' ' + second


add_name('Kate', 'Moss')

# Prints out:
# "Hello Kate Moss!""
