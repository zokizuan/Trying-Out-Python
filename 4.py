# Write a program in Python to print the sum of the following series:
# S = 1 - (x/1!) + (x^2/2!)+(x^3/3!+…

import math


def Series(x, n):
    sum = 1
    term = 1
    y = 2

    for i in range(1, n):
        fct = 1
        for j in range(1, y + 1):
            fct = fct * j

        term = term * (-1)
        m = term * math.pow(x, y) / fct
        sum = sum + m
        y += 1

    return sum


# Driver Code
print("Enter the value of x:")
x = int(input())
print("Enter the range of series:")
n = int(input())
print('%.4f ' % Series(x, n))
