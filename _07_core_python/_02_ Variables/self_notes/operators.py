#operators;
#operators are used to perform operations on variables and values.
#python divides the operators in many types;
#arithmetic operators;
#Addition
#Subtraction
#multiplication
#division
#modulus
#exponentiation
#floor division

x = 2
y = 3

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)

#assignment operators;
#these are used to assign values to variables:

x += 2 #  x = x + 2
x -= 4  # x = x - 4
x *= 3  # x = x * 3
x /= 3 # x = x / 3
x %= 3 # x = x % 3
x //= 3 # x = x // 3
x **= 3 # x = x ** 3


#Comparison operators;
#these are used to compare two values:
a = 5
b = 3
print (a == b)  # 5 is not equal to 3 so it is false
print (a < b)   # false because 5 is not less than 3
print (a > b) # true because 5 is greater than 3
print (a != b) # true bcz 5 is not equal to 3
print ( a >= b) # true bcz 5 is greater than or equal to 3
print ( a <= b) # false bcz 5 is neither less than or equal to 3

#Logical operators;
#these are used to combine conditional statements:
#AND;
x = 5
print(x > 3 and x < 10) # true
#OR;
print(x > 3 or x < 4) # true
#NOT;
print(not(x > 3 and x < 10)) # false bcz it reverse the result

#Identity operators;
#is;
x = ["swetha", "navya"]
y = ["swetha", "navya"]
z = x

print(x is z) # true bcz z and x are same
print(x is y) # false
print(x == y) #

#Membership operators;
#in;
print("navya" in x) # true bcz a sequence with the value "navya" is in the list
#not in;
print("teja" not in x) # true bcz a sequence with the value "teja" is not in the list










