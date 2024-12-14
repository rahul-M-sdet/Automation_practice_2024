dic1 = {100:'x',200:'y',300:'z'}
print(dic1)

# Example 1 read the value from dict

# print(dic1[100])
# by using get method

print(dic1.get(100))

print(dic1.get(300))

# change value in dict

dic1[100]=400
print(dic1)

# reading complete dictionary ie keys and values

for i,j in dic1.items():
    print(i,j)

# check if the keys is present in the dictionary

if 200 in dic1:
    print('Exist')
else:
    print('Non exist')

# find number of items in the dictionary

print(len(dic1))  # using len function

# add items into the dict

dic1['500'] = 'a'
print(dic1)

# remove items from dict

dic1.pop(300)
print(dic1)

# another way to remove the items from dict

del dic1[200]
print(dic1)

# del dic1
# print(dic1)

# if the variable is not present will get nameerror

# delete the items but not complete dict

dic1.clear()
print(dic1)

# copy one dict into another
dic2={100:'x',200:'y',300:'z'}

dic1 = dic2
print(dic2)