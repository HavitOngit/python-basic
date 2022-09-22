# tuple is odred, unchangeble, allow duplictes
from typing import Tuple, Any

mytuple = ("apple", "banana", "cocoa", "milkseck")

# tuple is Unchangable but you change
# convert tuple into list then change and convert into tuple

y = list(mytuple)
y[3] = "cake"
mytuple = tuple(y)
print(mytuple)

# make it list and you apply all list methods

# you can add tuple in tuple
tuple2 = (1, 2, 5, 8)

newtup = mytuple + tuple2

print(newtup)

# use count for count how many time item in tuple
print(newtup.count("apple"))

# Unpack tuple
(num1, num2, num3, num4) = tuple2

print(num1)
print(num2)
# note () = tuple the oder of asine

# if you don't know how many values in tuple add * in arg

(a, *b) = tuple2

print(b)