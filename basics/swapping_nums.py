"""================== Using temporary Variable =================="""
x = 5
y = 10

print("before swapping x = ",x," & y = ",y)

temp = x
x = y
y = temp

print("After swapping x = ",x," & y = ",y)


"""================== Using Tuples =================="""
a = 20
b = 30

print("before swapping a = ",a," & b = ",b)

(a, b) = (b, a)

print("After swapping a = ",a," & b = ",b)
