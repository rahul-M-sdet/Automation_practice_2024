d = {'Rahul': 10, 'rajiv': 9, 'Naveen': 4}

mykeys = list(d.keys())
mykeys.sort()

sd = {i: d[i] for i in mykeys}
print(sd)
