height_cm = input('Enter your height in CM: ')
float_height_cm = float(height_cm)
print('Your height in feet is ', float_height_cm/30.48)

# or can just type cast:
dog_age = int(input("How old is your dog?"))
print("Your dog was born in: ", 2025-dog_age)

# can also cast to a string but it's more rare. will mostly cast to int or floats

# make a salary calculator!
hours = float(input("How many hours did you work last month?"))
salary = float(input("What is your hourly rate?"))
print('Last month, you earned ', hours * salary, 'dollars!')

# more about operators:
# wth is a binary operator? uses TWO operands!
2 + 5
# unary operators work with one operand
print(+12)

# then there is OOO (PEMDAS)
(2 + 3) * 2

# floating point numbers are super precise:
# they are stored in mem as long chains or 0 and 1's
print(0.1)
# see the full math trickines of Py
print(0.1 + 0.1 + 0.1)
# the precision of floats in py is limited!
print(2 ** 3 ** 3)
# the exponentiation operator starts at the right, instead of the left like the rest

# keyword args are named args
print('Hello. ', end='.')
# the end arg adds a new line char
print('Py speaks!')

# kwargs are optional!
print('Sep is a default value of a space char.')
name = 'afs'
print('Your name is ', name, 'friendo!', sep='-')

# can use both at the same time


# bitwise operators
# 1 KB = 1,000 bytes = 8,000 bits (or sometimes 1,024 bytes)
# 1 MB = 1,000,000 bytes = 8,000,000 bits (or sometimes 1,048,576)

# no one really does bit operations....

bit_1 = 1
bit_2 = 0

# & = and
print(bit_1 & bit_2)

# | = or
print(bit_1 | bit_2)

# ^ = logical XOR (exclusive OR)
print(bit_1 ^ bit_2)

# ~ logical NOT
print(bit_1, bit_2)

# << and >> are shifters to move left or right in the decimal system
print(12 << 3)
print(12 >> 2)
