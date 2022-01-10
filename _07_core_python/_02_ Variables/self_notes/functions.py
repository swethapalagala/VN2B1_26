#functions
list1=[1,2,3,4]
print("before :",list1)
t1=tuple(list1)
print("After :",t1)

t2=(10,20,30,40,444)
print("iterate the tuple")
for each in t2:
    print(each)

len = len(t2) #5 elements
for i in range(len): #range(4)
    print(i,":",t2[i])



list1=["swe","tej","chinnu"]
print("Before :", list1)
list1.append("nikku")
print("After :", list1)
#return type

#pop()
#remove()

print("list pop :", list1.pop(1)) #index position
print(list1)
print("list remove :", list1.remove("nikku"))
print(list1)


