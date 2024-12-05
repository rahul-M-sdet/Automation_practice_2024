s1 = 'welcome to programming'

print(s1[1:-1])
print(s1[1:-2])

###################
# get the ASCII number of char

print(ord('A'))  # 65
print(chr(65))  # A
l = s1.split()
print(len(s1.split()))

# in and not in

s = 'welcome'
print('scome' in s)
print('scome' not in s)

str = 'welcome to python'
s2 = '220'

print(str.isalnum())
print(s2.isdigit())
print(str.format())
print(str.capitalize())
print(str.replace('come', 'mome'))
print(str.endswith('thon'))
print(str.casefold())
print(s.find('come'))  # return the position of start index of particular string
print(str.find('become'))  # return the -1 if the string does not match with orignal string
print(str.count('t'))
print(str.count('o'))  # return how many times that particular subtring is occured

# string conversion method

s3 = 'welcome to programming'
print(s3.capitalize())      # capitalize the first starting char in string
print(s3.islower())     # check if all the char in lower case
print(s3.isupper())     # check if all the char are in uppercase
print(s3.title())       # capitalize every starting char in string
print(s3.lower())
print(s3.upper())
print(s3.swapcase())