import time
import random

#function that adds 2 seconds in between every piece of text 
def print_pause(message):
	print(message)
	time.sleep(2)

def library():
	print_pause("You endup back to the library it's night and everyone's gone")
	print_pause("Enter 1 to exit door. \n")
	print_pause("Enter 2 go back to the country side kitchen.\n")
	choice = input("Please enter 1 or 2\n")

	valid=True
	while valid == True:
		if int(choice) == 1:
			print_pause("You exit the library and go home\n")
			play_game()
			valid=False
		elif int(choice)== 2:
			front_door()
			valid=False
		else:
			choice=input("Please enter 1 or 2\n")
			

def front_door():
	print_pause("You open the front door and infront of you is a corn field across the street you notice\n")
	print_pause("BLACK FIGURE STANDING THERE AND THEN IT STARTS RUNNING TOWARDS YOU!!!!\n")
	print_pause("You put salt along the door to protect yourself from this figure you run towards the porch\n")
	print_pause("Enter 1 to get into the car infront of you and escape\n")
	print_pause("Enter 2 to go outside and look around\n")
	choice=input("Please enter 1 or 2\n")

#repeated code with slight difference see if you can add this into a function 
	valid=True
	while valid==True:
		if int(choice)==1:
			car()
			valid=False
		elif int(choice)==2:
			go_outside()
			valid=False
		else:
			choice=input("Please enter 1 or 2\n")
			

def car():
	print_pause("You see the figure circle around and it doesn't seem to notice you\n")
	print_pause("You get out safely and beat the game CONGRATULATIONS!\n")
	play_game()


def go_outside():
	print_pause("You look around and don't see it anywhere it then comes out of the shadows and gets you\n")
	play_game()

"""

make a weapons list to randomly chose from

make a attacker lis to randomly chose from 

fix the input when user doesnt enter valid answer such as 1 or 2

"""
#game over function asks user whther they want to play the game again
def play_game():
	print_pause("Game Over\n")
	choice=input("Would you like to play again enter 1 for yes and 2 for no\n")

	valid=True
	while valid == True:
		if int(choice)==1:
			start()
			valid=False
		elif int(choice)==2:
			print_pause("Thanks for playing come again")
			valid=False
		else:
			choice=input("Please enter 1 for yes and 2 for no\n")


#function that starts off game 
def start():
	print_pause("You are studying for big math test in the library.\n")
	print_pause("You leave the room to go to the restroom you endup in a country sidehouse kitchen it is dark\n")
	print_pause("Enter 1 to go back to the door you came from.\n")
	print_pause("Enter 2 to try to leave through the front door.\n")
	print_pause("What would you like to do?\n")
	choice= input("Please enter 1 or 2\n")

	valid=True
	while valid == True:
		if int(choice) == 1:
			library()
			valid=False
		elif int(choice) == 2:
			front_door()
			valid=False
		else:
			choice= input("Please enter 1 or 2\n")


#start game
start()
