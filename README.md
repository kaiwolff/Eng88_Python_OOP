# Introduction to Object-Oriented Programming

### Packages

Packages and modules are pre-made blocks of code that can be used to perfor a particular task without the need to add your own code. They can be simply imported using the ```import``` command. It is also possible to import individual functions using the command ```from [package] import [function]```. This has the advantage that the function can suimply be called by its name, rather than needing to specify the package name for every function call.

#### os and sys

These tow packages are useful for doing system-related tasks, such as getting the current working directory (an obvious use case for this would be contructing a filepath for saving or retrieving files).

##### Math - Sample code discussion

The ```math``` libvrary contains a large amount of functions and values commonly used in mathematics. These are commonly used to perform operations such as rounding.

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
