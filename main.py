from time import sleep
from random import uniform
import sys

mmc = "Hanji"
fmc = "Yandra"


def game_over():
    for x in "GAME OVER":
        print(x, end='')
        sys.stdout.flush()
        sleep(uniform(0, 0.3))


def sword():
    print("This is to sword")


def bow():
    print("This is a bow")


def banana():
    print("\nYou are in the woods, a humongus gorilla is in front of you.\nWhat will you do?")
    select = 0
    while select <= 0 or select > 3:
        select = input("1.Attack\n2.Run\n3.Give Banana\n>>")
        select = int(select)
    if select == 1:
        print("You attacked the gorilla, but your banana did not damage to the gorilla.")
        for x in "Sqush! Squash...":
            print(x, end='')
            sys.stdout.flush()
            sleep(0.1)
        sleep(2)
        print("\nYou are squash to death by a gorilla.")
        sleep(1)
        game_over()
    elif select == 2:
        print("")
    elif select == 3:
        print("You gave the gorilla your banana, the gorilla thinks you're friendly.")
        print("The gorilla gave you a pineapple. The gorilla became your companion.")
        for x in "Wha... What?":
            print(x, end='')
            sys.stdout.flush()
            sleep(uniform(.2, .5))
        sleep(1)
        print("The gorilla turns out to be " + fmc + "you have been looking for.")


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

print("You mission is to save the princess, the world relies on you. ")
for x in "I give you my blessing.":
    print(x, end='')
    sys.stdout.flush()
    sleep(.2)
print("\nz")
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
