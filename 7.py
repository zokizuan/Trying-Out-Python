""" Write a program in Python to print all the Krishnamurthy numbers within a given range. Take the upper limit and lower limit as input, using functions. """
def factorial(n):
    fact = 1
    while n != 0:
        fact = fact * n
        n = n - 1
    return fact


def isKrishnamurthy(n):
    sum = 0
    temp = n
    while temp != 0:
        rem = temp % 10
        sum = sum + factorial(rem)

        temp = temp // 10

    return sum == n


print("krishnamurthy from a given range:")
print("Enter the lower range:")
lower = int(input())

print("Enter the upper range:")
upper = int(input())

for num in range(lower, upper + 1):

    if (isKrishnamurthy(num)):
        print(num)
