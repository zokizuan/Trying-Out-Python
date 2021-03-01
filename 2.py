""" Write a program in Python to print the sum of the following series:
S = 1 + 4 + 9 + ⋯ + n^2 """

print("Enter the range of number(Limit):")
n=int(input())
#sum
S=0
i=1
print("The range of number is:")

while(i<=n):
    print(i*i,end=" ")
    S=S+i*i
    i+=1


print("\n")
print("The Sum of the range is:")
print(S,)