# Write a program to find out whether a file is identical and matches the content of another file.
f = open("this.txt","r")
data1 = f.read()
f.close()

f = open("copy.txt","r")
data2 = f.read()
f.close()


if data1 == data2:
    print("Both files are same!")
else:
    print("Both files are different!")