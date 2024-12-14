# req: Emp
# create constructor pass the arguments eid,ename,sal
# create display method and print the value

# class Emp:
#     def __init__(self, eid, ename, Sal):
#         self.eid = eid
#         self.ename = ename
#         self.Sal = Sal
#
#     def display(self):
#         print(self.eid, self.ename, self.Sal)
#
#
# e1 = Emp(101, 'Rahul', 2000)
# e1.display()


class Emp:
    def __init__(self, eid, ename, Sal):
        self.eid = eid
        self.ename = ename
        self.Sal = Sal

    def __str__(self):  # string constructor will return string datatype only not other value
        return self.ename


e1 = Emp(102, 'John', 20000)
print(e1)
