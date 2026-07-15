# Write a program to wipe out the content of a file using python
f = open("copy.txt","r")
data = f.read()
f.close()
data = ""
f = open("copy.txt","w")
f.write(data)
f.close()


# this is a simpler way to wipe up the file 
'''
f = open("copy.txt", "w")
f.close()
'''