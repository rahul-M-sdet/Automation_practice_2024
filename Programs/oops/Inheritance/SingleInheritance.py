class A:
    def m1(self):
        print("I m from m1 method of class A")


class B(A):
    def m2(self):
        print("I m from m2 method of class B")


b = B()
b.m1()
b.m2()
