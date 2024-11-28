def search(l1, x):
    if x in l1:
        return f"{x} is present in the list"
    else:
        return f"{x} is not present in the list"


l1 = [1, 2, 3, 4, 5, 6]

result = search(l1, 2)
print(result)
