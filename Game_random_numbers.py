#*************Guess the number game***************
#Compiled by : Sumit Purandare

import random
print("Hello!,What is you name ?")
name=input()
print("Bonjour",name,"Well! I was thinking of a number between 1 and 20 ")
#print("Can you guess the number")
spam=random.randint(1,20)
for guesstaken in range(1,7):
    print("Take a guess and you have 6 attempts!")
    input1=int(input())
    if spam<input1:        
        print("Your guess is too high")
    elif spam>input1 :
        print("Number is too low,Try again!")
    else:
        break # this condition ios correct guess
if input1==spam:
    print("Good Job!,",name," You guessed the number right.")
else:
    print("Nope! I was thinking you have exceeded attempted" ,str(guesstaken),"guesses")