user_age = int(input('What is your age? '))

if user_age > 30:
    print('You are over thirty years old!')
elif user_age == 30:
    print('You are exactly thirty!')
else:
    print("Age comes in numbers, homie!")

# remember, in Py, = is for assignment, == is for checking equality

password = input('what is the secret pw? ')
if password != 'secret':
    print('not correct!')
else:
    print('correct password')

if password != 'secret' and user_age == 40:
    print('You need to figure out the secret you are missing at 40!')
else:
    print('Good job knowing the secret!')

# bools have PEMDAS
# 1. and -> 2. not -> 3. or

# nested if statements
travely = input('Do you like to travel?')

if travely == 'y':
    print('Good, me too!')
    answer2 = input('Do you like Asia? y/n ')
    if answer2 == 'y':
        print('Go to NC instead!')
    else:
        print('Same! I wouldn\'t want to fly that far!')
else:
    print('Boooooooo!')

# loops are used to do one or more instructions until a condition is met
# while condition:
    # do_something()

counter = 1
while counter < 11:
    print(counter)
    counter += 1  # increment!

print('Finished!')

# if the condition is false from the beginning, like this, Py won't exe the loop
while counter > 11:
    print(counter)
    counter += 1

print('Finished bc didn\t work!! ')

# an infinite loop won't end

# easy way for multi-line prints:
print('''
==============================
===== Secret Number Game =====
==============================
      ''')

secret_number = 14
user_guess = int(input('Please guess a number: '))
while secret_number != user_guess:
    print('Wrong!')
    user_guess = int(input('Try again to guess the number! '))
print('Perfect! You guessed the secret number!')

# for loops  are handy to go through all the elements in a specific instance
for char in 'hello':
    print(char)


for counter in range(1, 11, 3):
    print(counter)
print('Done counting!')

# break and continue
# break makes Py exit the loop and move on to the next instruction
while True:
    name = input('Enter your name to EXIT or close the program: ')
    if (name == "EXIT"):
        print('Bye! ')
        break
    print('Hello ', name)

# pass
# Why use pass? Loop syntax requires you put SOMETHING in the loop
# throw a pass in there to avoid errors and not break the program.
