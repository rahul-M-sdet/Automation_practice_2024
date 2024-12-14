class A:
    a, b = 50, 100

    def m1(self):
        print(self.a + self.b)


class B(A):
    c, d = 20, 10

    def m2(self):
        print(self.c - self.d)


class C(A):
    i, j = 2, 3

    def m3(self):
        print(self.i * self.j)

obj2=B()
obj2.m1()
obj2.m2()
