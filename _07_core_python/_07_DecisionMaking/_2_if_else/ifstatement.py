#Decision Making:
#Here is comes to take situation where we need to take some decision.
#then further execution of the code depends.
#decision making statements decides the output or result of a program.
#in python we can make decision using-If statement
                                    #If - Else statements if, else

#If-statement:
#it is the simple decision making statement in python programming.
#it is used to decide weather a particular statement is True or not.
#if the condition is true,the statement inside the 'IF' will execute.
#if the condition is false then it will not execute.

#exp;
x = 10
if x == 10 :
    print('x is 10')

#by using arithmetic operators in If-statement  ;
x = 10
y = 30
if x+y:
    print("addition of x and y:",x+y)
if x-y:
    print("subtraction of x and y:",x-y)
if x*y:
    print("multiplication of x and y:",x*y)
if x/y:
    print("division of x by y:",x%y)
if x**y:
    print("exponentiation of x and y:",x**y)
if x%y:
    print("modulus of x and y:",x%y)
if x//y:
    print("floor division of x and y:",x//y)



#by using comparison operators;
a = 20
b = 10
c = "python"
if a == b:
    print("a and b are equal") #false
if a != b:
    print("a and b are not equal") #true
if a > b:
    print("a is greater than b") # true
if a < b:
    print("a is less than b") # false
if a >= b:
    print("a is greater than are equal to b") #true
if a <= b:
    print("a is less than are equal to b") #false
if c == "python":
    print("string:",c)


#If statement using logical operators;
d = 25
e = 50
if d>20 or e>45:
    print("0r condition is executed")
if d<20 or e>45:
    print("Or condition is executed")
if d>20 and e>45:
    print("And condition is executed")
if e<20 and e>45:
    print("And condition not satisfied") #false


#if statement using identity operators;
m = "class"
n = "room"
o = "room"

if m is n:
    print("strings are same") #false
if m is not o:
    print("strings are not same") #true
if  o is n:
    print("strings are same") #true










