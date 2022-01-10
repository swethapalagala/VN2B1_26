#Data types :
# 1. Interger - 10,20,30
#2. Float - 100.20,144.344
#3. Boolean - True, False
#4. String - 'name',"adress","10","True"


x = 10
print("type of x : ", type(x))
print("Id of x : ", id(x))

x = 20 + 30 - 40 * 32 / 3
print("final value:", x)
print("type of x : ", type(x))
print("Id of x : ", id(x))

swetha = True
print("Type of swetha : ", type(swetha))

a = 20
print("integer:", type(x), id(x))
b = 33.3
print("float:", type(b), id(b))
str = "30"
print("type of str:", type(str), id(str))

#conversions:
print("----Type conversions--------")
'''
int()
float()
complex()
bool()

'''

x = 10
print("value : ",x, type(x))
#convert to float
x = float(x)
print("value : ",x, type(x))

x = 1
print(x, type(x))

x = bool(x)
print(x, type(x))

x = 12
print(x, type(x))
x = bool(x)
print(x, type(x))


