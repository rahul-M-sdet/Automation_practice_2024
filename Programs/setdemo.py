# set is unordered and unindexed , set is represented by curly braces

myset = {'banana','apple','cherry'}

# Read the data from set, there is only one method available

for i in myset:
    print(i)

# check wheather element is present in the set

# if 'banana' in myset:
if 'banana1' in myset:
    print("it is present")
else:
    print("Not present")

# add items in the set
# we have two method add() and update()
# add() - if we want to add single element
# if we want to add multiple element use update()

myset = {'banana','orange','apple'}
myset.add('cherry')
print(myset)

myset1 = {'a','b','c'}

myset1.update(['mango','grapes','carrot'])
print(myset1)

# find how many items in the set

print(len(myset))

# we want to delete the item from set
# we have two method remove() and discard()

myset = {'banana','orange','apple'}
myset.remove('banana')
print(myset)
myset.remove('xyz')  # it will show key error if item is not present and try to delete


myset.discard('banana')
print(myset)
myset.discard('xyz') # it will not throw any error

# delete the ser

myset = {'banana','orange','apple'}








