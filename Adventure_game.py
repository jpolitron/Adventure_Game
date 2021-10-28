import time
import random

def print_pause(message):
	print(message)
	time.sleep(1)

def intro():
	print_pause("You are studying for big math test in your school library.\n")
	print_pause("You leave the room to go to the restroom once you open the restroom door you endup in a country sidehouse kitchen it is dark\n")


def front_door(items,killer):
	print_pause("You open the front door and infront of you is a huge corn field across the street.")
	print_pause("You notice a {} standing there suddenly" .format(killer))
	print_pause("it starts running towards you!!!")
	
	if "heavy duty chain" in items:
		print_pause("You close the door and lock it")
		move_around(items,killer)
	else:
		print_pause("The {} gets you".format(killer))
		print_pause("game over")
		play_again()

def kitchen(items,killer):
	print_pause("The kitchen is dark and no one is home you are trying to figure out how you ended up in one place when going through the bathroom door you see the lock on a table and save it for later")
	items.append("heavy duty chain")
	if "car keys" in items:
		print_pause("You are trying to figure out how to locate where the car is for these keys so you can escape")
	else:
		print_pause("you find some car keys one the table and you are trying to figure where the car is located")
		items.append("car keys")

	move_around(items,killer)

def library(items,killer):
	print_pause("everyone you were with is gone and it is now 3 am you are puzzled trying to figure out what is going on you see car keys left on the table")
	items.append("car keys")
	move_around(items,killer)

def library_exit(items,killer):
	print_pause("you exit the library and go home")
	print_pause("Congratulations you beat the game and escaped would you like to play again y for yes n for no")
	play_again()

def back_door(items,killer):
	print_pause("You end up in the back porch of the house and the {} circles around the car and does not seem to see you there is a car infront of you".format(killer))
	if "car keys" in items:
		print_pause("you get in the car and drive off before it sees you")
		print_pause("Congratulations you beat the game")
		play_again()
	else:
		print_pause("you don't seem to have any car keys with you there is no oter way to get into the car")
		move_around(items,killer)

def move_around(items,killer):
	print_pause("Enter the number for the room you want to go to")
	room = input("1 front door of country side house\n"
			"2 country side kitchen\n"
			"3 library\n"
			"4 library exit door\n"
			"5 house back door\n")
	if room == '1':
		front_door(items,killer)
	elif room == '2':
		kitchen(items,killer)
	elif room == '3':
		library(items,killer)
	elif room == '4':
		library_exit(items,killer)
	elif room == '5':
		back_door(items,killer)
	else:
		move_around(items,killer)

def play_again():
	print_pause("would you like to play again y for yes and n for no")
	choice = input()
	if choice.lower() == "y":
		play_game()
	elif choice.lower() == "n":
		print_pause("Thank you for playing come again!")
	else:
		play_again()

def play_game():
	items = []
	enemy = ["Black figure","Zombie", "Serial Killer"]
	killer = random.choice(enemy)
	intro()
	move_around(items,killer)


play_game()
