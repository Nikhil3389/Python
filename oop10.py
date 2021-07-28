def getNum(n):
    for i in range (n):
        yield i
seq = getNum(4)
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())



