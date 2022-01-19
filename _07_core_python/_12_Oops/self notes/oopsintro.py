#Class:
#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

#To Create a Class
#we have to use the keyword class:

class Employee:
   x = 5
print(Employee)

#Create Object:
#here we can use the class named Employee to create objects:

a = Employee()
print(a.x)

#The _init_() function:
#here we can understand the built-in_init_() function.
#all classes have a function called_init_(),which is always executed when the class is being initiated.
#we are using the _init_() function to assign values to object,
#properties or other properties that are necessary to do when the object is being created:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
x = Person("swetha",26)
y = Person("teja",28)

print(x.name,x.age)
print(y.name,y.age)

#Method:The method is a function that is associated with an object.
#In Python, a method is not unique to class instances.
#Any object type can have methods.


#Object methods:
#Objects can also contain methods,methods in object are functions,
#that belong to the object.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
       print("My name is " + self.name)

x = Person("swetha",26)
x.myfunc()

class Student:
    def __init__(self,name, year):
        self.name = name
        self.year = year
    def display(self):
        print(self.name,self.year)

P1 = Student("Btech", 2016)
P2 = Student("Mtech", 2020)

print(P1.name, P1.year)
P1.display()
P2.display()

#The self Parameter:
#The self parameter is a reference to the current instance of the class,
#and is used to access variables that belongs to the class.
#It does not have to be named self , you can call it whatever you like,
#but it has to be the first parameter of any function in the class:
#we can also modify the properties by changing values.
#we can also delte the properties from the object by using del keyword.
#we can also use pass statement to avoid getting an error.


''''
          Class                                           OBJECT

1	Class is used as a template for declaring           1.An object is an instance of a class.
    and creating the objects.                         
2. 	When a class is created,                            2.Objects are allocated memory space
     no memory is allocated.                               whenever they are created,
3.   The class has to be declared only once.             3.An object is created many times as per requirement.                                               
4.   A class is a logical entity.                        4.An object is a physical entity.
5.   A class cannot be manipulated as they are not       5.Objects can be manipulated.
     available in the memory.
6.   class does not contain any values which             6.Each object has its own values, 
     can be associated with the field.                     which are associated with it.

'''
class Dog:

   def __init__(self, name):
    self.name = name

   def func(self):
    print("I am  " + self.name)

x1 = Dog("poodle")
x2 = Dog("shihtzu")

x1.func()
x2.func()

class person:
    def__init__















