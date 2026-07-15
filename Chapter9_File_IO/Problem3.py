# Write a program to generate multiplication tables from 2 to 20 and write it to the different
# files. Place these files in a folder for a 13-year-old.
for i in range(2, 21):
    f = open(f"13-year-old/table_of_{i}.txt", "w")
    f.write("Multiplication Table of " + str(i) + "\n")
    f.write("=============================\n")
    for j in range(1, 11):
        f.write("       " + str(i) + " x " + str(j) + " = " + str(i*j) + "\n")
    f.write("=============================\n")
    f.close()