# how do scopes / namespaces work in python

# a namespace is a context where variables live
# the way that python interprets any name of a variable/etc
#  like fred, Person, print, str, etc
# LEGB namespaces
# first, it checks the local namespace
# then, any enclosing namespaces,
# then, the global namespace,
# then, the built-in namespace (print, str)

var = 5 # global
if True:
    var2 = 5 # global

print(var2)

# functions, including nested functions, have their own namespaces
def func():
    var = 6 # enclosing (relative to func2)
    # def print():
    #     pass
    print('asdf')

    def func2():
        # nonlocal var
        # print(var)
        var = 7 # local
        # print = 5
        # id = 5
        # map
        # filter

    func2()

func()

print(var)
