'''
The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous
Hi-score. You need to write a program to update the Hi-score whenever the game()
function breaks the Hi-score
'''
import random

def game():
    print("--- 🎮 GAME START! 🎮 ---")
    print("Guess the number between 1 to 10!")
    
    secret_number = random.randint(1, 10)
    attempts = 0
    
    while True:
        guess = int(input("Input the Number (1-10): "))
        attempts += 1
        
        if guess == secret_number:
            score = max(10, 110 - (attempts * 10))
            print("Correct Answer! You are done in" , attempts , "Attempts")
            return score
        elif guess < secret_number:
            print("Guess a big number! 📈")
        else:
            print("Guess a small number! 📉")

c = game()
try:
    f = open("Hi-score.txt","r")
    data = f.read().strip()   
    f.close()
except FileNotFoundError:
    data = ""

if data == "":
    f = open("Hi-score.txt","w")
    f.write(str(c))
    f.close()
    print("Final Score = ", c)
else:  
    hi_score = int(data)
    if c > hi_score:
        f = open("Hi-score.txt" , "w")
        f.write(str(c))
        f.close()
        print("Your New Score is: ", c)
    else:
        print("Your Score = ", c)        
        print("Hi Score = ", hi_score)  