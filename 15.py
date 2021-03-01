"""Write a Program in Python to take a set of Integers as Input in a list and display the number of
occurrences of each unique integer"""

lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    print("%s->" % (i + 1))
    ele = int(input())

    lst.append(ele)

print(lst)

ul = set(lst)
result = sorted([(x, lst.count(x)) for x in ul], key=lambda y: y[1])
for elem in result:
    print('{} occurred {} times'.format(elem[0], elem[1]))
