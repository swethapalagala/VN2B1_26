#If-Else statement:
#if the condition  inside 'If' is false,then we use if-else.
#if the  ondition is true,then program will execute the code under if-condition
#if the condition is false,it will execute the code under else part.

p = 100
q = 50
if p < q:
    print("p is greater than q") #false
else:
    print("q is not greater than p")

#elif-condition;
#this keyword is used in python if the previuos conditions were not true,then we can usethis condition.
#there is no limit we can include after an if statement you can add as many as you need into the program.

x = 20
y = 40
if x > y:
    print("x is greater") #false
elif x == y:
    print("x and y are equal") #false
else:
    print("y is greater than x") #true

'''
# Grade A  >=75
# Grade B >=60 and <75
# Grade C  >=35 and <60
# fail         < 35
'''
marks = int(input("enter marks :"))
if marks < 0 or marks > 100:
    print("please enter valid marks between 0 to 100")
else:
    if marks >= 75:
        print("result : Grade A ")
        if marks == 90:
            print("result : GOOD")
        elif marks >= 60 and marks < 75:
            print("result : Grade B")
        elif marks >=35 and < 60:
            print("result: Grade C")
        else:
            if marks <35:
                print("result : fail")











