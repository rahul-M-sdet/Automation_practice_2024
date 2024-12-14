mytuple = (1, 2, 3, 'a', 'b', 'c')

# we cannot modify the value in tuple
# first we have to convert into list and then again change to tuple

mylist = list(mytuple)
mylist.append('d')
print(mylist)
mytuple = tuple(mylist)
print(mytuple)

####################
# try to change items in tupple

# mytuple[0] = '4'
# print(mytuple)

tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

result = dict(zip(tuple1, tuple2))
print(result)

s1 = 'jan,feb,mar'
s2= 'January|February|March'
keys = s1.split(',')
values = s2.split('|')
d2=dict(zip(keys,values))
print(d2)
