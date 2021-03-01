""""Write a program in Python to find out the digital root of a number, using functions. The digital
root of a number is the sum of digits taken continuously till the sum is lesser than 10"""


def digitalRoot(num):
    # If num is 0.
    if (num == "0"):
        return 0

    ans = 0
    for i in range(0, len(num)):
        ans = (ans + int(num[i])) % 9

    if (ans == 0):
        return 9
    else:
        return ans % 9


print("Calculating Digital Root")

num = input("Enter the number:")

print("The Digital Root of the number is: %d" % digitalRoot(num))
