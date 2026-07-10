# Write a python function to remove a given word from a list and strip it at the same time.

l = ["apple","mango","banana ","apple "]
def removeWordFromListAndStrip(item):
    new_list = []
    for i in l:
        clean_word = i.strip() 
        if clean_word != item:
            new_list.append(clean_word)
    return new_list

print(removeWordFromListAndStrip("apple"))

            