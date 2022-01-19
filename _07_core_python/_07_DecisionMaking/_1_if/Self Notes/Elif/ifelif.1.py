'''
Amount           Shorts          Pants           shirts
0-100              -               3%               5%
101-200            5%              8%               10%
201-300            10%             12%              15%
Above 300          18%             20%              22%

'''

sh = int(input("Enter shorts amt :"))
p = int(input("Enter pants amt :"))
sht = int(input("Enter T-shirts amt :"))

if sh <= 0 :
    print("Enter valid amt for shorts")
else:
 if sh > 0 and sh <= 100 :
        print("bill ", sh)
 elif sh >= 101 and sh <= 200 :
        discount = 0.05*sh
        print("5% discount on sh",discount)
        print("bill for sh",sh-discount)
 elif sh >= 201 and sh <= 300 :
     discount = 0.1*sh
     print("10% discount on sh",discount)
     print("bill for shorts",sh-discount)
 else:
     discount = 0.18*sh
     print("18% discount on shorts",discount)
     print("bill for shorts",sh-discount)

 if p <= 0 :
     print("Enter valid amt for pants")
 else :
     if p > 0 and p <= 100 :
        discount = 0.03*p
        print("3% discount on pants",discount)
        print("bill for pants",p-discount)
     elif p >= 101 and p <= 200 :
         discount = 0.08*p
         print("8% discount on pants",discount)
         print("bill for pants",p-discount)
     elif p >= 201 and p <= 300 :
         discount = 0.12%p
         print("12% discount on pants",discount)
         print("bill for pants",p-discount)
     else :
         discount = 0.2*p
         print("20% discount on pants",discount)
         print("bill for pants",p-discount)
 if sht <= 0 :
     print("Enter valid amt for T-shirts")
 else :
     if sht > 0 and sht <= 100 :
         discount = 0.05*sht
         print("5% discount on T-shirts",discount)
         print("bill for T-shirts",sht-discount)
     elif sht > 100 and sht <= 200 :
         discount = 0.1*sht
         print("10% discount on T-shirts",discount)
         print("bill for T-shirts",sht-discount)
     elif sht > 200 and sht <= 300 :
         discount = 0.15*sht
         print("15% discount on T-shirts",discount)
         print("bill for T-shirts",sht-discount)
     else :
         discount = 0.22*sht
         print("22% discount on T-shirts",discount)
         print("bill for T-shirts",sht-discount)


