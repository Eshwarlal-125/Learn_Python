# Write a program to find whether a given username contains less 
# than 10 characters or not.

username = str(input("Enter your username: "))

length = len(username)
if(length < 10):
    print("Yes! this username contains less than 10 characters.")
else:
    print("No! this username does not contains less than 10 characters.")

