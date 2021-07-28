class A:
    classvar1 = "I am a class in class A"
    def __init__(self):
        self.var1="I am inside class A"
        self.classvar1="Instance "
        self.special = "special"
class B(A):
    classvar1 = "I am Class B"
    def __init__(self):
        self.var1 =" I am inside class B "
        self.classvar1 = "instance of class b"
        super(B, self).__init__()
        print(super().classvar1)
a=A()
b = B()
print(b.special,b.var1,b.classvar1)