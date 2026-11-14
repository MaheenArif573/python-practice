string = input("Enter string: ")
reverse_string = ""

for i in range(len(string) - 1, -1, -1):
    reverse_string += string[i]

print("Reverse string: ", reverse_string)