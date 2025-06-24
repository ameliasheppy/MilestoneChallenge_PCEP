# basic data types only hold one thing: int = 2

# container data types hold more than one dt: list, tuples, dictionaries

# lists hold multiple values of the same types.
cities = ['LA', 'HB', 'SD', 'PCB', 'FB']

for city in cities:
    print(city)

# lists start at 0

# access list items by index!

print(cities[1], 'is my favorite!')
print(cities[-1], 'is where I\'d move!')

# use list slicing to only access a few elements
print(cities[0:3:2])

# slicing returns a new list
# get two -> end
print(cities[3:])
# print first half
print(cities[:2])
# print whole new list
print(cities[:])

# access by index = single element. access with slicing = new list

# how to del from list?
del cities[1]

print(cities)

cities.insert(1, 'HB')
print(cities)

del (cities[0])
print(cities)

# add to a list
# methods exist alongside the data they belong to
book_ratings = [7, 8, 3, 10]
book_ratings.append(8)

print(book_ratings)

# methods are invoked by a .(method) after the data they are called on
# methods are functions that belong to specific data

# iterating over lists:
# sequences are ds that can be browsed one by one. can iterate lists the same way!

for city_index in range(len(cities)):
    print('Index is', city_index, ' | Current city: ', cities[city_index])

spendings = [32, 48, 10]
sum = 0
for item in spendings:
    sum += item
print('You spent', sum)

name1 = input('First number: ')
name2 = input('Second number: ')
print('Before swapping: ', name1, name2)
# name1 = name2
# name2 = name1
# print('After swapping: ', name2, name1)

# Py has a swapping method:
name1, name2 = name2, name1
print('After swapping: ', name1, name2)

# py can sort cities
cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

# don't want to mess with original list?
sorted(spendings)
print(spendings)

# sort is method working on the list itself. sorts in place. sorted returns a brand new one without modifying the original list!

# checking the presence of elements:
for char in 'happy':
    print(char)

user_city = input('City to vacation in? ')
if user_city in cities:
    print('I want to go there too!')

if user_city not in cities:
    print('Not on my faves list!')

# name of var is contents usually
name_original = 'Jon Snow'

new_name = name_original
print(new_name)

name_original = 'Danny T?'
print(new_name)
# it changed when the original changed!

# reference is the place in mem where something is stored
# behind the scenes, both vars point to the same ref bc they share the same list.
# how to modify so can have two sep lists to modify?
# slice it!
original = [1, 2, 3]
new = original[:]
original[0] = -5

print('Original: ', original, 'New: ', new)

# can just get some elements of the list if wanted too

# list comprehensions bc this is ugly:
numbers_list = [1, 2, 3, 4]
numbers_list = []
for i in range(1, 51):
    numbers_list.append(i)
print(numbers_list)

# do a list comp:
numbers_list = [i for i in range(1, 10) if i % 3 != 0]
print(numbers_list)

# list comps made on the fly when you run program!

# nested lists
# put whatever you want in a list. kitchen sink, it holds them, but why would you? keep lists to one type if you can

cells = [['A', 'B', 'C'], [1, 2, 3]]
print(cells[0])
print(cells[1][2])

for x in cells:
    print('Element: ', x)

# want to access both? use a nested for loop!
for x in cells:
    for y in x:
        print(y)

# nested lists are like tables
table = [["A1", "A2"], ["B1", "B2"]]
for row in table:
    for column in row:
        print("Element: ", column)


# do this j's range of times!
table2 = [[i for i in range(1, 6)] for j in range(4)]
print(table2)

# adding and multiplying lists
us = ['NY', 'Chi']
uk = ['London', 'South']
both = us + uk
print(both)

new_spending = spendings * 3
print(new_spending)

# strings are sequences like lists
fav_mmc = 'Ivan'
print(fav_mmc[3])

print(fav_mmc[:])

print(fav_mmc.upper())

# tuples!
# similar to lists. collection of multiple elements
# create with ()
# write them however you want:
empty_tuple = ()
# mutable = freely updated like lists, add new, remove, swap
# tuples are immutable = assign a new tuple to a var, like I do
user_date = ("John", "KY", 1964, [234.4, 278.9, 284.0])
print(user_date)
print(type(user_date))
# can not append to tuples!
# can not del in tuples!
# can index or slice, but not to change!
print(user_date[1])

# lists are mutable, tuples are not

# reassign if you want
message = 'Welcome'
message = 'WELCOME!'
# but this will fail bc immutable:
# print(message[0]='w')

# tuple operations
# use len to count
print(len(user_date))
if 'John' in user_date:
    print('From the US!')


for el in user_date:
    print(el)


print(user_date * 3)

# use lists for when want many of same DT.
# use tuples when you want to group vals of different types that may be grouped together
# tuples don't only group related things

# tuples in lists, lists in tuples
cats = ('Tiger', 3)
dogs = ('Stormy', 1)
pets = [('Lemon', 1), ('Izzy', 5)]
for pet in pets:
    print("Name", pet[0], "Age:", pet[1])

# can add new things to a list inside a tuple like user_data
user_date[3].append(74.4)
print(user_date)

# tuple itself is immutable, but can modify a mutable el in a tuple!

# dicts!
# collections that store k/v pairs!
emails = {
    'amy': 'gmail',
    'jesse': 'hotmail',
    'ivan': 'it'
}

# access by key in []
print(emails["ivan"])

# can't provide val with key
# use .get
print(emails.get('tim'))
print(emails.get('jesse'))

# what can we do to dict?
grades = {}
grades['John'] = 'A-'
print(grades)
grades.update({"John": "A"})
print(grades)

if 'John' in grades:
    print('John got:', grades["John"])

# can do del grades['John]
# dicts were not ordered back in the day. They are now

for el in grades.keys():
    print(el)

for el in grades.values():
    print(el)
