# If the names of 2 friends are same; 
# what will happen to the program in problem 6?
s = {}
name = input("Enter friend name: ")
lang = input("Enter language name: ")
s.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")
s.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")
s.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")
s.update({name: lang})

print(s)

# If the names of 2 friends are the same, 
# the second entry will overwrite the first one.