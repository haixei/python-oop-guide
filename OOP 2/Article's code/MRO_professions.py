class Profession:
    def __init__(self, name):
        print(name, 'is a professional.')


class Manager(Profession):
    def __init__(self, name):
        print(name, 'can manage people.')
        super().__init__(name)


class Developer(Profession):
    def __init__(self, name):
        print(name, 'has a technical background.')
        super().__init__(name)


class TechnicalManager(Developer, Manager):
    def __init__(self, name):
        print(name, 'is a technical manager.')
        super().__init__(name)


kate = TechnicalManager('Kate')
print(TechnicalManager.__mro__)
