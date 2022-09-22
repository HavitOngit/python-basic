# lambda arg: expression
# lambda is like def func but annoymos one liners

x = lambda a, b: a * b
print(x(2, 3))

# You pass unlimited arg and take input for there

# Some ! exps

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2) # this will make n = 2 in myfunc
mytrippler = myfunc(3) # this will make n = 3 in myfunc

print(mydoubler(5)) # set a = 5
print(mytrippler(3)) # set a = 3
