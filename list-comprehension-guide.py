# author: Asmaa ~ 2019

# LIST COMPREHENSION IN PYTHON

# ----------------------------------------------

# definition: An elegant way to define and create lists based on existing lists.
# General Syntax: [expression for item in list]

name = 'Asmaa'
name_letters = [l for l in name]
print('List of letters:', type(name_letters), name_letters)

# Output: <class 'list'> ['A', 's', 'm', 'a', 'a']

# Conditions in list comprehension
# Syntax: [expression for item in list if condition]
ages = [5, 6, 28, 13, 18, 12, 11, 3, 44, 38, 60, 25, 21, 70]
adults = [age for age in ages if age >= 18]
print('Adults:', adults)

# Output: [28, 18, 44, 38, 30, 25, 21]

# Nested if with list comprehension
# Syntax: [expression for item in list if condition if conditions]
youth = [age for age in ages if age >= 18 if age <= 40]
print('Youth:', youth)

# OR
# Syntax: [expression for item in list if condition and conditions]
youth = [age for age in ages if age >= 18 and age <= 40]
print('Youth:', youth)

# if-else with list comprehension
# Syntax: [expression if condition else expression for item in list]
classes = ['adult' if age >= 18 else 'Child' for age in ages]
print('Classes:', classes)

# Output: ['Child', 'Child', 'adult', 'Child', 'adult', 'Child', 'Child',
# 'Child', 'adult', 'adult', 'adult', 'adult', 'adult', 'adult']

# Nested for loops
# General Syntax: [expression outer loop inner loop]
# Detailed Syntax: [expression for expression2 in list for expression in expression2]

# unpack the matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
unpacked = [item for row in matrix for item in row]
print('Unpacked Matrix:', unpacked)

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ----------------------------------------------------------------------

# example - 0:
num = [1, 2, 3, 4, 5]
square = [num**2 for num in num]
print('Squares:', square)

# Output: [1, 4, 9, 16, 25]


# example - 1:
height = [10, 20, 30, 40]
width = [1, 2, 3, 4]
area = [h*w for h, w in zip(height, width)]
print('Areas:', area)

# Output: [10, 40, 90, 160]


# example - 2:
# get all possible combinations
str1 = 'abc'
str2 = 'xyz'

comb = [j + k for j in str1 for k in str2]
print('Combinations:', comb)

# Output: ['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']