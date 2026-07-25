'''
A list contains the multiplication table of 7. Write a program to convert it to vertical string
of same numbers.
'''
l = [str(7*i) for i in range(1,11)]

final = "\n".join(l)

print(final)
