# author: Asmaa Mirkhan ~ 2019

# LISTS

# list declaration and appending
my_list = [0, 15, 12.5, 2, 3, 4]
my_list.append(74)  # appends one element
my_list.extend([14, 12])  # appends multiple elements
print('After appending:', my_list)

# Output: [0, 15, 12.5, 2, 3, 4, 74, 14, 12]

# inserting at sepecific position (index, value)
my_list.insert(2, 44)  # inserts the 44 value at 2nd position
print('After inserting:', my_list)

# Output: [0, 15, 44, 12.5, 2, 3, 4, 74, 14, 12]

# deleting element(s)
del my_list[0]  # deletes element(s)
print('After deleting:', my_list)

# Output: [15, 44, 12.5, 2, 3, 4, 74, 14, 12]

# statistical operations
print('length:', len(my_list), 'min:', min(my_list), 'max:', max(my_list), 'sum:',
      sum(my_list), 'count', my_list.count(2), 'index of 2:', my_list.index(2))

# Output: length: 9 min: 2 max: 74 sum: 180.5 count 1 index of 2: 3

# list slicing
print('list[1:3]', my_list[1:3])
print('list[-4:-2]', my_list[-4:-2])
print('list[:3]', my_list[:3])
print('list[4:]', my_list[4:])

# Output
# [44, 12.5]  ## start printing from 1st position to 3rd position (3rd not included) in maths [1,3)
# [4, 74] ## start printing from 4th position from the end to 2nd position from the end (3rd not included)
# [15, 44, 12.5] ## start printing from the start to the 3rd position (3rd not included)
# [3, 4, 74, 14, 12] ## start printing from the 4th position to the end


# sample list indexing
# list:                 15    11    -45    -14.6    74.45    87    96
# positive indexing     [0]   [1]   [2]     [3]      [4]    [5]    [6]
# negative indexing     [-7]  [-6]  [-5]    [-4]     [-3]   [-2]   [-1]


# list operations
print('+ operation', my_list[2:5] + my_list[3:6])
print('* operations', my_list[:3]*3)

# Output:
# [12.5, 2, 3, 2, 3, 4]
# [15, 44, 12.5, 15, 44, 12.5, 15, 44, 12.5]

# list sorting
my_list.sort()
print('Sorted list', my_list)
# Output: [2, 3, 4, 12, 12.5, 14, 15, 44, 74]


# list comperhansions
my_filtered_list = [i for i in my_list if i > 11]
print('Filtered list', my_filtered_list)

# Output: [12, 12.5, 14, 15, 44, 74]

my_complex_list = [
    i*j for i in my_list for j in my_filtered_list if i*j < 50]
print('Complex list', my_complex_list)

# Output: [24, 25.0, 28, 30, 36, 37.5, 42, 45, 48]

square_list = [i**2 for i in range(1, 6)]
print(square_list)

# Output: [1, 4, 9, 16, 25]

# reversing
square_list.reverse()
print('Reversed list', square_list)

# Output: [25, 16, 9, 4, 1]

my_list.clear()
print(my_list)

# Output: []

# in operation
print('25? ', 25 in square_list)
# Output: True

# iterating
for val in square_list:
    print(val)
# Output: all square_list's values

for i, val in enumerate(square_list):
    print(i, 'th value:', val)

# Output: all square_list's indeces and values

for i, val in enumerate(square_list, start=3):
    print(i, 'th value (started from index=3):', val)

# Output: square_list's indeces and values starting from 3rd position

# iterating in reversed order
for val in reversed(square_list):
    print('value (reversed order): ', val)

# Output: all square_list's indeces and values in reversed order

# ------------------------------------------------------------

# TUPLES

# tuple declaration
some_tuple = 1, 2, 5, 'asmaa', [-88, -55, 13]
sample_tuple = (15, 11.5, 13)
print(some_tuple)
print(sample_tuple)

# Output:
# (1, 2, 5, 'asmaa', [-88, -55, 13])
# (15, 11.5, 13)

# tuple indexing and slicing
print('indexing', some_tuple[1], some_tuple[3]
      [2], some_tuple[-1], some_tuple[1:4])

# Output: 2 m [-88, -55, 13] (2, 5, 'asmaa')

# Note: tuples are immutable
# some_tuple[0]=2 #ERROR
some_tuple[-1][2] = 1111  # OK, element is itself a mutable datatype
print('Changed tuple:', some_tuple)

# Output: (1, 2, 5, 'asmaa', [-88, -55, 1111])

# tuple operations
sample_tuple = some_tuple + (47, 48, 49)
print('+ operation', sample_tuple)
sample_tuple = (11, 22, 33)*3
print('* operation', sample_tuple)

# Output
# (1, 2, 5, 'asmaa', [-88, -55, 1111], 47, 48, 49)
# (11, 22, 33, 11, 22, 33, 11, 22, 33)

# deleting a tuple
del sample_tuple
# print(sample_tuple) ERROR

# iterating
for val in some_tuple:
    print(val)

# Output: prints all values in the tuple

for i, val in enumerate(some_tuple):
    print(i, 'th value: ', val)

# Output: prints all values and indeces in the tuple
