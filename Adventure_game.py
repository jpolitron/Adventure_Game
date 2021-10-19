import time
import random

#functions needed
def print_pause(message):
	print(message)
	time.sleep(2)

def library():
	print_pause("You endup back to the library it's night and everyone's gone")
	print_pause("Enter 1 to exit door. \n")
	print_pause("Enter 2 go back to the country side kitchen.\n")


"""

#make a weapons list to randomly chpose from

#make a attacker list

def front_door():

def car():

def go_outside():

def play_game():
	#call function depending what player choses in the END
"""		
def start():
	#playing = True
	print_pause("You are studying for big math test in the library.\n")
	print_pause("You leave the room to go to the restroom you endup in a country sidehouse kitchen it is dark do you\n")
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
			#call function
			valid=False
		else:
			choice= input("Please enter 1 or 2\n")


#start game
start()
