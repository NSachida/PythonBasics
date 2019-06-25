# author: Asmaa Mirkhan ~ 2019

# STRINGS

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

# access chars and slicing
print('Accessing and slicing: ',hello_string[0], hello_string[1:3], hello_string[:5], hello_string[-1])

# Output: h el hello d

# Note: string are immutable
# hello_string[1] = 'f' # ERROR

# string operations:
my_string = hello_string+' '+sample_string
print('+ op: ',my_string)

my_string = hello_string*3
print('* op: ',my_string)

my_string = 'hello''world'
print(my_string)
# Output:
# hello world asmaa 
# hello worldhello worldhello world
# helloworld

# iterating
for i, letter in enumerate(my_string):
    print(i, letter)

# Output: prints all chars in the string with indeces

# membership test
print('Membership: ','h' in my_string, 'm' in my_string)
# True Flase

# string formatting
my_string = 'name: {}, surname: {}'
my_string = my_string.format('asmaa', 'mirkhan')
print('Formatting: ',my_string)

# Output: name: asmaa, surname: mirkhan

# char operations:
print('Upper, lower:',my_string.upper(), my_string.lower())
print('Find:',my_string.find('me'))

# Output 
# NAME: ASMAA, SURNAME: MIRKHAN name: asmaa, surname: mirkhan 
# 2

# splitting:
splitted = my_string.split() 
print('Splitting:',splitted)
joined= ''.join(splitted)
print('Joining', joined)

# Output: 
# ['name:', 'asmaa,', 'surname:', 'mirkhan']
# name:asmaa,surname:mirkhan

# replacing:
my_string = my_string.replace('asmaa', 'esma')
print('Replacing:',my_string)

# Output: name: esma, surname: mirkhan

# filling and centering

my_string = my_string.center(40, '*')
print('Filling: ', my_string)

# Output: ******name: esma, surname: mirkhan******

# insensitive copmaring
print('Casefold:','asmaa'.casefold()=='ASmaa'.casefold())

# Output: True

# end control
print('End control:','asmaa'.endswith('aa'))

# Output: True

# char type control
print('Char control: ','aa11ss22'.isalnum(), '--sssaaa2222'.isalnum())
print('Char control:', '10.15'.isdecimal(), '15'.isdecimal(), 'aa15'.isdecimal())

# Output: 
# True False
# False True False

# TODO: complete string methods