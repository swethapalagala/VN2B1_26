'''
 Marked price              Discount
    >10000                     20%
    >7000 and <=10000           15%
    <=7000                      10%
'''

markedprice = int(input("enter markedprice:"))

if markedprice > 10000:
    discount = markedprice*0.2
    print("discountprice is",discount)
    print("aftr discount:",markedprice-discount)
elif markedprice <= 10000 and markedprice > 7000:
    discount = markedprice*0.15
    print("discountprice is",discount)
    print("aftr discount:",markedprice-discount)
else:
    discount = markedprice*0.1
    print("discountprice is",discount)
    print("aftr discount:",markedprice-discount)
    
