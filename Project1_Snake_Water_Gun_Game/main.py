'''
snake = 1
water = -1
gun = 0
'''
import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {
    "s":1, "w":-1, "g":0
}
reverseDict = {
    1:"Snake", -1:"Water", 0:"Gun" 
}
if youstr not in youDict:
    print("Invalid choice! Please enter s, w, or g.")
    exit()

you = youDict[youstr]

print("You Choose: ", reverseDict[you])
print("Computer Choose: ", reverseDict[computer])

if(computer == you):
    print("Its a draw")
else:
    if(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == 0 and you == 1):
        print("You Lose!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 1 and you == -1):
        print("You Lose!")
    else:
        print("Something went Wrong!")
