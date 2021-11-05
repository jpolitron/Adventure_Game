import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def intro():
    print_pause("You are studying for big math test in your school library.\n")
    print_pause("You leave the room to go to the restroom you open the door\n")
    print_pause("and endup in a country sidehouse kitchen it is dark\n")


def front_door(items, killer):
    print_pause("You open the front door and infront of you is a corn field.")
    print_pause("You notice a {} standing there suddenly" .format(killer))
    print_pause("it starts running towards you!!!\n")

    if "heavy duty chain" in items:
        print_pause("You close the door and lock it\n")
        move_around(items, killer)
    else:
        print_pause("The {} gets you".format(killer))
        print_pause("game over")
        play_again()


def kitchen(items, killer):
    print_pause("The kitchen is dark and no one is home\n")
    print_pause("you see the lock on a table and save it for later\n")

    items.append("heavy duty chain")

    if "car keys" in items:
        print_pause("You are trying to figure out how to locate the car\n")
    else:
        move_around(items, killer)


def library(items, killer):
    print_pause("everyone you were with is gone and it is now 3 am \n")
    print_pause("you see car keys left on the table\n")
    items.append("car keys")
    move_around(items, killer)


def library_exit(items, killer):
    print_pause("you exit the library and go home\n")
    print_pause("Congratulations you beat the game\n")
    play_again()


def back_door(items, killer):
    print_pause("The {} circles around the back porch".format(killer))
    print_pause("it does not seem to see you")

    if "car keys" in items:
        print_pause("you get in the car and drive off before it sees you\n")
        print_pause("Congratulations you beat the game\n")
        play_again()
    else:
        print_pause("you don't have the car keys\n")
    move_around(items, killer)


def move_around(items, killer):
    print_pause("Enter the number for the room you want to go to\n")
    room = valid_input(
        "1 front door of country side house\n"
        "2 country side kitchen\n"
        "3 library\n"
        "4 library exit door\n"
        "5 house back door\n",
        ['1', '2', '3', '4', '5']
        )

    if room == '1':
        front_door(items, killer)
    elif room == '2':
        kitchen(items, killer)
    elif room == '3':
        library(items, killer)
    elif room == '4':
        library_exit(items, killer)
    elif room == '5':
        back_door(items, killer)


def valid_input(prompt, options):
    while True:
        option = input(prompt)
        if option in options:
            return option
        else:
            print("not a valid response. try again")


def play_again():
    options = valid_input("Would you like to play again?(y/n)\n", ['y', 'n'])
    if options.lower() == 'y':
        play_game()
    elif options.lower() == "n":
        print_pause("Thanks for playing!")
        exit(0)


def play_game():
    items = []
    enemy = ["Black figure", "Zombie", "Serial Killer"]
    killer = random.choice(enemy)
    intro()
    move_around(items, killer)


play_game()
