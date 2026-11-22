# ord() or text.encode('ascii')
import numpy as np
"""
if len(rom_num) == 2:
    for i in rom_num:
        if i not in roman_list:
            print("Invalid Roman Number entered")
            break
        else:
            if rom_num[0] < rom_num[1]:
                int_num = dict[rom_num[1]] - dict[rom_num[0]]
            else:
                int_num = dict[rom_num[1]] + dict[rom_num[0]]
else:
    for i in rom_num:
        if i not in roman_list or rom_num[i] < rom_num[i - 1]:
            print("Invalid Roman Number entered")
            break
        else:
            int_num += dict[i]

print("Integer Number of Roman number", rom_num, "is", int_num)
"""

dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C':100,
    'D': 500,
    'M': 1000
}

rom_num = input("Enter your roman number to convert into integer: ")
rom_num = rom_num.split()
roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
rom_pairs = ['IV', 'IX', 'XL','XC', 'CD', 'CM']
int_num = 0

def sub_case(r_n):
    flag = 0
    for i in range(len(r_n) - 1):
        char = r_n[i] + r_n[i + 1]
        if char not in rom_pairs:
            if r_n[i] < r_n[i+1]:
                print("Invalid Roman Number entered")
                break
            else:
                continue
        else:
            flag += 1
        if flag > 1:
            print("Invalid Roman Number entered")
            break
        else:
            continue

def Invalid_check(r_n):
    for num in r_n:
        if num not in roman_list:
            print("Invalid Roman Number entered")
            break
        elif rom_num.count('I') > 3 or rom_num.count('X') > 3 or rom_num.count('C') > 3 or rom_num.count('M') > 3:
            print("Invalid Roman Number entered")
            break
        else:
            sub_case(r_n)


