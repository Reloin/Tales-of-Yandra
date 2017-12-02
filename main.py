from time import sleep
import time
import os
from random import uniform
import sys

mmc = "Hanji"
fmc = "Yandra"
valid = ['yes', 'no', 'y', 'n']
validlocation = ['east', 'west', 'north', 'south']
roomNo = 1
location = ""
exitnow = False
validaction = ['pickup']
validobject = ['skull', 'meme']


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


def returnaction(v, n):
    print("\nYou choosed to", v, n)


def game_over():
    for x in "GAME OVER":
        print(x, end='')
        sys.stdout.flush()
        sleep(uniform(0, 0.3))


def checkanswer(q, extend):
    while True:
        a = str.lower(input(q))
        c = a.split()
        if c[0] in validaction and c[1] in validobject:
            validaction.append(extend)
            return a
            returnaction(c[0], c[1])
            if(roomNo == 3):
                exitnow = True
        else:
            q = str("\nPlease enter a valid verb + action\nAvailable commands: " + str(validaction).strip('[]') + ".\n>> ")


def sword():
    delay_print("\nYou have just picked up a glittering sword which looks as shiny as the iPhone X.")
    print('\n')
    delay_print("Before you could think further, you fell into a trap just beneath your feet which you didn't notice before this.")
    time.sleep(.7)
    os.system('cls')
    print("\nIt's dark around you")
    print("\nYou will have to find a way to get out of here")

    while True:
        location = str.lower(input("\nWhich direction would you like to head to next? (East, West, North, South). You're in room " + str(roomNo) + "\n>> "))
        if location in validlocation:
            headto(location, roomNo)
        else:
            print("\nPlease select between east, west, north and south.\n>> ")


def headto(s, roomNo):
    print('\nYou\'re now heading to the', s)
    if(roomNo == 1):
        if(location == 'east'):
            location == ''
            roomNo += 1
            checkanswer("\nYou see a black skull on the ground, what would you like to do next? \n>> ", 'tear')
            print("This game crashed :)")

        else:
            print("\nThere is nothing in the", s, '\n')
    if(roomNo == 2):
        if(location == 'west'):
            location == ''
            roomNo += 1
            checkanswer("\nIn the dark room, there is a circular opening on the ceiling, what would you like to do next? \n>> ", 'use')
        else:
            print("\nThere is nothing in the", s, '\n')
    if(roomNo == 3):
        if(location == 'north'):
            location == ''
            roomNo += 1
            checkanswer("You have successfully exited the room, you're now at the princess's room, what would you like to do next?", 'save')
            validaction.extend('slap')
        else:
            print("\nThere is nothing in the", s, '\n')


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
        print("With the banana you have she leads you to her village, this village is full of young and")
        sleep(.3)
        print(" beautiful females. She told you that her village suffrer from giving birth the next generations.")
        sleep(1)
        print("As all of the females in this village are dead from an incident, The ramining ones")
        sleep(.3)
        print("tried to find a cure or a solution for this.")
        choice = "x"
        last = None
        while choice not in valid:
            last = input("Will you help them with your banana?\n>>")
        if last == "y" or last == "yes":
            for x in "CONGRATULATIONS":
                print(x, end='')
                sys.stdout.flush()
                sleep(0.2)
            print("you are gay")
            game_over()
        elif last == "n" or last == "no":
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
        print("The gorilla turns out to be " + fmc + "you have been looking for.")
        for x in "GAME END":
            print(x, end='')
            sys.stdout.flush()
            sleep(uniform(.1, .3))
        sleep(.5)
        print("HAPPY ENDING")


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
