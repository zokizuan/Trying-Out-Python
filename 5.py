# Write a program in Python to print all the Palindrome numbers within a given range. Take the
# upper limit and lower limit as input, using functions.

# Palindrome Function
def is_palindrome(n: int) -> bool:
    # reverse
    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10

    return n == rev


def count_pal(lower_range: int, higher_range: int) -> None:
    for i in range(lower_range, higher_range + 1):
        if is_palindrome(i):
            print(i, end=" ")


print("Palindrome from a given range:")
print("Enter the lower range (more than 9):")
first_number = int(input())

print("Enter the upper range:")
second_number = int(input())

count_pal(first_number, second_number)
