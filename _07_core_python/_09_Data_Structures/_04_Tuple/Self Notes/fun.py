#Global variables;
# variables that are created outside of a function.
#  Global variables can be used by everyone,both inside and outside.

a = "good"
def myfunc():
    print("very "+ a)
myfunc()

#global keyword;
# if you create a variable inside a function,that variable is local and can only be used inside that function.
#To create a global variable inside a function,you can use the global keyword.
b= "language"
def myfunc():
    global b
    b = "fantastic"
myfunc()

print("python is " + b)
