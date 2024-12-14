class Calculation:
    def add(self, a=0, b=0, c=0):
        print(a + b + c)


obj1 = Calculation()
obj1.add()
obj1.add(10, 20)
obj1.add(100, 200, 300)
