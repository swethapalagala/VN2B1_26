#Tuple:
#it is a collection of python objects separated by commas. (, ,)
#In someways a tuple is similar to list in terms of indexing,nested objects and repetition.
#it is a immutable unlike lists which are mutable.
#Diff b/w LIST and TUPLE  in python:
'''
        LIST                              TUPLE
->List is mutable.                    ->Tuple is immutable.
->List iteration is slower and        ->Tuple iteration is faster.
  is time consuming.
->List is useful for insertion and     ->Tuple is useful for readonly operations like
  deletion operations.                    accessing elements.
->it consumes more memory.              ->it consumes less memory.
->it provides many built-in methods.    ->it have less built-in methods.
->List operations occur more errors.    ->tuple doesnot take place,these are safe.

'''

#List1= [10,20,30,40]  -> this is mutable.
#Tup1=(10,20,30,40)    -> this is immutable.

Tup1 = (10,20,30,40)
print("sum of Tup1 :", sum(Tup1))






