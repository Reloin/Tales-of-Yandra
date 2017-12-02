from time import sleep
from random import uniform
import sys

mmc = "Hanji"
fmc = "Yandra"
valid = ['yes', 'no', 'y', 'n']


def game_over():
    for x in "GAME OVER":
        print(x, end='')
        sys.stdout.flush()
        sleep(uniform(0, 0.3))


def sword():
    print("This is to sword")


def bow():
    print("You came to a garden and you wandered around.")
    choice = input("You saw a black witch, will you shoot it down?(yes/no)\n>>")
    while choice not in valid:
        choice = input("You saw a black witch, will you shoot it down?(yes/no)\n>>")
    if choice == "yes" or choice == "y":
        print("You shot it down, the black colour faded and reveals a female's body.")
        sleep(1)
        print("It was " + fmc)
        sleep(.4)
        print("You killed who you were supposed to protect")
        sleep(.3)
        game_over()
    elif choice == "n" or choice == "no":
        print("The witch leaves a spell on you, you were stoned.")
        sleep(1)
        print("You are going to stand here holding a bow and arrow")
        print("for the rest of your life.")
        game_over()


def banana():
    print("\nYou are in the woods, a humongus gorilla is in front of you.\nWhat will you do?")
    select = 0
    while select <= 0 or select > 3:
        select = input("1.Attack\n2.Run\n3.Give Banana\n>>")
        select = int(select)
    if select == 1:
        print("You attacked the gorilla, but your banana did not damage to the gorilla.")
        sleep(1)
        for x in "Sqush! Squash...":
            print(x, end='')
            sys.stdout.flush()
            sleep(0.1)
        sleep(2)
        print("\nYou are squash to death by a gorilla.")
        sleep(1)
        game_over()
    elif select == 2:
        print("You run and run ", end='')
        sleep(.7)
        print("you bump into a girl.")
        print("With the banana you have she leads you to her village, this village is full of ")
        sleep(.3)
        print("young and beautiful females. She told you that her village suffrer from giving")
        sleep(1)
        print("birth the next generations. As all of the females in this village are dead from")
        sleep(.3)
        print("an incident, The ramining ones tried to find a cure or a solution for this.")
        choice = input("Will you help them with your banana?(yes/no)\n>>")
        while choice not in valid:
            choice = input("Will you help them with your banana?(yes/no)\n>>")
            pass
        if choice == "y" or choice == "yes":
            for x in "CONGRATULATIONS":
                print(x, end='')
                sys.stdout.flush()
                sleep(0.1)
            sleep(1)
            print("\nyou are gay")
            game_over()
        elif choice == "n" or choice == "no":
            print("They killed you by not helping them.")
            game_over()

    elif select == 3:
        print("You gave the gorilla your banana, the gorilla thinks you're friendly.")
        print("The gorilla gave you a pineapple. The gorilla became your companion.")
        for x in "Wha... What?":
            print(x, end='')
            sys.stdout.flush()
            sleep(uniform(.2, .5))
        sleep(1)
        print("\nThe gorilla turns out to be " + fmc + "you have been looking for.")
        for x in "GAME END":
            print(x, end='')
            sys.stdout.flush()
            sleep(uniform(.1, .3))
        sleep(.5)
        print("\nHAPPY ENDING")


# introduction
print("Welcome hero, to the world of Imagnus. \n I am Talia, the goddes of this world")
filler = input("What's your name? \n>>")
print("So your name is " + mmc)
gender = None

# select gender
print("Are you a male or a female, or you identify yourself as something else?")

# if it's not yes or no then loop
while gender not in valid:
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
    sleep(.1)
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
