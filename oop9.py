# Diamond shape  problem
class A:
    def met(self):
        print("This is a method from A")
class B(A):
    def met(self):
        print("this is a method from B")
class C(A):
    def met(self):
        print("This is a method from C")
class D(C,B):
    def met(self):
        print("This is a D")
a = A()
b = B()
c = C()
d = D()
c.met()