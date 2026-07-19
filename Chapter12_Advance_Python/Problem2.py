# Write a program to print third, fifth and seventh element from a list using enumerate function.
numbers = ["1st","2nd","3rd","4th","5th","6th","7th","8th"]

for index,value in enumerate(numbers):
    if index == 2 or index == 4 or index == 6:
        print(f"This is index: {index}, and value is: {value}")