# ord() or text.encode('ascii')

def count_characters(t_str):
    temp_str = t_str.lower()

    ascii_list = [(ord(c) - 97) for c in temp_str]
    list = np.zeros(26, dtype=int)

    for i in range(len(ascii_list)):
        c = ascii_list[i]
        list[c] = list[c] + 1

    return list

def anagram(str, str2):
    list_1 = count_characters(str)
    list_2 = count_characters(str2)

    if list_1.all() == list_2.all():
        print(str, " is an anagram of ", str2)
    else:
        print(string2, " is not an anagram of ", string)

import numpy as np

string = input("Enter string: ")
string2 = input("Enter string to be checked: ")

if len(string) == len(string2):
    anagram(string, string2)
else:
    print(string2, "is not an anagram of", string)
