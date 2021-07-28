class employee:
    no_of_leaves = 8
    pass

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} And role is {self.role}"


nikhil = employee("nikki", 255, "student")
print(nikhil.salary)
