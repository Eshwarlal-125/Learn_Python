# Can you change the values inside a list which is contained 
# in set S? s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}

s.update({[3,4]})

print(s)

# NO. it will give an error because set elements must be immutable,
# and lists are mutable. 