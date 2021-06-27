 list1=[" this", 2.3, 1, 1, 1, True]

print(list1)

#put square brackets to name out justone thing from the list
list2=["clock","fan","chair","table'"]

print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])

#this is the ineficeint way
list3=["keyboard","mouse","phone","ipad","microphone","charger","wire",]

print(list3[1])

import random

die_roll_7 = random.randint(0,7)

print("the 7-sided die rolled a", die_roll_7 )

#random list genrater[]
import random

list3=["keyboard","mouse","microphone"]

print(list3[random.randint(0,2)])

list1=["the", "quick", "brown", "fox"]
list1[1] = "slow"

print(list1)
    
list1 = [1, 2, 3, 5, 5, 3]
list1[3] -=1
list1[2] *=4
print(list1)

#The append() method in python adds a single item to the existing list. 
list1.append(2)
#insert() is an inbuilt function in Python that inserts a given element at a given index in a list.
list1.insert(2,4)
print(list1)

#Python List Extend() ... extend() is a built-in function that adds the specified list elements (or any iterable) to the end of the current list. 
list1.extend([1, 3, 5, 2, 7, 6])
print(list1)

#Python List remove() The remove() method removes the first matching element (which is passed as an argument) from the list.
list1.remove(1)
print(list1)

#pop() is an inbuilt function in Python that removes and returns last value from the list or the given index value. ... index (optional)-
#- The value at index is popped out and removed.If the index is not given, then the last element is popped out and removed.
list1.pop()
print(list1)

#tuple1 = ("hi",)

print(tuple1)

#Like a random number genrater. 
print(list(range(3, 9, 2[])))
