mmc = "Hanji"
fmc = "Yandra"

print("Welcome hero, to the world of Imagnus. \n I am Talia, the goddes of this world")
filler = input("What's your name? \n")
print("So your name is " + mmc)
validgender = ['yes', 'no', 'y', 'n']
gender = None

print("Are you a male or a female, or you identify yourself as something else?")

while (gender)
gender = str.lower(input("Please answer yes or no \n"))
while gender in validgender:
    print("Let's begin your journey. First you'll need a weapon, what weapon would you choose?")
    weapon = None
    listed[3] = {"Sword", "Bow and Arrows", "Banana"}
    while (weapon is not 1) or (weapon is not 2) or (weapon is not 3):
        print("Please select with the number \n1.Sword\n2.Bow and Arrows\n3.Banana")
        break

else:
    print("Please answer yes or no .\n")
weapon = weapon - 1
print("I see you selected " + listed[weapon])
