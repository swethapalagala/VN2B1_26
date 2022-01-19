
Name=str(input("Enter the Name"))
mobile=int(input("Enter the number"))
price=int(input("Enter the amt"))

if price > 50000 and price <= 600000:
    print("laptop")
elif price > 45000 and  price <=49000:
    print("iphone")
elif price > 10000 and price <= 15000:
    print("ear buds")
elif price > 0 and price <= 1000:
    print("nokia keypad")
else :
    print("you cant get any product")




