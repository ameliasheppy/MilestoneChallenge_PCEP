def doMath(a, b):
    return a * b


print(doMath(9, 8))
print(doMath(2, 3))


def fizzbuzz(number):
    # check if the number is divisible by 15, 3, and 5
    result = []
    for i in range(1, number):
        if i % 15 == 0:
            result.append("Fizzbuzz!")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result


print(fizzbuzz(24))


def gausses_trick():
    total = 0
    for number in range(101):
        total = total + number
    print(total)


gausses_trick()

for i in range(0, 11, 5):
    print(i)

# countdown with a loop
for i in range(5, -1, -2):
    print(i)

# a function is a piece of code with one job
print('Hello, World!')

# escape characters when you act like a fool with quotation marks
print('I\'m studying Python!')

# add a newline char to a string
print('I\'m studying\nPython!')

# think of variables as cells in Excel, just a box of data.
# give them an initial value.
greeting = 'Hello Friend!'
print(greeting)

greeting = 'Hi Everybody!'
print(greeting)

# define, then call! Don't call above assignment.

# data types
age = 25
age1 = '25'
age2 = 25.0
age3 = True
print(age, age1, age2, age3)
print(type(age), type(age1), type(age2), type(age3))

# numerical representations
big_num = 1_000_000
print('1,000,000 = ', big_num)

# can use for scientific notation 3 * 10(4th power) = 30000
# e/E for the really big or small nums!
print(0.00000000000000000000000000000003, '3e-32')

# can also do octal or hexadecimal
# start with 0O or 0o are octal
# start with 0X or 0x are hexadecimal

# do some Python math!
2 + 3
5-4
print(3 * 5)
# standard division retruns a float:
6/2
print(7/2)
# integer division returns the nearest whole  num rounded down
6//2
print(7//2)
# modulus operator
6 % 2
print(5 % 1, 20 % 30)

# increment with Py
numberIs = 2
numberIs += 7
print(numberIs)

# concatenate strings
print('dogs', 'are', 'the', 'best :)')

# multiply strings!
print("beach trip please! " * 2)

# str != nums!
print('23 + 5 != \'23\' + \'5\'')

# functions in python can: 1. cause some effect or 2. return a value
