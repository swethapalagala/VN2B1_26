x = int(input("enter num of kms:"))
if x <= 10:
    y = x*11
    print("charges for kms:",y)
elif x >= 11 and x <= 90:
    z = x*10
    print("charges for kms:",z)
else:
    s = x*9
    print("cgarges for next kms:",s)
