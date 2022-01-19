'''

The collection Module in Python provides different types of containers.
 A Container is an object that is used to store different objects and provide
 a way to access the contained objects and iterate over them.
Some of the built-in containers are Tuple, List, Dictionary,
 the different containers provided by the collections module.

Counters
OrderedDict
DefaultDict
ChainMap
NamedTuple
DeQue
UserDict
UserList
UserString

'''

d = { }
d["swe"]    = 1
d["teja"]   = 2
d["aaria"]  = 3
for key,value in d.items():
    print(key,value)

od = orderedDict()
od["swe"]    = 1
od["teja"]   = 2
od["aaria"]  = 3
for key,value in od.items():
    print(key,value)
