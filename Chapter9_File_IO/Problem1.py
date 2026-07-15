# Write a program to read the text from a given file ‘poems.txt’ and find out whether it
# contains the word ‘twinkle’.
f = open("poems.txt", "r")
content = f.read()
print(content)
if "twinkle" in content or "Twinkle" in content:
    print("Yes Twinkle found")
else:
    print("No Twinkle is not found")    

f.close()