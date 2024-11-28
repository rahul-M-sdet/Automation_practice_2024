l1 = [1, 2, 3, 'a', 'b', 'c']

int_lst = []
char_lst = []

for element in l1:
    if isinstance(element, int):
        int_lst.append(element)
    else:
        char_lst.append(element)

print(int_lst)
print(char_lst)
