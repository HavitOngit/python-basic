# list is collection wich is ocad. wrinte in [data]

mylist = ["apple", "banana", "coco"]

# add in list

mylist.insert(2, "cherry")

print(mylist)

#append meyhod will add items at end of list
mylist.append("watermelon")
print(mylist)

# removing items

mylist.pop(0) #remove first item

mylist.pop() #this will remove last items


mylist.remove("banana") #remove specified item

# copy list
# in copy method in change happen in original list this will not efffect on copied list
thislist = mylist.copy()

print(mylist)

# for empty list use clear method
mylist.clear()
print(mylist)
print(thislist)

# delte entire list use [del listname]
#like this: del my list