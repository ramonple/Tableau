#Guess random mystery number

#Import the module to allow access to random functions
import random

#Generate a random mystery number, using the random module
mysteryNumber = random.randint(1,10)

#User guess number, convert to and int
guessNumber = int(input("Guess a whole number between 1 and 10?"))

#Check if guess is correct
if guessNumber == mysteryNumber:
    #If correnct
    print("Your guess is correct!")
else:
    #If wrong
    print("Your guess was wrong!")
    #Nice to tell user what the number was!
    print("The mystery number was", mysteryNumber, "!")

#The end.
print("The end!")
