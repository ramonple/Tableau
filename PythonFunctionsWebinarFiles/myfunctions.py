#Hello World function

import random

def hello_world():
    print("Hello World!")
    print("Hello Universe!")
    
def hello_world_para(name):
    print("Hello", name)
    print("Have a good day.")

def miles_to_km(miles):
    """ converts a miles value to Km """
    km = miles * 1.609344
    return km

def random_no():
    print(random.randint(1,10))
    choice = input("Y for another number, any other key to exit: ")
    if choice == "Y":
        random_no()

def main():
    hello_world()
    hello_world_para("Michelle")
    miles_to_km(12)
    print(miles_to_km(12))

main()



