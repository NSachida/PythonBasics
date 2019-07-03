# author: Asmaa Mirkhan ~ 2019

# DICTIONARIES

# dictionary declaration
sample_dict = {1: 'asmaa', 2: 'mirkhan'}
print(sample_dict)
some_dict = dict({'name': 'asmaa', 'surname': 'mirkhan'})
print(some_dict)

# Output:
# {1: 'asmaa', 2: 'mirkhan'}
# {'name': 'asmaa', 'surname': 'mirkhan'}

# access element
print('Element access: ', some_dict['name'], some_dict.get('name'))

# Output: asmaa asmaa

# updating values
name = {'name': 'some_name'}
some_dict.update(name)
print('After updating:', some_dict)

some_dict['name'] = 'esma'
print('After updating:', some_dict)

# Output:
# {'name': 'some_name', 'surname': 'mirkhan'}
# {'name': 'esma', 'surname': 'mirkhan'}

# adding keys
some_dict['age'] = 21
some_dict['city'] = 'istanbul'
print('New keys:', some_dict)

# Output: {'name': 'esma', 'surname': 'mirkhan', 'age': 21, 'city': 'istanbul'}

# remove element
del some_dict['age']
some_dict.pop('city')
print('After deleting: ', some_dict)

# Output: {'name': 'esma', 'surname': 'mirkhan'}

# clearing
my_dict = {'name': 'Esma', 'surname': 'Mir'}
my_dict.clear()
print('Clearing:', my_dict)

# Output: {}

# copying - giving NEW reference to the new element
my_dict = sample_dict.copy()
print('Copying', my_dict, sample_dict)

# Output {1: 'asmaa', 2: 'mirkhan'} {1: 'asmaa', 2: 'mirkhan'}

my_dict.clear()
print('Copying', my_dict, sample_dict)

# Output: {} {1: 'asmaa', 2: 'mirkhan'}

# assignment - reference to the ORIGINAL value
my_dict = sample_dict
print('Assignment', my_dict, sample_dict)

# Output {1: 'asmaa', 2: 'mirkhan'} {1: 'asmaa', 2: 'mirkhan'}

my_dict.clear()
print('Assignment', my_dict, sample_dict)

# Output: {} {}

# Creating dict from sequence of keys
keys = ['city', 'phone', 'birthdate']
my_dict = dict.fromkeys(keys)
print(my_dict)

# Output: {'city': None, 'phone': None, 'birthdate': None}

# Creating dict from sequence of keys with initial values
keys = ['city', 'phone', 'birthdate']
my_dict = dict.fromkeys(keys, 'Unknown')
print(my_dict)

# {'city': 'Unknown', 'phone': 'Unknown', 'birthdate': 'Unknown'}

# getting elements as items, keys or values
items = my_dict.items()
print('Items:', items)
keys = my_dict.keys()
print('keys:', keys)
values = my_dict.values()
print('values:', values)

# Output:
# dict_items([('city', 'Unknown'), ('phone', 'Unknown'), ('birthdate', 'Unknown')])
# dict_keys(['city', 'phone', 'birthdate'])
# dict_values(['Unknown', 'Unknown', 'Unknown'])

# iterating
print(some_dict)
for item in some_dict:
    print(item, some_dict[item])

# Output: prints all keys and values
