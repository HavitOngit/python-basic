# directories come in key = value pair

# directories are ordered changeable don't allow duplicates

mydict = {
    "name": "Havit",
    "age": 18,
    "current_location": "125.34.77",
}

# accessing items by key name

x = mydict["name"]
print(x)

# using get() method
print(mydict.get("age"))

#
x = mydict.values()
print(x)

# change values
mydict["name"] = "Harsh"
print(x)
# note: we use mydict[] because change happen in dict

# iteam method
a = mydict.items()
print(a)

# adding items
mydict["lang"] = "Gujarati"
print(mydict)
# this key not exist in my dict so new key added automaticaly

# Update method
mydict.update({"hobby": "drawing"})
print(mydict)
# note in this method we used {} brakets

# remove items
# pop() method

mydict.pop("lang")
print(mydict)
# if you use popitem() it will remove last item

# clear method return empty dict
# del method delete dict


# for copy use dictname.copy() method or dict() method

newdict = dict(mydict)
print(newdict)

# you also make dict into dict
ndict = {
    "p1": {
        "name": "harsh",  # note ","
        "age": "18"
    },
    "p2": {
        "name": "harsh",  # note ","
        "age": "18"
    }
}
p1 = {"name": "harsh",  # note ","
      "age": "18"}
p2 = {"name": "harsh",  # note ","
      "age": "18"}
p3 = {"name": "harsh",  # note ","
      "age": "18"}
dicttype2 = {
    "parson1": p1,
    "parson2": p2,
    "parson3": p3
}

print(dicttype2.get("parson1"))