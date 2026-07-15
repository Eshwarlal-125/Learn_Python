# A file contains a word “Donkey” multiple times. You need to write a program which
# replaces this word with ##### by updating the same file.

f = open("Problem4_file.txt", "r")
data = f.read()
f.close()

new_data = data.replace("donkey","#####").replace("Donkey","#####")

f = open("Problem4_file.txt", "w")
f.write(new_data)
f.close()

