num = int(input("Enter a Number: "))
table = [num * i for i in range(1,11)]

f = open("Table.txt","w")
f.write(str(table))
f.close()