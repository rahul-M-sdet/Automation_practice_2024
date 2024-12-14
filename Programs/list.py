list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# first approach to combine two list by using concatenate operator

list3 = list1 + list2
print(list3)

####################
# second approach by using looping concept

for i in list2:
    list1.append(i)
print(list1)

########################
# third approach by using extend function

l1 = ['a','b','c']
l2 = [1,2,3]

l1.extend(l2)
print(l1)
