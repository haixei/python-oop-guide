# Example: creating and using a static member
class X:
    # This is our static attribute! It is the same for
    # each instance of the class but we can overwrite it,
    # let's see how that works!
    static_atrr = "Hello!"

    def return_static(self):
        return self.static_atrr


test_obj1 = X()
test_obj2 = X()


# Both cats make the same sound
print(test_obj1.return_static(), test_obj2.return_static())

# Let's change the static variable
test_obj1.sound = "HELLO!!"

# It changes for both of them
print(test_obj1.return_static(), test_obj2.return_static())

# Salem is sad because he didn't get enough snacks..
# let's change his sound to reflect that, in this case
# it will change only for him!
test_obj1.sound = "Goodbye.."
print(test_obj1.return_static(), test_obj2.return_static())
