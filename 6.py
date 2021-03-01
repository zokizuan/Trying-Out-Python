"""Write a program in Python to print all the Armstrong numbers within a given range. Take the
upper limit and lower limit as input, using functions."""

print("Armstrong from a given range:")
print("Enter the lower range (more than 9):")
lower = int(input())

print("Enter the upper range:")
upper = int(input())

for num in range(lower, upper + 1):

    order = len(str(num))

    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)
