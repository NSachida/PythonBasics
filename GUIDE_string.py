# author: Asmaa Mirkhan ~ 2019

# STRINGS

# -----------------------------------

# string declaration
sample_string = 'asmaa'
hello_string = "hello world"
multi_line = """Hello,
my name is asmaa"""
print(sample_string, hello_string)
print(multi_line)

# Output: asmaa hello world
# Hello,
# my name is asmaa

# -----------------------------------

# access chars (indexing) and slicing
print('Accessing and slicing: ',
      hello_string[0], hello_string[1:3], hello_string[:5], hello_string[-1])

# Output: h el hello d
# Note: string are immutable
# hello_string[1] = 'f' # ERROR

# -----------------------------------

# Arithmetic operators on strings
my_string = hello_string + ' ' + sample_string
print('+ op: ', my_string)

my_string = hello_string * 3
print('* op: ', my_string)

my_string = 'hello''world'
print(my_string)

# Output:
# hello world asmaa
# hello worldhello worldhello world
# helloworld

# -----------------------------------

# iterating enumarate(sttring)
for i, letter in enumerate(my_string):
    print(i, letter)

# Output: prints all chars in the string with indeces

# -----------------------------------

# membership test
print('Membership: ', 'h' in my_string, 'm' in my_string)

# Output: True Flase

# -----------------------------------

# string formatting

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
age, name, floatnum = 5, 'asmaa', 1.12345
mystr = 'My name is %s and I am %d years old, %.2f' % (name, age, floatnum)
print(mystr)
# Output: My name is asmaa and I am 5 years old, 1.12

mystr1 = 'My name is {} and I am {} years old, {:.3f}'.format(name, age, floatnum)
print(mystr1)
# Output: My name is asmaa and I am 5 years old, 1.123

mystr2 = 'My name is ' + name + ' and I am ' + str(age) + ' years old, ' + str(floatnum)
print(mystr2)
# Output: My name is asmaa and I am 5 years old, 1.12345

# -----------------------------------

# char operations:
print('Upper, lower:', my_string.upper(), my_string.lower())

# Output:
# NAME: ASMAA, SURNAME: MIRKHAN name: asmaa, surname: mirkhan

# swapcase(string) case swapping :P
string = 'AsmAA MirKhaN'
print('Case swapping:', string.swapcase())

# Output: aSMaa mIRkHAn

# .title(): returns camel case string with spaces
s = 'introduction to python'
print('Title:', s.title())

# Output: Introduction To Python

# -----------------------------------

# find(string) returns index of first matching substring
print('Find find():', my_string.find('me'))

# rfind(string) returns index of last matching substring
print('Find rfind():', my_string.rfind('me'))

# Output:
# 2
# 18

# -----------------------------------

# splitting:
splitted = my_string.split()
print('Splitting:', splitted)

# joining
joined = ''.join(splitted)
print('Joining', joined)

# Output:
# ['name:', 'asmaa,', 'surname:', 'mirkhan']
# name:asmaa,surname:mirkhan

# another example
# declare a string
original = 'My name is Asmaa'

# convert string into list and splitting criteria is ' ' (space)
split = original.split(' ')
print('Splitting:', split)

# rejoin string (convert list into string again) and 
# separate words by ',' ==> this parameter can be any string 
join = ','.join(split)
print('Joining:', join)

# Output:
# ['My', 'name', 'is', 'Asmaa']
# My,name,is,Asmaa

# -----------------------------------

# replacing:
my_string = my_string.replace('asmaa', 'esma')
print('Replacing:', my_string)

# Output: name: esma, surname: mirkhan

# -----------------------------------

# filling and centering

my_string = my_string.center(40, '*')
print('Filling: ', my_string)

# Output: ******name: esma, surname: mirkhan******

# -----------------------------------

# insensitive copmaring
print('Casefold:', 'asmaa'.casefold() == 'ASmaa'.casefold())

# Output: True

# -----------------------------------

# start control
print('Start control:', 'asmaa'.startswith('aa'), 'asmaa'.startswith('asm'))

# Output: False True

# start control with parameter (membership test again :/)
# index parameters are a range [start, end)
print('Start control with parameter:', 'asmaa'.startswith('sm', 1, 3))

# Output: True

# end control
print('End control:', 'asmaa'.endswith('aa'))

# Output: True

# -----------------------------------

# char type control
print('Char control: ', 'aa11ss22'.isalnum(), '--sssaaa2222'.isalnum())
print('Char control:', '10.15'.isdecimal(),
      '15'.isdecimal(), 'aa15'.isdecimal())

# Output:
# True False
# False True False
