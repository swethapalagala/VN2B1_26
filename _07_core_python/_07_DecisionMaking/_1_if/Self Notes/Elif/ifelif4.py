#2.
'''
till five days : Rs 2/day.
six to seven days : Rs 3/day.
11 to 15 days : Rs 4/day.
After 15 days : Rs 5/day.
'''
print("---charges applied---")

days = int(input("enter number of days :"))
if days <= 0 :
    print("invalid input")
elif days > 0 and days <= 5:
    print("charges :", days*2)
elif days >= 6 and days <= 10:
    print("charges :", days*3)
elif days >= 11 and days <= 15:
    print("charges :", days*4)
else:
    print("charges after 15 days:", days*5)
