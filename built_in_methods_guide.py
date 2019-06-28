# author: Asmaa Mirkhan ~ 2019

# COMMON BUILT-IN METHODS IN PYTHON

# ----------------------------------------------

# any(structure)
# explanation: returns True if the iterabale structure contains at least one True (0 is considered False)

# with lists
# At least one True value is enough ==> True
structure1 = ['asmaa', 11, 87.41, [1, 3]]
structure2 = ['esma', 141.87, '']
structure3 = [0, False, '']
structure4 = ['asmaa', 11, 87.41, [0, False]]
structure5 = []
print('any() with lists:', any(structure1), any(structure2),
      any(structure3), any(structure4), any(structure5))

# Output: True True False True False

# with strings
# Only when it is empty ==> False
print('any() with strings:', any('bla bla'), any('0'), any(''))

# Output: True True False

# with dictionaries
# Related to the keys, at least one True key is enough ==> True
dict1 = dict({'Name': 'Asmaa', 'Surname': 'Mirkhan'})
dict2 = dict({'Name': False, 'Surname': False})
dict3 = dict({False: 'Asmaa', '0': 'Mirkhan'})
dict4 = dict({False: 'Asmaa', 0: 'Mirkhan'})
print('any() with dictionaries:', any(dict1),
      any(dict2), any(dict3), any(dict4))

# Output: True True True False

# ------------------------------------------------------------------

# any(structure)
# explanation: returns True only if all elements of the iterabale structure are True
print()
# with lists
# At least one False value is enough ==> False
# Empty list ==> True -_-
structure1 = ['asmaa', 11, 87.41, [1, 3]]
structure2 = ['esma', 141.87, '']
structure3 = ['asmaa', 11, 87.41, [0, False]]
structure4 = []
print('all() with lists:', all(structure1), all(
    structure2), all(structure3), all(structure4))

# Output: True False True True

# with strings
# Always returns True :o
print('all() with strings:', all('bla bla'), all('0'), all(''))
# Output: True True False

# with dictionaries
# Related to the keys, at least one False key is enough ==> False
dict1 = dict({'Name': 'Asmaa', 'Surname': 'Mirkhan'})
dict2 = dict({'Name': False, 'Surname': False})
dict3 = dict({False: 'Asmaa', '0': 'Mirkhan'})
print('any() with dictionaries:', all(dict1), all(dict2), all(dict3))

# Output: True True False

# ------------------------------------------------------------------

# bool(value or structure)
# explanation: returns True only if the value is True
print()

# like if(value) in another programming languages
print('bool() method:', bool(''), bool('asmaa'), bool(0), bool([]), bool([0]))

# Output: False True False False True


# ------------------------------------------------------------------

# enumerate(structure)
# enumerate(structure, start)
# explanation: adds counter to an iterable structure, used in for (foreach) loops
print()

fruits = ['banana', 'orange', 'pear']
fruits1 = enumerate(fruits)
print('enumerate() method', list(fruits1))

# Output: [(0, 'banana'), (1, 'orange'), (2, 'pear')]

fruits2 = enumerate(fruits, 5)
print('filter() method with start parameter', list(fruits2))

# Output: [(5, 'banana'), (6, 'orange'), (7, 'pear')]

# ------------------------------------------------------------------

# filter(function, structure)
# explanation: filters given iterable with a test function


def isUpper(letter):
    return letter.isupper()


name = 'Asmaa Mirkhan.'
filtered_name = filter(isUpper, name)
print('filter() method with test func', list(filtered_name))

# Output: ['A', 'M']

# how it works without test function?
# returns True values, its default test function is bool()
structure = [0, False, True, 'asmaa', '', 0, [], [15, 0]]
no_func = filter(None, structure)
print('filter() method without test func', list(no_func))

# Output: [True, 'asmaa', [15, 0]]

# ------------------------------------------------------------------

# len(structure)
# explanation: returns length of the structure

# with lists: return number of elements
print('len() method with lists: ', len([]), len([1, 2, 3]), len(range(1, 10)))

# Output: 0 3 9

# with strings: returns number of characters
print('len() method with strings: ', len(''), len('asmaa'))

# Output: 0 5

# with dictionaries: returns the number of keys
dict1 = {'Name': 'Asmaa', 'Surname': 'Mirkhan'}
print('len() method with strings: ', len(dict1), len({}))

# Output: 2 0


# ------------------------------------------------------------------

# map(function, structure1, structure2, structure3, .....)
# explanation: applies given function to structures

def plusOne(num):
    return num+1


list1 = [44, 55, 66, 77]
list1 = map(plusOne, list1)
print('map() method, one structre', list(list1))

# Output: [45, 56, 67, 78]


def addNumbers(num1, num2):
    return num1+num2


list1 = [1, 1, 1, 1]
list2 = [2, 2, 2, 2, 2]
list2 = map(addNumbers, list1, list2)
print('map() method, two structres', list(list2))

# Output: [3, 3, 3, 3]


# ------------------------------------------------------------------

# sorted(structure)
# sorted(structure, reverse=?)
# sorted(structure, reverse=?, key=?)
# explanation: sorts elements of given iterable structure

# with lists:
list1 = [15, 12, 51, -16]
print('sorted() method with lists', sorted(list1), sorted(list1, reverse=True))

# Output: [-16, 12, 15, 51] [51, 15, 12, -16]

# with strings:
str1 = 'Asmaa'
print('sorted() method with strings', sorted(str1), sorted(str1, reverse=True))

# Output: ['A', 'a', 'a', 'm', 's'] ['s', 'm', 'a', 'a', 'A']

# sortig with key
list2 = [(1, 15), (2, 24), (3, -25)]
print('sorted() method with dictionaries with key',
      sorted(list2, key=lambda x: x[1]))

# Output: [(3, -25), (1, 15), (2, 24)]

# with dictionaries: returns sorted keys only :o
dict1 = {'Surname': 'Asmaa', 'Name': 'Mirkhan'}
print('sorted() method with dictionaries',
      sorted(dict1), sorted(dict1, reverse=True))

# Output: ['Name', 'Surname'] ['Surname', 'Name']

# trick for dictionary sorting (by key)
print('sorted() method with dictionaries trick:',
      sorted((key, value) for (key, value) in dict1.items()))

# Output: [('Name', 'Mirkhan'), ('Surname', 'Asmaa')]

# ------------------------------------------------------------------

# zip(structure1, structure2, structure3, .....)
# explanation: merges structures in tuples

# zipping:
list1 = [1, 2, 3]
list2 = ['Asmaa', 'Esma', 'Asma']
zipped = list(zip(list1, list2))
print('zip() method, zipping', zipped)

# Output: [(1, 'Asmaa'), (2, 'Esma'), (3, 'Asma')]

# unzipping
a, b = zip(*zipped)
print('zip() method, unzipping', a, b)

# Output: (1, 2, 3) ('Asmaa', 'Esma', 'Asma')
