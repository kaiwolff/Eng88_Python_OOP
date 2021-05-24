# Introduction to Object-Oriented Programming

### Packages

Packages and modules are pre-made blocks of code that can be used to perfor a particular task without the need to add your own code. They can be simply imported using the ```import``` command. It is also possible to import individual functions using the command ```from [package] import [function]```. This has the advantage that the function can suimply be called by its name, rather than needing to specify the package name for every function call.

#### os and sys

These tow packages are useful for doing system-related tasks, such as getting the current working directory (an obvious use case for this would be contructing a filepath for saving ro retrieving files)