# Introduction to Object-Oriented Programming

### Packages

Packages and modules are pre-made blocks of code that can be used to perform a particular task without the need to add your own code. They can be simply imported using the ```import``` command. It is also possible to import individual functions using the command ```from [package] import [function]```. This has the advantage that the function can suimply be called by its name, rather than needing to specify the package name for every function call.

#### os and sys

These two packages are useful for doing system-related tasks, such as getting the current working directory (an obvious use case for this would be constructing a filepath for saving or retrieving files).

##### Math - Sample code discussion

The ```math``` library contains a large amount of functions and values commonly used in mathematics. These are commonly used to perform operations such as rounding.

An example of this is shown here:

```python

from random import random
import math

num1 = random()
print(num1)
if num1 >= 0.5:
    print(math.ceil(num1))
else:
    print(math.floor(num1))
```

We are actually using two packages here: math and random. Howver, we only imported the function ```random``` from the package of the same name, which means we can call it like a function and don't have to mention the name of the packaged anymore.

To use the ceil and floor functions, we use the syntax ```math.[function]```.

#### Lambda
This type of function takes multiple arguments and returns a singular value. It has built-in functionality that helps us work out certain things

### The Four Pillars of OOP

- Abstraction
- Inheritance
- Encapsulation
- Polymorphism

#### Abstraction

Abstraction is the process of taking away characteristics to reduce something to an essential set of characteristics. When modelling objects using classes ,minimising the amount of information necessary for a user of a function to know in order to get usable software.

#### Inheritance

This means that we can, and should, create "child classes", which take the properties of a "parent class" and "inherit" their traits as a starting point. For example, you might have a person class, but then have classes based on this such as worker, student, or similar.

#### Encapsulation

This means hiding data internal to a class from a client or external user. Use underscores to signal to other programmers that we do not want a variable changed. e.g. to indicate that ```var``` is private, we would define it as ```_var``` in our function.

#### Polymorphism

This is the philosophy of having many forms available. This means you can overwrite methods from a parent class without changing the parent class. This means that if you had an employee class, you might write a different "pay" method depending on the way the employee was paid (e.g some are salaried, some hourly, some get bonuses, etc etc.)


#### In practice - Animal class and child classes

To demonstrate this, we create a quick class called Animal, containing a few typical features an animal might have:

```python

#animal fil to create Animal class
#Notice the convention. Classes are in CamelCase

class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return "Keep breathing to stay alive"

    def eat(self):
        return "nom nom nom."

    def move(self):
        return "moving all around the world"


#now, we need to create an object of our Animal class to test.

# cat = Animal()
# print(cat.breathe()) # breathing for cat is abstracted. It is possible to just call the breathe function.

#Important point is that a class needs to be instantiated (an object of the class needs toi be created) in order to call the methods


```

we can import this into another class, which we note as a child of the Animal class using the syntax ```ChildClass(ParentClass```. If we are writing in a separate file as we have done here, we also need to import the parent class we are basing our work on using, in this case, the command ```from animal import Animal```. We can also inherit further, with "grandchild" classes, which we have done in the other files. Notice that we can call all the way up the inheritance tree, even being able to call Animal methods in the snake class even though it is the "great-grandchild" of that class.

Taking the example below, we see the great-grandchild of Animal, Python. An object of the python class can use methods from any of the predecessors, as the print statements show:

```python
from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return "yum yum yum, that was a big meal"

    def climb(self):
        return "Up we go"

    def shed_skin(self):
        return "Time to grow out of myself"


my_python = Python()

print(f"From Animal class: {my_python.breathe()}")
print(f"From Reptile object: {my_python.seek_heat()}")
print(f"From Snake class: {my_python.use_tongue_to_smell()}")
print(f"From Python class: {my_python.digest_large_prey()}")
```


## Simple Test Case - A Calculator in Two Parts

This task is similar to the one done in Week 1, but to demonstrate the ability to inherit, it is split into two parts, a simple calculator (stored in oop_calculator), and a slightly mroe advanced calculator stored in functional_calculator.

We start with the SimpleCalculator class:

```python
class SimpleCalculator:

    def add(self, value1, value2):
        return value1 + value2


    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2
```

This contains four functions, for addition, subtraction, multiplication and division. If an objec tof SimpleCalculator is instantiated, the functions can be accessed, for example like below:

```python
calculator_object = SimpleCalculator()
print(calculator_object.add(1,2))
```

We now want to add mroe functionality to the calculator, in this case a check whether two numbers are divisible, a converter for inches to centimetres, and a function to calculate the area of a triangle.

To do this, we create a child class of SimpleCalculator, which I have called FunctionalCalculator:

```python
from oop_calculator import SimpleCalculator

class FunctionalCalculator(SimpleCalculator):
    #add mroe functionality compared to the simple calculator
    def __init__(self):
        super().__init__()

    def inchtocm(self, value1):
        return value1 * 2.54

    def triangle_area(self, height, width):
        return height*width/2

    def divisible(self, value1, value2):
        if value2 == 0:
            return False
        elif value1 % value2 == 0:
            return True
        else:
            return False

```

The functions we have added are available only in FunctionalCalculator. However, the key thing is the below block of code:

```python
    def __init__(self):
        super().__init__()
```

using the ```super().__init__()``` statement means we are telling the interpreter to set up the initial coinditions of our class in the same way as its parent class, or superclass. We can therefore access all of SimpleCalculator's functions, with the new functions being added on for our FunctionalCalculator class. This is what is known as inheritance, and a key aspect of OOP.