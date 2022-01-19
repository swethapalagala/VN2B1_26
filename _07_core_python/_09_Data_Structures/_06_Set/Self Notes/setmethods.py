x = {"java","python","devops"}
y = {"manual","automation"}
z = {"database"}

print("-----add method-----")
y.add("testing")                  #it will add an element to the set
print(y)

print("---------update method-------")
x.update(z)                         # updates the set with the union of this set and others
print(x)

print("--------discard method-----")
x.discard("devops")                #it removes the specified element ,if the item to remove does not eist,it will not give error
print(x)

print("-------remove method------")
y.remove("manual")             #removes the specified element,if the item to remove does not exist ,it will raise an error
print(y)

print("-------pop method-------")
y.pop()                     #removes an element from the set.
print(y)

a = {"white","blue","green","yellow"}
b = {"red","black","green","orange"}
print("set1 is :",a)
print("--------intersection method---------")
print(a.intersection(b))              #returns a set which is same in of two sets

print("---------symmetric_difference method---------")
print(a.symmetric_difference(b))        #returns a set with the symmetric difference of two sets

print("----------union method-------")
print(a.union(b))                     #return a set containing the union of sets

print("----------difference_update method--------")
c = {"white","blue","green","yellow"}    #removes the items in this set that are also included in another,specified set.
c.difference_update(b)          #b-c
print(c)

print("-------------interaction_update method---------")
d = {"white","blue","green","yellow"}
d.intersection_update(b)    #removes the items in this set that are not present in other,specified sets.
print(d)

print("-----------symmetric_difference_update method----------")
d.symmetric_difference_update(b)
print(d)                   #inserts the symmetric differences from this set and another.

print("--------issubset method------")
e = {10,20,30}
f = {40,50,60,70,10,20,30}
print(e.issubset(f))        #returns whether another set contains this set or not.
print(f.issubset(e))

print("---------issuperset method-------")
print(e.issuperset(f))      #returns whether this set contains another set or not.
print(f.issuperset(e))

print("------isdisjoint method-------")
print(e.isdisjoint(f))
print(f.isdisjoint(e))      #returns whether two sets have an intersection or not
print(a.isdisjoint(e))

print("-----copy method-----")
set = e.copy()                  #returns the copy of the set
print(set)

print("--------clear method-----")
set.clear()                #removes all the elements from the set
print(set)

print("-------difference method-----")
p = {1,2,3}
q = {4,5,1}

r = p.difference(q)
print(r)





