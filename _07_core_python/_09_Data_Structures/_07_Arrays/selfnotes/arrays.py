'''
ARRAYS:
Arrays are used to store multiple values in one single variable.
An array is a special variable, which can hold more than one value at a time.
An array can hold many values under a single name, and you can access the values by referring to an index number.
Use the len() method to return the length of an array (the number of elements in an array).
You can also use the for in loop to loop through all the elements of an array.
You can use the append() method to add an element to an array.
You can use the pop() method to remove an element from the array.
You can also use the remove() method to remove an element from the array.

'''

print("------Array Methods--------")
print("-----append method----")
x = [10,20,30]                     #it appends the element to the end of the list.
y=[40,70,60]
x.append(y)
print(x)



print("--------copy method---------")
z = x.copy()
print(z)                         #returns a copy of the specified list.

print("-------count method------")
a = x.count("30")                #returns the number of the element with a specified value
print(x)

print("--------extend-------")
m = [7]
x.extend(m)                #it adds the specified list elements to the end of the current list.
print(x)

print("-----index method-----")
a = x.index(20)             #Returns the index of the first element with the specified value
print(a)

print("-------------insert method--------")
a = x.insert(0,22)
print(x)                  #Adds an element at the specified position

print("-------------sort method-----------")
y.sort()                 #Sorts the list
print(y)

print("-----clear method-----")
y.clear()                        #removes all the elements from a list.
print(y)





