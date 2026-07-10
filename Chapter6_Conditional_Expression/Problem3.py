# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”.
# Write a program to detect these spams.

sentence = str(input("Enter a sentence: "))

if("make a lot of money" in sentence.lower() or "buy now" in sentence.lower() or "subscribe this" in sentence.lower() or "click this" in sentence.lower()):
    print("SPAM")
else:
    print("SAFE")