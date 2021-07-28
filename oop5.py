class parent():
    def first(self):
        print("parents")
class child(parent):
    def second(self):
        print("child")
object1=child()
object1.first()
object1.second()