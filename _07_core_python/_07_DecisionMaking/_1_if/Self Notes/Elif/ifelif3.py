''''
#Below 25---D
#25 to 45---C
#45 to 50---B
#50 to 60---B+
#60 to 80---A
#Above 80---A+
'''
print("---Grade of user---")

percentage = int(input("Enter percentage :"))
if  0 < percentage < 100:
    print("please enter valid percentage between 0 to 100")

    if percentage < 25 :
        print("Result : Grade D")
    elif   25 <= percentage < 45:
        print("Result : Grade c")
    elif  45 <= percentage < 50:
        print("Result : Grade B")
    elif  50 <= percentage < 60:
        print("Result : Grade B+")
    elif  60 <= percentage < 80:
        print("Result : Grade A")
    else:
        print("Result : Grade A+")
else:
    print("percentage not valid")





