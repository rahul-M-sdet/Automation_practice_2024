s1 = 'jan,feb,mar'
s2 = 'January|February|March'

keys = s1.split(',')
value = s2.split('|')

dict = {}

for i in range(len(keys)):
    dict[keys[i]] = value[i]
print(dict)
