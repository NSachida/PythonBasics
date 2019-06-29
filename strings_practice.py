# counting occurrences of a substring in a string
# learning split() method

string = "Computer science is the study of processes that interact with data and that can be represented as data in the form of programs"
substring = "data"
splitted_string = string.split(" ")
counter = 0
for word in splitted_string:
    if word == substring:
        counter += 1
print(substring, "occurrences:", counter)

# after discovering count() method :P

counter = string.count(substring)
print(substring, "occurrences:", counter)

# reversing a string
# learning join() and reversed() methods

reversed_substring = ''.join(reversed(substring))
print("reversed string", substring, reversed_substring)

# finding smallest and largest word in a given string
# getting used to syntax

min_len = max_len = len(splitted_string[0])
max_word = min_word = splitted_string[0]
for i in splitted_string:
    if len(i) < min_len:
        min_len = len(i)
        min_word = i
    elif len(i) > max_len:
        max_len = len(i)
        max_word = i
print("max word", max_word, max_len, "min word", min_word, min_len)

# counting occurrences of all characters within a string
# getting used to dictionaries and strings

char_dict = dict()
for letter in string:
    c = string.count(letter)
    char_dict[letter] = c
print("Char Dictionary:",char_dict)

# string characters balance Test
# s1 and s2 is balanced if all the chars in the string1 are there in s2
# getting used to syntax

test_string = "computer"
is_balanced = True
for i in test_string:
    if i not in string:
        is_balanced=False
print("Are strings balanced?", is_balanced)