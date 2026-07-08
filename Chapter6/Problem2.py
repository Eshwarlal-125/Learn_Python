# Write a program to find out whether a student has passed or 
# failed if it requires a total of 40% and at least 33% in each 
# subject to pass. Assume 3 subjects and take marks as an
# input from the user.

subj1 = int(input("Enter marks for Subject 1: "))
subj2 = int(input("Enter marks for Subject 2: "))
subj3 = int(input("Enter marks for Subject 3: "))

total_percent = ((subj1 + subj2 + subj3)/300)*100

if(subj1>=33 and subj2>=33 and subj3>=33):
    if(total_percent>=40):
        print("Pass")
    else:
        print("Fail")
else:
    print("Fail")