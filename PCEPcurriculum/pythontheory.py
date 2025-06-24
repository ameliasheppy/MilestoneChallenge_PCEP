# we write simple computer programs.

# computer program = a collection of instructions executed by a computer

# intstruction list = the set of instructions the given computer can execute; written in the form of machine code

# vmachine code is ugly and can't be read by humans.

# we use high-level langs like python to make source code. they are similar to natural langs used by humans.

# how does our source code get translated into machine code?

# something takes it and transforms it so computers can exe the program.

# can be done with compilation or interpretation.

# compilation takes the source code only once into an exe file. get an ex file as a result of compilation. give the exe file to anyone you want to use. compile the source code once, use it everywhere.

# interpretation happens on the fly, everytime you run programs. but everyone needs the interpreter to run it and translate the source code into machine code. need to run a second time? interprets again! share the code with friends? they need an interpreter!

# PYTHON IS A HIGH LEVEL INTERPRETER LANG!!

# py exe instructions from top to bottom.

# throws errors based on checking 3 elements: lexis, syntax, semantics

# lexis = some words can't be var names. keywords are part of lexis of py

# syntax = learns of writing py. input func needs input func name then ()

# semantics = can't add two args to input, that would give TypeError.

print(7 // 2)


x = 11
y = 4
x = x % y
x = x % y
y = y % x
print(x, y)
