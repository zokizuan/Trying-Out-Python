# Write a Program in Python to take 2 numbers as input and swap them without using a third variable.
x = int(input("Enter the value of x?"))
y = int(input("Enter the value of y?"))
print("before swapping numbers: %d | %d\n" % (x, y))
# swapping#
x = x + y
y = x - y
x = x - y
print("After swapping: %d | %d\n" % (x, y))
