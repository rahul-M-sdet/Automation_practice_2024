def remove_even_number(l1):
    return [num for num in l1 if num % 2 != 0]


l1 = [1, 2, 3, 4, 5, 6, 7]
odd_number = remove_even_number(l1)
print("The remaining number in the list is: ", odd_number)
