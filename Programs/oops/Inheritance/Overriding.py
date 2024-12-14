# class A:
#
#     def m1(self):
#         print("I m from m1 method of class A")
#
#
# class B(A):
#
#     def m1(self):
#         super().m1()
#         print("I m from m1 method of class B")
#
#
# obj1 = B()
# obj1.m1()

# like method we can override variables also

class A:
    name='John'

class B(A):
    name='Rahul'

obj1=B()
print(obj1.name)
