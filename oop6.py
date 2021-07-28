class Base1:
    def func1(self):
        print("this is base 1 class")
class Base2:
    def func2(self):
        print("this is base 2 class")
class child(Base1, Base2):
    def func3(self):
        print("this is base 3 class")
obj = child()
obj.func1()
obj.func2()
obj.func3()
