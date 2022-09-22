import shelve

# this method save file secrectly
# use key:value like i mean it store data in dict method


secfile = shelve.open('secretdata')
dog = ['dog', 'dog2', 'dog3']
secfile['dog'] = dog
secfile.close()

# Unpack secrets
unsecfile = shelve.open('secretdata')
x = list(unsecfile.values())
print(x)
