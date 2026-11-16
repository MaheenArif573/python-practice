string = input("Enter your string: ")
reverse_string = string[:: -1]

if string == reverse_string:
    print("Number is palindrome.")

else:
    print("Number is not palindrome.")