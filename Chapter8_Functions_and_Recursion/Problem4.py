# Write a recursive function to calculate the sum of first n natural numbers.
def sumNaturalNumbers(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    else:
        return number + sumNaturalNumbers(number-1)

print(sumNaturalNumbers(6))