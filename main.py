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
weapon = ""
listed = ["", "Sword", "Bow and Arrows", "Banana"]

while (weapon != 1) or (weapon != 2) or (weapon != 3):
    weapon = input("Please select with the number \n1.Sword\n2.Bow and Arrows\n3.Banana\n")
    weapon = int(weapon)

print("I see you have selected " + listed[weapon])

print("You mission is to save the princess, the world relies on you. \nI give you my blessing.")
print("\n")

print("You are in the woods, a humongus gorilla is in front of you.\nWhat will you do?")
choice = input
