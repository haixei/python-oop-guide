from datetime import datetime


# In this example I refer to the exercise from the first section of the post (OOP basics 1)
class Assistant:
    _latest_version = 12

    def __init__(self, name, version=9):
        self.name = name
        self.version = version

    # The assistant should be able to answer our call and return the time
    # if the version is appropriate, let's say the support for this function
    # started at the version 11 and it won't work for anything below that
    def return_time(self):
        if self.version < 11:
            return "Upgrade your device to use that function."
        else:
            current_time = datetime.now().strftime('%A, %H:%M %p')
            return f'Today is {current_time}'

    # Upgrade the system if the newest version is available
    def upgrade(self):
        if self.version < self._latest_version:
            self.version = self._latest_version
        else:
            return "Your system already has the latest version."


Siri = Assistant("Siri")

# Try to return the time
print(Siri.return_time())

# Let's upgrade the device
Siri.upgrade()
print(Siri.return_time())

# In the later posts we will learn how to make sure that the version is not initialized
# with a higher value than the latest version using decorators
