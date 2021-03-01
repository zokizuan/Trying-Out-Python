# Write a Program in Python to take a list as Input and reverse it within itself.

def reverseList(a):
    end = len(a) - 1
    start = 0
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1


lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    print("%s->" % (i+1))
    ele = int(input())

    lst.append(ele)  # adding the element

print(lst)

reverseList(lst)

print(lst)
