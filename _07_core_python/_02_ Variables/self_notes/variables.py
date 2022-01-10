# variables are containers for storing values.
# First we have to assign a value for the variable.
# The type of variable,we can be change after the declaration set.
# For string variables we can use single or double quotes.
# Variable name we have to start with a letter/ underscore character.
# variable name we cannot start with a number.
# x = 10
# In the above operation
 #   L.H.S = R.H.S
  #  x represents the variable,
  #   10 is the value.
  # = is the operator.
# Here execution starts from R.H.S to L.H.S .
# it converts to binary format.
x=10
print(x)
print(id(x))
# Aftr executing the variable the R.H.S is 2739125158416.

# NUMBER SYSTEM;
y=20
print(y)
print(id(y))
print (type(y))
# type(x) is 'int'
 # if
z=10.5
print(z)
print(id(z))
print (type(z))


#type(x) is 'float'

#BOOLEAN;
X=True
print(id(X))
print (type(X))
#by using string;
x="fruit"
print(x[2])

#one value to multiple variables;
a = b = c = 30
print(id(a))
print(id(b))
print(id(c))

#multiple values to multiple variables;
x,y,z=20,30.3,False

print(x,y,z)
print(id(x),id(y),id(z))

a=10,20,30
print(a)
print (type(a))

#first character should not be number ;
_3 = 'swetha'
#here by using underscore we can use the number as first character

#delete;
c=10
d=30
print(c,d)
del c,d
print(c,d)


#Global variables;
# variables that are created outside of a function.
#  Global variables can be used by everyone,both inside and outside.

e = "programming language"
def myfunc():
    print("python is " + e)

myfunc()

#global keyword;
# if you create a variable inside a function,that variable is local and can only be used inside that function.
#To create a global variable inside a function,you can use the global keyword.

def myfunc():
    global x
    x = "fantastic"
 myfunc()

print()























