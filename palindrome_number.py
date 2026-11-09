num = int(input("Enter your number: "))

remainder = 0
digits = []

while num > 0:
    remainder = int(num % 10)
    num = num // 10
    digits.append(remainder)

reverse = digits

if digits == reverse:
    print("Number is a palindrome.")
else:
    print("Number is not a palindrome.")
