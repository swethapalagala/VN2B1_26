'''
time period of service                 bonus
 more than 10 years                     10%
 >=6 and <=10                            8%
 less than 6 years                       5%

'''

salary = int(input("enter salary:"))
serviceyear = int(input("enter serviceyear:"))
if serviceyear > 10:
    bonus = salary*0.10
    print("bonus:",bonus+salary)
elif 6 >= serviceyear <= 10:
    bonus = salary*0.08
    print("bonus:",bonus+salary)
else:
    bonus = salary*0.05
    print("bonus:",bonus+salary)
