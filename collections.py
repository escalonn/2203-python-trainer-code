# collection types

# list

data = [1, 2, 3]
# lists are mutable
data[0] = 0
# they can grow and shrink
data.append(4)
data += [5, 6, 7]
del data[3]
# they support all the things other sequences do
# they can be sorted
data.sort() # method on lists, sorts the list in-place
sorted(data) # takes any iterable, returns a new list

print([3, 4] * 2)
print([3, 4] < [3, 5])

# tuples

data2 = ('abc', 3, 5)

name, quantity, price = data2
data3 = [data2, data2, data2]

for (i, item) in enumerate(data):
    pass


# for threedatas in data3:
#     print(threedatas[0], threedatas[1], threedatas[2])
for name, quantity, price in data3:
    print(name, quantity, price)


# set

# set in python is an unordered collection
# that is very fast to check for membership in
#  (because of the properties of the underlying hashtable data structure)
# sets can't have duplicates, if you try to add a duplicate, nothing happens

registered_usernames = set()
registered_usernames = {'bob', 'fred', 'nick'}

def create_new_username(input):
    if input in registered_usernames:
        # raise Exception('username already in use')
        return False
    registered_usernames.add(input)
    return True

# dicts

# dicts have a lot in common with sets
# dicts are associative maps
#  (they don't contain just one value at a time, they contain key-value pairs)

person_age_map = {} # dict, not set
person_age_map = {
    'bob': 35,
    'tom': 24
}

person_age_map['bob'] == 35
person_age_map['bob'] = 36

# it's very common to use dicts anytime your code will be
# looking up one value by another value

for key in person_age_map: # iterate over keys (or use .keys())
    print(key)
for value in person_age_map.values(): # iterate over values
    print(value)
for key, value in person_age_map.items(): # iterate over keys and values
    print(key, value)

# access value, with a KeyError if the key isn't found
person_age_map['nick']
# access value, return None if the key isn't found
person_age_map.get('nick')
person_age_map.get('nick', default=0) # or, a different default from None
# is the key in the dict at all
'nick' in person_age_map
# is the value present (not fast like seraching by key)
35 in person_age_map.values()

# comprehensions

collection = [] # any collection not just list
for x in data:
    for y in data:
        if x != 0:
            collection.append(x * y)

# list comprehension
collection2 = [x ** 2 for x in data]
collection2 = [x * y for x in data for y in data if x != 0]

# set comprehension
set_comp = {x ** 2 for x in data}

# dict comprehension
nums_to_squares = {x: x ** 2 for x in data}
squares_to_nums = {x ** 2: x for x in data}
