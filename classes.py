class Person:
    def __init__(self, name):
        self.name = name
        self._id = name.lower() # underscore prefix = "private" but only by convention

    # when methods are defined in a class, it adds them as attributes to any instance of that class.
    # when a method is called on an object, it automatically adds
    #       the object itself as the first argument to that method. conventionally named "self"
    def display(self):
        # f-strings
        return f'{self.name} ({self.job})'

    def same_name(self, other):
        return self.name == other.name

class SomethingElse:
    pass

# there are several other special method names like __init__, that we will talk about later

# in python, if i say x.y, y is an "attribute" of x (incl "fields", and methods, anything)
# in python, by default for custom classes, you can add new attributes to any object
#   you want

# this condition is true if this module is being directly executed
# this condition is false if this module is being imported by another
if __name__ == '__main__':
    # if you don't define an __init__ method (constructor), a default empty constructor will be called.
    # nick = Person()
    nick = Person('Nick')
    nick2 = Person('Nick')

    nick.same_name(nick2)

    # classes do not need to specify what attributes are allowed on the object
    # we can just add them (every object has a special dict inside it that holds those attributes)
    # nick.name = 'Nick'
    nick.job = 'Trainer'

    print(nick)
    print(nick.name)
    print(nick.job)

    print(nick.display())
    print(Person.display(nick)) # equiv to above, but we wouldn't normally write it like that


#example

# module1 is its own application
# module2 is a different application that wants to use some function that module1 already made

# "library" module meant to be imported, "application" module meant to be executed
# IF you want one module to be able to do BOTH - you then need "if __name__ == '__main__':"
