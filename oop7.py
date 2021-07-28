class level:
    def first(self):
        print("code")
class level1(level):
    def first2(self):
        print("code2")
class level2(level1):
    def first3(self):
        print("code3")
object= level2()
object.first()
object.first2()
object.first3()