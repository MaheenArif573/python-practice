# ord() or text.encode('ascii')
import numpy as np

def count_characters(t_str):
    temp_str = t_str.lower()
    temp_str = temp_str.replace(" ","")
    ascii_list = [(ord(c) - 97) for c in temp_str]
    dict = {}

    for char in temp_str:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def first_unique_letter(str):
    list = count_characters(str)
    for i in list:
        if list[i] == 1:
            return i
        else:
            continue
    print("There is no unique character in the string.")

string = input("Enter string: ")
char = first_unique_letter(string)

print("First unique letter in the string is", char)