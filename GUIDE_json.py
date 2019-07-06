# author: Asmaa Mirkhan ~ 2019

# JSON

# -----------------------------------

# import the library
import json

# declare json object as a string
str_json = '{"name":"Asmaa", "surname": "mirkhan"}'


# This gives parsing error -_-
# str_json = "{'name':'Asmaa', 'surname': 'mirkhan'}"

# parse the string ==> loads(string)
json_obj = json.loads(str_json)
print('STR ==> JSON', json_obj)

# Output: {'name': 'Asmaa', 'surname': 'mirkhan'}

# --------------------------------------------------

# Converting from Python structures to JSON

# dictionary ==> JSON

# declare a dictionary
my_dict = dict({'product': 'HTC 820', 'price': '200$'})

# convert by dumps()
json_obj = json.dumps(my_dict)
print('DICT ==> JSON', json_obj)

# Output: {"product": "HTC 820", "price": "200$"}

# --------------------------------------------------

# list, tuple, any iterable, ... ==> JSON

# declare a list
my_list = ['HTC', 'Xiaomi', 'Huawei']
my_tuple = ('HTC', 'Xiaomi', 'Huawei')

# convert by dumps()
json_obj = json.dumps(my_list)
print('LIST ==> JSON', json_obj, type(json_obj))

# Output: ["HTC", "Xiaomi", "Huawei"] <class 'str'>

json_obj = json.dumps(my_tuple)
print('TUPLE ==> JSON', json_obj, type(json_obj))

# Output: ["HTC", "Xiaomi", "Huawei"] <class 'str'>

# --------------------------------------------------

# read JSON files

# open JSON file and load data
with open('./files/json_file.json') as json_file:
    jsons = json.load(json_file)

# print data
print(jsons)

# --------------------------------------------------

# pretty print JSON :D

print(json.dumps(jsons, indent=5, sort_keys=True, separators=(". ", " = ")))
