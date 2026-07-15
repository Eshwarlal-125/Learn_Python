# Write a program to mine a log file and find out whether it contains ‘python’
f = open("Problem6_file.txt","r")
data = f.read()
f.close()

if "python" in data or "Python" in data:
    print("Found the word python")
else:
    print("Not Found the word python")