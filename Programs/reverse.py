s1 = 'welcome to python'
rev_str = ''
for char in s1:
    rev_str = char + rev_str
print(rev_str)

###############################
# 2. by using slice operator

rev=s1[::-1]
print("The reversed string is: ",rev)
