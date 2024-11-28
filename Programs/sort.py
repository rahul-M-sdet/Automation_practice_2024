# int array5[]={7,3,1,2,9,0,6,4,5}

# Write the program to print Sorting Ascending & Descending order


def lst_sort(l1):
    for i in range(len(l1)):
        for j in range(0, len(l1) - i - 1):
            if l1[j] > l1[j + 1]:
                l1[j], l1[j + 1] = l1[j + 1], l1[j]
    return l1


l1 = [7, 3, 1, 2, 9, 0, 6, 4, 5]
result=lst_sort(l1)
print(result)
print(list(reversed(l1)))
