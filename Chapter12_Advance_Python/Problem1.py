#Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not
#present, a message without exiting the program must be printed prompting the same.

'''
files = ["file1.txt","file2.txt","file3.txt"]
for file in files:
    try:
        with open(file,"r") as f:
            print(f"{file} opended Successfully!")
    except FileNotFoundError:
        print(f"{file} is not present. Please create it.")
'''

try:
    f = open("file1.txt","r")
    data = f.read()
    f.close()
    print(f"File 1 is present")
except FileNotFoundError as e:
    print(e)
try:
    f = open("file2.txt","r")
    data = f.read()
    f.close()
    print(f"File 2 is present")
except FileNotFoundError as e:
    print(e)
try:
    f = open("file3.txt","r")
    data = f.read()
    f.close()
    print(f"File 3 is present")
except FileNotFoundError as e:
    print(e)

print("Thankyou!")