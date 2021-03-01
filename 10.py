# Write a program to perform Prime Factorization of a number using functions
import math


def primeFactors(n):
    while n % 2 == 0:
        print(2, end=" "),
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            print(i, end=" ")
            n = n / i

    if n > 2:
        print(n, end=" ")


print("Performing Prime Factorization")

print("Enter the number:")
num = int(input())
primeFactors(num)
