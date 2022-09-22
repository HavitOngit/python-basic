age = 18

txt = "I am {} years old."

print(txt.format(age))

# if you add direct arg in str this will give you error
# so use format method
name = "Harsh"
village = "somewere"

txt2 = "hello i am {0}.from beutiful village {1}."

# you also specify number so data place into correct location
print(txt2.format(name, village))

# if you change txt.format(village, name)
#result will be like:
# hello i am somewere.from beutiful village Harsh.

#note: we use {} in string and then pass arg