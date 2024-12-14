class A:
    a, b = 50, 100

    def m1(self):
        print(self.a + self.b)


class B(A):
    c, d = 20, 10

    def m2(self):
        print(self.c - self.d)


class C(B):
    i, j = 2, 3

    def m3(self):
        print(self.i * self.j)


obj1 = C()
obj1.m1()
obj1.m2()
obj1.m3()
