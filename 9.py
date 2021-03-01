# Write a program in Python to calculate the HCF and LCM of 2 numbers, using functions


def my_function(no, nt):
    a = no
    b = nt
    while b != 0:
        temp = b
        b = a % b
        a = temp

    hcf = a
    lcm = int((no * nt) / hcf)

    print("\nLCM (" + str(no) + ", " + str(nt) + ") = ", lcm)
    print("HCF (" + str(no) + ", " + str(nt) + ") = ", hcf)


print("Calculating HCF and LCM")
print("Enter First Numbers: ", end="")
first_number = int(input())
print("Enter Second Numbers: ", end="")
second_number = int(input())
my_function(first_number, second_number)
