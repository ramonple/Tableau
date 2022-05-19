#Waist size health

def waist_input():
    waistCM = input("What is your waist size in CM? ")
    try:
        waistCMFloat = float(waistCM)
    except:
        print("You need to enter a number.")
        waistCMFloat = waist_input()
    return waistCMFloat

def waist_to_health(cm):
    """ Checks the waist measurement agains WHO recommendation """
    if cm < 93.98:
        result = ("Well done, you have a healthy waist size!")
    else:
        result = ("You are over the recommended waist size.")

    return result

def main():
    waistSize = waist_input()
    waistHealth = waist_to_health(waistSize)
    print(waistHealth)

main()
        
    
