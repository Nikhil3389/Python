
# excercise of multipe level inheritance
# electronic
# pockets
# smartphone
class electronic:
    motherboard= 66
    circult = 5
class pockets(electronic):
    GPS =1
    circult = 3
    time = "Yes"
class smartphone(pockets):
    circult = 10
    gpu=9
    cpu = 1
obj = electronic()
obj1 = pockets()
obj3 = smartphone()
print(obj3.motherboard)