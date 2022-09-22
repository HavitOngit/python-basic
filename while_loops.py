i = 0
while i < 5:
    print(i)
    if i == 3:
        print("time out !")
        break  # The break method stop while loop
    i += 0.5
else:
    print("loop over !")
# when you use break statement else will not exicude

# Continue method
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue  # Continue statement bypass the loop
    print(x)

else:
    print("continue loop over !")
# else statment active when while's condition become False
