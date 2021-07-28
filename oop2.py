class employee:
    no_of_leaves = 8
    pass
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} "
nikhil = employee()
rohit = employee()
nikhil.name= "Nikhil"
nikhil.salary = 245

rohit.name= "Rohit"
rohit.salary = 345
print(rohit.printdetails())