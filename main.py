<<<<<<< HEAD
=======
import time
import sys

>>>>>>> 5edf701175f3989dd1d1c45566edbe6def5b72d8
mmc = "Hanji"
fmc = "Yandra"

# introduction
print("Welcome hero, to the world of Imagnus. \n I am Talia, the goddes of this world")
filler = input("What's your name? \n")
print("So your name is " + mmc)
validgender = ['yes', 'no', 'y', 'n']
gender = None

# select gender
print("Are you a male or a female, or you identify yourself as something else?")

# if it's not yes or no then loop
while gender not in validgender:
    gender = str.lower(input("Please answer yes or no \n"))


print("Let's begin your journey. First you'll need a weapon, what weapon would you choose?")
weapon = 4
listed = ["", "Sword", "Bow and Arrows", "Banana"]

<<<<<<< HEAD
while weapon > 3 or weapon <= 0:
    weapon = input("Please select with the number \n1.Sword\n2.Bow and Arrows\n3.Banana\n")
    weapon = int(weapon)


print("I see you have selected " + listed[weapon])

print("You mission is to save the princess, the world relies on you. \nI give you my blessing.")
print("\n\n\n\n\n")

print("You are in the woods, a humongus gorilla is in front of you.\nWhat will you do?")
=======
# select gender
while True:
    gender = str.lower(input(gender_question))
    if gender in validgender:
        # select weapon
        print("\nLet's begin your journey. First you'll need a weapon, what weapon would you choose?\n")
        while True:
            weapon = int(input(weapon_question))
            if weapon in validweapon:
                print("\nI see you selected " + listed[weapon] + '\n')
                weapon_question = ''
                print("You mission is to save the princess, the world relies on you. \nI give you my blessing.")
                print("")
                time.sleep(.7)
                print("z")
                time.sleep(.7)
                print("zzzz")
                time.sleep(.7)
                print("zzzzzzzzzzzzzzzzzz")
                time.sleep(.7)
                break

            else:
                weapon_question = str("\nPlease select a valid weapon with the number \n1.Sword\n2.Bow and Arrows\n3.Banana \n>> ")

        gender_question = ''

    else:
        gender_question = str("\nPlease answer yes or no .\n>> ")

    break

print("out")
>>>>>>> 5edf701175f3989dd1d1c45566edbe6def5b72d8
