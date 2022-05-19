#Program to record, and then list films
print("Best film list")

#initialise variables
filmList = []
count = 0

n = int(input("How many films would you like to store? "))

#Input film names
while count < n:
        filmName = input("Enter film name: ")
        filmList.append(filmName)        
        print(filmList[count], "has been added to the list.")
        count +=1

print("Your list of films:")

#Print the films using for in loop
for film in filmList:
      print("Film: ", film)

print("End of list!")
