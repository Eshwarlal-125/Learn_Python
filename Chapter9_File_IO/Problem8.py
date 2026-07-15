# Write a program to make a copy of a text file “this.txt”
f = open("this.txt","r")
data = f.read()
f.close()

f = open("copy.txt","w")
f.write(data)
f.close()