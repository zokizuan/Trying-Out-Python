""" Write a program in Python to accept a String as Input and check whether it is a Palindrome or
not."""
def isPalindrome(s):
    rev = ''.join(reversed(s))

    if s == rev:
        return True
    return False


str = input("Enter the string:")
ans = isPalindrome(str)

if ans==True:
    print("Yes, the string is palindrome")
else:
    print("No, the string is not palindrome")
