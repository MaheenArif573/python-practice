num = int(input("Enter your number: "))

remainder = 0
digits = []

while num > 0:
    remainder = int(num % 10)
    num = num // 10
    digits.append(remainder)

digits.reverse()
print(digits)