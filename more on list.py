# make list by scaning list with conditions

fruits = ["apple", "banana", "watermelone", "cherry"]

newlist = []  # just leave empty list and append it

for i in fruits:
    if "a" in i:
        newlist.append(i)

print(newlist)

# you also short this

smlist = [x for x in fruits if "r" in x]
print(smlist)


# sort kist

def myfunc(n):
    return int(n / 2)


listf = [1, 5, 3, 7, 3, 9, 333, 45]

listf.sort(key=myfunc)  # note here we use myfunc not my func()
print(listf)

# add two list


list2 = fruits + listf  # sum two list
print(list2)

fruits.append(listf) # append method
print("append", fruits)

fruits.extend(list2)  # exttend method
print("extend", fruits)

# protip

import collections
# this way you create default value for dict
mdict = collections.defaultdict(int) # float, list can be usable
print(mdict['hi'])
