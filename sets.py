# sets are Unordered Unchangeable Duplicates not allowed

myset = {"apple", "banana", "cherry", "orange"}

# you can't change item but you add new items

myset.add("Orange")  # add method

# add entire sets by using update method

data = ["kivi", "orange"]

myset.update(data)

print(myset)

# removing items by using discard method

myset.discard("kivi")
# Note you also use remove method but if item not exist this will reise error
# pop method also work but because of set are unordered we don't know which item should remove

# join sets
# unions metod or update both work
newset = myset.union(data)
print(newset)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# keep only duplicates

set1.intersection_update(set2)
print(set1)
# if you revove the _update then this method will return new set

# keep all but not duplicates
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

z = set1.symmetric_difference(set2)
print(z)
# note: we are not used update so we store new set in z var

