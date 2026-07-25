# Write a program to filter a list of numbers which are divisible by 5.

l = [4,5,9,10,14,15,19,20]
def divisible(n):
    return n%5==0

final = filter(divisible,l)

print(list(final))