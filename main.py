mmc = "Hanji"
fmc = "Yandra"

# introduction
print("Welcome hero, to the world of Imagnus. \nI am Talia, the goddes of this world", '\n')

filler = input("What's your name? \n>> ")

print("\nSo your name is", mmc, '\n')

validgender = ['yes', 'no', 'y', 'n']
validweapon = [1, 2, 3]

gender = None
weapon = None

# variables for questions to avoid displaying multiple of them
gender_question = str("Are you a male or a female, or you identify yourself as something else? \n>> ")
weapon_question = str("Please select with the number \n1.Sword\n2.Bow and Arrows\n3.Banana \n>> ")
listed = ["", "Sword", "Bow and Arrows", "Banana"]

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
                print("\n\n\n\n\n")

            else:
                weapon_question = str("\nPlease select a valid weapon with the number \n1.Sword\n2.Bow and Arrows\n3.Banana \n>> ")

        gender_question = ''

    else:
        gender_question = str("\nPlease answer yes or no .\n>> ")
