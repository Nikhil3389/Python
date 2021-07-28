class employee:
    no_of_leaves = 8
    pass

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} And role is {self.role}"

    @classmethod
    def from__str(cls, param):
        pass


nikhil = employee("nikki", 255, "student")
rohit = employee("rohit", 255, "student")
#print(nikhil.salary)
@classmethod
def change_leaves(cls , newsleaves ):
    cls.no_of_leaves = newsleaves
    rohit.change_leaves(34)
print(nikhil.no_of_leaves)
@classmethod
def from__str(cls, string):
    return cls(string.split("-"))
rohit = employee.from__str("rohan-2334-Student")
print(rohit.no_of_leaves)
