#Guess the random number with loop
#Use of try to handle errors
#Outputs the mystery number only if guesses wrong

import random

#Setup variables
mysteryNumber = random.randint(1,10)
guess = 1
#Set guess, so guess is wrong for loop and try
guessNumber = 0

print("Guess the mystery number game!")

#Loop to give 3 guesses, also checks for a correct guess with !=, loop stops when the same
while guess <=3 and guessNumber != mysteryNumber:
    try:
        #Handle error if guess is not a whole number
        guessNumber = int(input("Guess a whole number between 1 and 10? "))
    except:
        print("Your input was invalid")
    
    if guessNumber == mysteryNumber:
         print("Your guess is correct!")
    else:
         print("Your guess was wrong!")
         print("Guess number", guess, "of 3!")
    guess +=1

#Only prints out mystery number if all guesses wrong.
if guessNumber != mysteryNumber:
    print("Your guesses have ran out.")
    print("The mystery number was: ", mysteryNumber)

print("Game Over!")
