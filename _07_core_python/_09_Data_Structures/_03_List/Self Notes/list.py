'''
#Builtin functions:
-------------------------
append insert extend  : UPDATE
pop remove            : DELETE
count                 : RETRIEVE
index                 : RETRIEVE
reverse               : UPDATE
sort                  : UPDATE
copy                  : CREATE

'''
print("--------------List Functions-------------")
print("------Append------")
list=[1,2,3,4,5]
print("Before :",list)
list.append("swetha")
list.append(True)
list.append({5:3})
print("after :",list)

print("-------Extend------")
list=[1,2,3,4,5]
print("Before :",list)
list.extend(('hello'))
print("after :",list)

print("---------Insert--------")
list=[1,4,5,6,7]
print("before :",list)
list.insert(1,1+1)
print("after :",list)

print("----------pop---------")
list=["swe","tej","aaria"]
print("before :",list)
list.pop(1)
print("after :",list)
list.pop()
print("without any index :",list)

print("----------Remove-------")
list=["hello","hi","bye"]
print("before :",list)
list.remove("hi")
print("after :",list)

print("----------Insert[index,object]----------")
list=[11,22,33,44,55]
print("before :",list)
list[2]=100
print("after :",list)
list.insert(1,111)
print("after insert :",list)

print("---------count----------")
list=[11,22,33,44,55,66,77,88,99]
print("before :",list)
a=list.count(55)
print("after :",a)

print("-------index------")
list=[11,12,13,14,15]
print("before :",list)
a=list.index(13)
print("after :",a)

print("-------Reverse------")
list=[1,2,3,4,5,6]
print("before :",list)
list.reverse()
print("after :",list)

print("------sort-------")
list=[56,78,74,89,32]
print("before :",list)
list.sort()
print("after :",list)

print("-------copy--------")
list=[1,2,3,4,5,6]
print("before :",list)
a=list.copy()
print("after :",a)


