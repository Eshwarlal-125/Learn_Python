# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = "'''\nDear <|name|>,\nYou are selected!\n<|Date|>\n'''"
print("================================")
name = input("Enter your name: ")
date = input("Enter the date: ")

letter = letter.replace("<|name|>", name)
letter = letter.replace("<|Date|>", date)

print(letter)