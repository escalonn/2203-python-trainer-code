# we have if-else conditionals

# int and input are builtin functions
data = 'asdf' + str(4)
# data = int(input('enter a number: '))
# if data == 0:
#     print('it was zero')
# elif data < 0:
#     print('negative')
#     print('this too')
# else:
#     data = 'abc'

print(data)

print(type(data))
print(type(1))
print(type(1.5))
print(type(True))
print(type([]))

# while loop
# while input('enter x: ') != 'x':
#     print('error, enter x')

r = range(0, 5000000000, 1)
print(r[3])

# for val in [True, 3, 'str']:
#     print(val or False)

# collection = [5]
# if not collection: # if the collection is/is not empty


# for loop
# in python, you always iterate over a sequence of some kind
for i in range(5, 0, -1): # or range(5), same thing here
    print(' ' + str(i))

# range is a sequence data type in python
# that is 'lazy', it doesn't precompute the whole thing like a list,
# it calculates each value as needed

# usually you don't even write loops like that... you figure out a way to
# iterate over the collections of data that you'd be using that "i" to access

sequence = [1, 3, 2, 2, 5]
sum = 0
for i in range(len(sequence)):
    sum += sequence[i]
print(sum / len(sequence)) # calculating average unpythonically

sum = 0
for item in sequence:
    sum += item
print(sum / len(sequence)) # slightly more pythonic (actually we would use a comprehension)

# comprehension syntax in python is applied here and it's pretty powerful

# if you want to iterate over a list AND have an index as well

for i, item in enumerate(sequence):
    # i & item will be: first 0,1 - 1,3 - 2,7
    if i > 0:
        print(item != sequence[i - 1])

# enumerate returns a sequence of item-index tuples

# in python, a tuple is an immutable sequence
name = 'asdf'
age = 23
ident = 'asdfaasdf'
data = (name, age, ident) # creating a tuple
# -----
n, a, _ = data
x = 5
y = 6
x, y = y, x # swap using tuple

# enumerate is a initial basic example of the pythonic way to approach looping
# "how do i get all the data i want in each iteration of the loop"
# if possible, you want to change the definition of what sequence you're
#   iterating over so it already has all the things you need
