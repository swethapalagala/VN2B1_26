''''
Function:
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.

creating a functiom:
In Python a function is defined using the def keyword.
To call a function, use the function name followed by parenthesis:
'''
def my_function():
    print("python from a function")
my_function()

def my_function():
    print('1' + '2')    #when i use integer in string it combines two values
my_function()           #by using integer without string it gives the sum of two values.

'''
Arguments:
Information can be passed into functions as arguments.
Arguments are specified after the function name.
Inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

'''

def my_function(*company):
    print(company)
my_function("hcl","infosys","dell","tcs")

#Arbitary Arguments,*Args:
#Arbitrary Arguments are often shortened to *args in Python documentations.
#If the number of arguments is unknown, add a * before the parameter name:


def my_function(*company):
    print("your company is:",company[2])
my_function("hcl","infosys","dell","tcs")
''''
#Parameter:
#The terms parameter and argument can be used for the same thing,
# the information that are passed into a function.
#A parameter is the variable listed inside the parentheses in the function definition.

Defult parameter value:
If we call the function without argument, it uses the default value.

#Passing a list as an argument:
In this we can send data types of argument to a function are (string,number,list,dictionary)....
It will be treated as the same data type inside the function.

'''
def my_function(values):
    for x in values:
        print(x)       #sending list as an argument,it will be a list when it reaches function.
values = [10,20,30]

my_function(values)











