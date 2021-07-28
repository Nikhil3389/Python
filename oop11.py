f1 = open("nikhil.txt")
try:
    f = open("docs.txt")
except EOFError as e:
    print("print eof error encountered")
except IOError as e:
    print("print io error encountered")
else:
    print("this will be running only if the except block is not working ")
finally:
    print("Run this any way.......")
    f1.close()
print("Important ")