# This will be our decorator function, we pass the function we want to decorate
# as a parameter called "func"
def decorator_function(func):
    def wrapper():
        # Let's add some conversation before the greeting..
        print("- Excuse me?")
        func()
        # And some of it after
        print("- I'd like to order more tea :)")

    # We will return the modified function
    return wrapper


@decorator_function
def greeting():
    print("- Hi! How can I help you?")


# Call the function and see how it modified our greeting,
# it's a full conversation now!
greeting()
