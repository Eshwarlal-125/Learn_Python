# Repeat program 4 for a list of such words to be censored.

f = open("Problem5_file.txt", "r")
data = f.read()
f.close()
l = ["donkey", "Donkey", "stupid", "Stupid", "fool", "Fool"]
for i in l:
    data = data.replace(i,"#####")
f = open("Problem5_file.txt", "w")
f.write(data)
f.close()

