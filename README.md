# Introduction to Object-Oriented Programming

### Packages

Packages and modules are pre-made blocks of code that can be used to perfor a particular task without the need to add your own code. They can be simply imported using the ```import``` command. It is also possible to import individual functions using the command ```from [package] import [function]```. This has the advantage that the function can suimply be called by its name, rather than needing to specify the package name for every function call.

#### os and sys

These tow packages are useful for doing system-related tasks, such as getting the current working directory (an obvious use case for this would be contructing a filepath for saving or retrieving files).

##### Math - Sample code discussion

The ```math``` libvrary contains a large amount of functions and values commonly used in mathematics. These are commonly used to perform operations such as rounding.

An example of this is shown here:

```

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

Abstraction is the process of taking away characteristics to reduce something to an essential set of characteristics. User when modelling objects using classes and minimising the amount of information necessary for a user of a function to know in order to get usable software.

#### Inheritance

This means that we can, and should, create "child classes", which take the properties of a "parent class" and "inherit" their traits as a starting point. For example, you might have a person class, but then have classes based on this such as worker, student, or similar.

#### Encapsulation

This means hiding data internal to a class from a client or external user. Use underscores to signal to other programmers that we do not want a variable changed. e.g. to indicate that ```var``` is private, we would define it as ```_var``` in our function.

#### Polymorphism

This is the philosophy of having many forms availalbe. This means you can overwrite methods from a parent class without changing the parent class. This means that if you had an employee class, you might write a different "pay" method depending on the way the emplyee was paid (e.g some are salaried, some hourly, some get bonuses, etc etc.)


#### In practice - Animal class and child classes

To demonstrate this, we create a quick class called Animal, containing a few typical features an animal might have:

```

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

