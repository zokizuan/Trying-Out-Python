""" Write a program in Python to print the sum of the following series:
S = 1 − 2 + 3 − 4 + 5 − 6 + ⋯ ± n"""

print("Enter the range of series(Limit):")
n=int(input())
# when n is odd 
if n % 2 == 1:
    print("\n")
    print("The Sum of the series is is:")
    print ((n + 1)/2)
# when n is not odd
else: 
    print("\n")
    print("The Sum of the series is is:")  
    print (-n / 2)