# All Py programs can use built-in functions such as print(), input(), and len()
# Also comes with a set of modules called the standard library.
# Those modules are Python programs that contain a related group of functions.
# What does that mean though?
# The math module contains a group of functions to do math with. The random module has random number-related functions.

# Let's use a module:
import random

for i in range(3):
    print(random.randint(1, 10))
