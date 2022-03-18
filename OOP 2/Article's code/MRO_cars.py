class SmartVehicle:
    music_providers = ['Spotify']

    def ride_to(self, destination):
        return 'Autopilot: on\nMoving towards: ' + destination


class Car:
    music_providers = ['Radio']

    def ride_to(self, destination):
        return 'Car is starting, GPS on for: ' + destination


class SmartCar(SmartVehicle, Car):
    def __init__(self):
        SmartVehicle.__init__(self)
        Car.__init__(self)
        self.music_providers = SmartVehicle.music_providers + Car.music_providers


a = SmartCar()
print(a.ride_to('New York'))
print(a.music_providers)
