# where does python look for modules that match this name?
# two of the places are: the current directory (of this file), and wherever pip modules are installed
# a third place is, of course, the standard library
import classes
# when we import: that module is executed line for line.
# when we import: everything in that module's namespace (its global scope)
#      is accessible as an attribute of that module here

# alternative way to import only some things, directly into this module's global scope
# from classes import Person, SomethingElse

nick = classes.Person('Nick')
# nick = Person('Nick')
print(nick.name)
