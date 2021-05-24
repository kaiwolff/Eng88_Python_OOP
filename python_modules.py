#What are Python Modules/packages?

#Packages and nmodules are built-in blocks of code you can use to fulfil certain purposes, such as generating a random number, or performing a particular mathematical operations. These are available from Python's libraries directory, and can be imported using the "import" command. There is also full documentation available, if the user comes across a function in someone else's code and isn't sure what the function actually does.
#Let's try this out
#
# import random
# print(random.random())
#the above calls the "random" fucntion frokm teh random library to generate a number between 0 and 1. Can also import only singular functions using, for exampel "from random import random. This will only import the particular function. The advantage is that we would no longer have to type random.random(), but rather can just type random() for a random number.

# from random import random
# print(random())
# import math
#
# num1 = 23.66
# print(num1)
# print(math.ceil(num1))
# print(math.floor(num1))

#task:generate a number USING RANDOM. if the number inumber input is >= .50, apply ceil. if less than .50, apply floor()/

from random import random
import math

num1 = random()
print(num1)
if num1 >= 0.5:
    print(math.ceil(num1))
else:
    print(math.floor(num1))

