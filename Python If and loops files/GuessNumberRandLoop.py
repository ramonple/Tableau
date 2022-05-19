#Guess the random number with loop

import random

#Setup variables
mysteryNumber = random.randint(1,10)
#Counter for each guess
guess = 1

#Loop to give 3 guesses
while guess <=3:

    guessNumber = int(input("Guess a whole number between 1 and 10? "))
    
    if guessNumber == mysteryNumber:
         print("Your guess is correct!")
    else:
         print("Your guess was wrong!")
         print("Guess number", guess, "of 3!")

    #Increment the guess after each try
    guess +=1

print("The end!")
