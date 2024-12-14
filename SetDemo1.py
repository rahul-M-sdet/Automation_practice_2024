# Example 1 creating a set

myset = {'banana','mango','cherry'}
print(myset)

# Example 2 reading the data from set using loop

for i in myset:
    print(i)

# Example 3 check item is present in the set

if 'xyx' in myset:
    print("Yes it is present")
else:
    print("Not present")

# adding items in the set
# we have two method to add the items add()-add single element and update()- add multiple items in the set

set1={'a','b','c'}
new_set=set1.add('d')
print(set1)

# update - add multiple element in the set

set1.update('e','f','g')
print(set1)

# Example4 find the number of items in the set
print(len(set1))

# Example5 delete the items from the list remove() , discard(), del

set1={'a', 'd', 'c', 'e', 'f', 'b', 'g'}

set1.remove('b')
print(set1)

# set1.remove('axd')
# print(set1)

set1.discard('d')
print(set1)

set1.discard('xyz')
print(set1)

# if the item is not there in set and will try to remove the item it will show keyerror but discard function will not show any error
# if the items is not there

set1.clear()
print(set1)

del set1
#print(set1)


# Example 6 join the two set value

myset1 = {'a','b','c'}
myset2 = {1,2,3}
myset3 = myset1.union(myset2)
print(myset3)

myset1.update(myset2)
print(myset1)
