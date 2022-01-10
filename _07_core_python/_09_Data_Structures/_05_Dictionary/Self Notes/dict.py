#Dictionaries:
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered,changeable and do not allow duplicates.
#Used to store data values like a map,which,unlike other data types that hold only a single value as an element.
#Dictionary holds key:value pair. key-value is provided in the dictionary to make it more optimized.
#Dictionaries are written with curly brackets,and have keys and values:

list1=[1,2,3,4,5]
m_bill=[19.5,345,765,45,78]
e_data=[26,"swetha",60000,"female","Bangalore",560068,['213',"Mahadevpura"]]
#Address
print("Employee data:",e_data)

#Immutable:int float boolean string tuple
#Mutable  :list,dict,set

e_data={'e-id':26,
        'name':"swetha",
        'sal':60000,
        'Gender':"female",
        'loc':"Bangalore",
        'pin':560068,
        'address':{'Dno':'213','Area':"Mahadevpura"}
        }
mobile_no=int(input("Enter mobile no"))
e_data['mobile_no']=9550253224

print("Dictionary :", e_data)
print("Emp sal    :",e_data['sal'])
print("Emp area    :",e_data['address']['Area'])

#key properties:
#keys must be UNIQUE
#keys must be IMMUTABLE and values can be anything
#2.keys must be immutable and values can be anything
dict1 = {100: 20,
         200:{1:1,2:2},
         111.3: 26,
         True:"swe",
         'order list':[1,2,3,4,5],
         (1,2,3):(1,2,3),
        # [1,2,3] :{1:1,2:2}, #list is mutable so it is wrong
        #{1:1,2:2} :"hi"      #dict is mutable so it is wrong
        #{1,2,3} : "hi"       #set is mutable so it is wrong
       }

print("keys immutable :",dict1)

#keys must be unique
x=10
x=20

dict1={10: 100,
       20: 100,
       }
print("keys must be unique :",dict1)

#Dictionary is mutable
#CREATE
data={1: 'swe', 2: 'navya', 3: 'teja', 'id': '26'}

#RETRIEVE
print("Dictionary :", data, type(data))
print("Dict item :", data[3])
print("Dict item :", data['id'])

#UPDATE
data[2] = 'aaria'
data['id'] = 100
print("Dictionary update:", data)

#DELETE
del data[1]
del data['id']
print("Dictionary delete:", data)

data.clear()
print("Dictionary delete:", data)



