#Data structures;
#there are four built-in data structures in python-list
                                                  #  tuple
                                                  # dictionary
                                                  # set
 #Each of the data structures are "containers" that organize and group data according to type.
 #the data structures differ based on mutability and order.

 #Slicing;slicing in python means taking elements from one given index to another given index.
 #python slicing strings;slice from the start,by leaving out the start index,the range will start at the first character;slice to the end by leaving out.
 # slicing means getting a subset of elements from an iterable based on their indices.

#Indexing;it means referring to an element of an iterable by its position within the iterable.

print("---STRING---")
name = 'Swetha Reddy'
print(name)
print("2nd index value :", name[1]) #indexing
print("0th index value :", name[7])
print("Get partial name:", name[0:12]) #slicing

company = "HCL infotech"
print(company)

#List;A list is an ordered data structure with elements separated by a comma and enclosed within square brackets.
#suppose list1 has integers and list2 has strings,then can store mixed data types .

# List
print("------List------")

list1 = [100, 34.33, True, 'Swetha', [1,2,3], (2,3,), {2:20,3:30}, {1,2,3}]
print("List1 : ", list1)
print("Index : ", list1[3]) #indexing
print("Index :", list1[3][2])
print("slice : ", list1[1:6]) # slicing


#Tuple;it is a built-in data structure in python that is an ordered collection of objects.

# Tuple
print("-----Tuple-----")

tuple1 = (100, 34.33, True, 'Swetha', [1,2,3], (2,3,), {2:20,3:30}, {1,2,3})
print("Tuple : ", tuple1)
print("Index : ", tuple[3])
print("Index : ", tuple1[3][2]) #indexing
print("slice :", tuple1[1:6]) # slicing

#Dictionary;it is an unordered and mutable python container that stores mappings of unique keys to values.
#these are written with curly brackets({}),and separated by commas and colon.

#Dictionary
print("------Dictionary------")

s_data = {'sid' : 22,
          'name' : 'swethareddy',
          'fee' : 35000,
          'loc' : 'bangalore'
          }

print("Dict data :", s_data)
print("Dict data :", s_data['name'])
print("Dict data :", s_data['fee'])
print("Dict  data :", s_data['loc'])

#Set;A set is a data structure that can store any number of unique values in any order.
#these are different from arrays in the sense that they only allow non-repeated,unique values within them.we can create a set wwith in set function.

#Set
print("-----Set-----")

set1 = {1,2,3,4,5,6}
print("Set1 :", set1)














