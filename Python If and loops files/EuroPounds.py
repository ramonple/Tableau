#Covert euro/pounds
euro = 1.12
pound = 0.90

print("Currency converter, Euro/Pound.")

choice = input("Would you like to convert Pounds or Euros [P or E]? ")

#Amount
amount = float(input("Enter the amount of currency: "))

if choice == "P":
    #Calculate to euro
    print(amount, "converted to Euro is", amount * euro)
else:
    #Calc to pounds
    print(amount, "converted to Pounds is", amount * pound)


print("Exiting program.")
