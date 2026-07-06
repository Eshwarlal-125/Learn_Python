# Can we have a set with 18 (int) and '18' (str) as a value in it?

s = set()
s.add(18)
s.add('18')

print(s)


# Yes, we can have a set that contains both the integer 18 and 
# the string '18' as values. In Python, sets can hold elements 
# of different data types, and since 18 (int) and '18' (str) are 
# considered different types, they can coexist in the same set.