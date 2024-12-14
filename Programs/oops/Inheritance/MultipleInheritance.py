class A:
    a, b = 50, 100

    def m1(self):
        print(self.a + self.b)


class B:
    c, d = 20, 10

    def m2(self):
        print(self.c - self.d)


class C(A, B):
    i, j = 2, 3

    def m3(self):
        print(self.i * self.j)


obj3 = C()
obj3.m1()
obj3.m2()
obj3.m3()
