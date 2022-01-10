e_data = {'eid' : 26,
          'name': 'swetha reddy',
          'sal': 6000,
          'mobile': '9550253224',
           'place': 'Bangalore'
         }
print("Dictionary data:", e_data)


print("-------get function------")
print("the value of given key in dict is:",e_data.get('name'))
print("the value of given key in dict is:",e_data.get('eid')) #returns the value of the item with specified keys and values.

print("-----------keys function---------")
print("keys in given dict:",e_data.keys()) #returns a list containing the dict keys

print("---------values function--------")
print("values in given dict:",e_data.values()) #returns a list of all the values in the dict.

print("----------Fromkeys----------")
x=e_data.fromkeys([1,2,3,4],'Hi') #returns a dict with specified keys and values.
print(x)

print("-------pop function-------")
print("Before deleting key dict is:",e_data.pop('eid')) #removes the element with the specified key
print("After deleting key dict :",e_data)

print("-------items function------")
print("Total keys and values in dict:",e_data.items()) #returbns a list containing a tuple for each keyvalue.

print("---------popitem function--------")
print("before using popitem function:",e_data.popitem()) #removes the last inserted key values.
print("After using popitem function:",e_data)

print("---------copy function------")
print("copy of dictionary:",e_data.copy())   #returns the copy of the dict.

print("-------update function-------")
print("before updating dict:",e_data)    #it updates the dict with specified key values.
e_data.update({'Age':26})
print("After updating dict:",e_data)

print("-------clear function--------")
print("before clear function:",e_data)
e_data.clear()
print("after clear function:",e_data) #it removes all the elements from the dict.


print("-----Has key function-------")
print("values in the dict:",e_data.has_key('sal'))








