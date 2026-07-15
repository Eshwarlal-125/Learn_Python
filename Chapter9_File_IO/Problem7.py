# Write a program to find out the line number where python is present from ques 6.

f = open("Problem6_file.txt","r")
line = f.readline()
i = 1
found = False
while line != "":
    if "python" in line or "Python" in line:
        print("Found python in line: ", i)
        found = True
    line = f.readline()
    i+=1

if found == False:
    print("The word python is not found")
f.close()