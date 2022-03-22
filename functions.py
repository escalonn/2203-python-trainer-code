# define functions with "def"
# functions have a name and parameter list
# but in python there is no overloading, only one function (or anything else) with a given name in a given namespace/scope

def output(seq):
    print(seq)


# this replaces the previous function
# default arguments
def output(item, some_arg=3, separator: str = ' ') -> None:
    # use try-except-finally when you expect
    # an error might occur, and you want to handle it.
    # try block contains the code that might raise the error
    try: # like try-catch in other language
        # x = 'asdf'
        # iter(item)
        # raise TypeError('message')
        print(*item, sep=separator)
    # execution will jump to the except block if a matching error is raised.
    except TypeError as e:
        print(item)
        # return # without this it would continue to the print line, which i don't want
    finally:
        # the code here always runs after try and/or except.
        # whether there was no error, a caught error, or an uncaught error.
        # mostly useful for cleaning up resources that need to always be cleaned up
        pass
    # print(x)


# def output(one_item):
#     print(one_item)

# special value "None" with type NoneType

output([1,2,3], separator='-')
output(item=[1,2,3], separator='-')
output(123)
# print(1, 2, 3)

# python will try to detect errors and prevent them from happening
# x = [1, 2, 3][3]
# len(1)

# try:
#     while True:
#         pass
# except:
#     print('error caught')

def add_all(initial, *items):
    return initial + sum(items)

print(add_all(0, 2, 2, 3))
