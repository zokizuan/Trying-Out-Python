"""Write a program in Python to take a string as input and count the number of:
a. Vowels;
b. Consonants;
c. Digits;
d. Special Characters present in the String"""


def countCharacterType(str):
    vowels = 0
    consonant = 0
    specialChar = 0
    digit = 0

    for i in range(0, len(str)):

        ch = str[i]

        if (('a' <= ch <= 'z') or
                ('a' <= ch <= 'Z')):

            ch = ch.lower()

            if (ch == 'a' or ch == 'e' or ch == 'i'
                    or ch == 'o' or ch == 'u'):
                vowels += 1
            else:
                consonant += 1

        elif '0' <= ch <= '9':
            digit += 1
        else:
            specialChar += 1

    print("Vowels:", vowels)
    print("Consonant:", consonant)
    print("Digit:", digit)
    print("Special Character:", specialChar)


str = input("Enter the string:")
countCharacterType(str)
