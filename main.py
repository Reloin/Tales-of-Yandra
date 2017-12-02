from time import sleep
import sys

mmc = "Hanji"
fmc = "Yandra"


def sword():
    print("This is to sword")


def bow():
    print("This is a bow")


def banana():
    print("\nYou are in the woods, a humongus gorilla is in front of you.\nWhat will you do?")
    select = 0
    while select <= 0 or select < 3:
        select = input("1.Attack\n2.Run\n3.Give Banana\n>>")
    if select == 1:
        print("You attacked the gorilla, but your banana did not damage to the gorilla.")
        for x in "Sqush! Squash...":
            print(x, end='')
            sys.stdout.flush()
            sleep(0.1)


# introduction
print("Welcome hero, to the world of Imagnus. \n I am Talia, the goddes of this world")
filler = input("What's your name? \n>>")
print("So your name is " + mmc)
validgender = ['yes', 'no', 'y', 'n']
gender = None

# select gender
print("Are you a male or a female, or you identify yourself as something else?")

# if it's not yes or no then loop
while gender not in validgender:
    gender = str.lower(input("Please answer yes or no \n>>"))


print("Let's begin your journey. First you'll need a weapon, what weapon would you choose?")
weapon = 4
listed = ["", "Sword", "Bow and Arrows", "Banana"]

while weapon > 3 or weapon <= 0:
    weapon = input("Please select with the number \n1.Sword\n2.Bow and Arrows\n3.Banana\n>>")
    weapon = int(weapon)


print("I see you have selected " + listed[weapon])

print("You mission is to save the princess, the world relies on you. \nI give you my blessing.")
print("z")
sleep(.7)
print("zzzz")
sleep(.7)
print("zzzzzzzzz")
sleep(.7)
print("zzzzzzzzzzzzzzz")
sleep(.7)

if(weapon == 1):
    sword()

if(weapon == 2):
    bow()

if(weapon == 3):
    banana()
