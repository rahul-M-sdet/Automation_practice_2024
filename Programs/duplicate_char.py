input_string=input("Enter the string: ")

print("duplicate char in the string is: ")
for char in set(input_string):
    count = input_string.count(char)
    if count > 1:
        print(f"{char}:{count}")
