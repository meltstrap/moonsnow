import time
import os
import sys
def definesavedperson():
	global savedperson
	savedperson = 0


def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def startup():
	definesavedperson()
	clear()
	print("===== Moonsnow =====")
	print()
	print("1. Play")
	print("2. Quit")
	print()
	inputprompt1()

def inputprompt1():
	input1 = input("Enter: ")
	if input1 == "1":
		room1()
	if input1 == "2":
		sys.exit()
	else:
		print("Sorry, try again.")
		inputprompt1()

def room1():
	clear()
	print("Waken up by the moonlight, you find yourself in the soft grass, wide as your field of view.")
	time.sleep(3)
	print("Your blue eyes point towards the sky, watching the flying angels fly around.")
	time.sleep(3)
	print("After that, you stand up, noticing that you are surrounded of dark green trees.")
	time.sleep(3)
	print("There are two paths. One towards the moon, the other towards a tall mountain.")
	time.sleep(3)
	print("What do you want to do?")
	print()
	print("1. Go towards the mountain.")
	print("2. Go towards the moonlight.")
	print()
	inputprompt2()

def inputprompt2():
	input2 = input("Enter: ")
	if input2 == "1":
		room2()
	elif input2 == "2":
		room3()
	else:
		print("Sorry, try again.")
		inputprompt2()

def room2():
	clear()
	print("You go towards the mountain, around the soft trees and flashing fireflies.")
	time.sleep(3)
	print("The top of the mountain is full of snow, soft as a polar bear. Also, you see a cave, black as a black hole.")
	time.sleep(3)
	print("What are you going to do?")
	print()
	print("1. Go to the snow.")
	print("2. Go to the cave.")
	print()
	inputprompt3()

def inputprompt3():
	input3 = input("Enter: ")
	if input3 == "1":
		room2_1()
	elif input3 == "2":
		room2_2()
	else:
		print("Sorry, try again.")
		inputprompt3()

def room2_1():
	clear()
	print("You go towards the snow through a clean path. Then you play through the snow.")
	time.sleep(3)
	print("Then you see a small house with smoke going out of his chimney. You also want to go back to the cave to see what it is about.")
	time.sleep(3)
	print("What are you going to do?")
	print()
	print("1. Go to the small house.")
	print("2. Go to the cave.")
	print("3. Go back and choose the other path.")
	print()
	inputprompt4()

def inputprompt4():
	input4 = input("Enter: ")
	if input4 == "1":
		ending1()
	elif input4 == "2":
		room2_2()
	elif input4 == "3":
		clear()
		print("You go back towards the moonlight")
		sleep(3)
	else:
		print("Sorry, try again.")
		print()
		inputprompt4()

def ending1():
	clear()
	print("You enter to the small house and you see a couch. You see also a little kitchen.")
	time.sleep(3)
	print("You fall asleep on the couch and hours later, see the warm sunbeam through your window.")
	time.sleep(3)
	print()
	print("1. Start over again.")
	print()
	inputprompte()

def room2_2():
	clear()
	print("You go to the cave. Then you see a flashlight on the floor.")
	time.sleep(3)
	print("What are you going to do?")
	print()
	print("1. Grab the flashlight")
	print("2. Leave it where it is.")
	print()
	inputprompt6()

def inputprompt5():
	input5 = input("Enter: ")
	if input5 == "1":
		room2_2_1()
	elif input5 == "2":
		ending2()
	else:
		print("Sorry, try again.")
		inputprompt5()

def room2_2_1():
	clear()
	print("You grab it up and you turn it on. It still has some charge for a few hours.")
	time.sleep(3)
	print("You go deeper through the cave, feeling the coldness surround your body. Lucky enough, you find a leather jacket.")
	time.sleep(3)
	print("What are you going to do?")
	print()
	print("1. Wear the jacket.")
	print("2. Leave it where it is.")
	print()
	inputprompt7()

def inputprompt6():
	input6 = input("Enter: ")
	if input6 == "1":
		room2_2_1_1()
	elif input7 == "2":
		ending3()
	else:
		print("Sorry, try again.")
		inputprompt6()

def room2_2_1_1():
	localsavedperson = savedperson
	if localsavedperson == 1:
		room2_2_1_1saved()
	else:
		clear()
		print("You wear it and go deeper. Then you find someone, thinking -I know who this is.")
		time.sleep(3)
		print("You grab him up and go back to the moonlight. He's still breathing, but he's uncouscious.")
		time.sleep(3)
		localsavedperson = 1
		localsavedperson = savedperson
		print("What are you going to do?")
		print()
		print("1. Take him through the snow.")
		print("2. Go back to the cave and investigate.")
		print("3. Go towards the moonlight and leave him here.")
		print()
		inputprompt7()
	

def inputprompt7():
	input8 = input("Enter: ")
	if input7 == "1":
		ending5()
	elif input7 == "2":
		ending4()
	elif input7 == "3":
		clear()
		print("You go back towards the moonlight")
		sleep(3)
		room3()
	else:
		print("Sorry, try again.")
		inputprompt7()
	

def ending2():
	clear()
	print("You decide to not take the flashlight with you. Minutes later, you fall into ice cold water and drown.")
	time.sleep(3)
	print("GAME OVER.")
	time.sleep(3)
	print()
	print("1. Start over again.")
	inputprompte()

def ending3():
	clear()
	print("You decide to leave it where it is. Later, you freeze and die from hypothermia.")
	time.sleep(3)
	print("GAME OVER.")
	time.sleep(3)
	print()
	print("1. Start over again.")
	print()
	inputprompte()

def ending4():
	clear()
	print("You decide to leave him outside the cave and investigate why is he uncounscious.")
	time.sleep(3)
	print("You hope that the flashlight can hold some minutes turned on.")
	time.sleep(3)
	print("Hearing the silent waterdrops hit the cold floor, being afraid of dying alone, you go deeper into the cave.")
	time.sleep(3)
	print("Someone is smelling your bloody meat...")
	time.sleep(3)
	print("GAME OVER.")
	print()
	print("1. Start over again.")
	print()
	inputprompte()

def inputprompte():
	inputx = input("Enter: ")
	if inputx == "1":
		startup()
	else:
		print("Sorry, try again.")
		inputprompte()

def ending5():
	clear()
	print("You decide to go with him through the snow.")
	time.sleep(3)
	print("You find a little house in the middle of the snow. You go and open the door.")
	time.sleep(3)
	print("You put him to rest on a couch inside the house. In the house there's a kitchen. Maybe you could make a tea for him... if you find tea, obviously.")
	time.sleep(3)
	print("You find a tea box inside a little door. You put water to boil and grab a mug.")
	time.sleep(3)
	print("You put the tea mug next to him and rest on another couch.")
	time.sleep(3)
	print()
	print("1. Start over again.")
	print()
	inputprompte()

def room3():
	localsavedperson2 = savedperson
	if localsavedperson2 == 1:
		ending6()
	clear()
	print("You go towards the moon and find a beach. You walk through the soft sand, touching it with your fingers.")
	time.sleep(3)
	print("Then you go deeper on the ocean, seeing the fish swim through the water.")
	time.sleep(3)
	print("You find a body near the water. You know who this is.")
	time.sleep(3)
	print("You get her out of the water. She's still alive.")
	localsavedperson2 = 1
	localsavedperson2 = savedperson
	time.sleep(3)
	print("You decide to go with her to the mountain, around the soft trees and flashing fireflies.")
	time.sleep(3)
	print("The top of the mountain is full of snow, soft as a polar bear. Also, you see a cave, black as a black hole.")
	time.sleep(3)
	print("What are you going to do?")
	print()
	print("1. Leave her here and go to the cave.")
	print("2. Go through the snow with her.")
	print()
	inputprompt8()


def ending6():
	clear()
	print("You go towards the moon and find a beach. You walk through the soft sand, touching it with your fingers.")
	time.sleep(3)
	print("Then you go deeper on the ocean, seeing the fish swim through the water.")
	time.sleep(3)
	print("You find a body near the water. You know who this is.")
	time.sleep(3)
	print("You get her out of the water. She's still alive.")
	time.sleep(3)
	print("You decide to go with both of them through the snow.")
	time.sleep(3)
	print("You find a little house in the middle of the snow. You go and open the door.")
	time.sleep(3)
	print("You put both of them to rest on a couch inside the house. In the house there's a kitchen. Maybe you could make a tea for them... if you find tea, obviously.")
	time.sleep(3)
	print("You find a tea box inside a little door. You put water to boil and grab two mugs.")
	time.sleep(3)
	print("You put the tea mugs next to them and rest on another couch.")
	time.sleep(3)
	print()
	print("1. Start over again.")
	print()
	inputprompte()


def inputprompt9():
	input8 = input("Enter: ")
	if input8 == "1":
		room2_2()
	elif input8 == "2":
		ending7()
	else:
		print("Sorry, try again.")
		inputprompt8()

def ending7():
	clear()
	print("You decide to go with her through the snow.")
	time.sleep(3)
	print("You find a little house in the middle of the snow. You go and open the door.")
	time.sleep(3)
	print("You put her to rest on a couch inside the house. In the house there's a kitchen. Maybe you could make a tea for him... if you find tea, obviously.")
	time.sleep(3)
	print("You find a tea box inside a little door. You put water to boil and grab a mug.")
	time.sleep(3)
	print("You put the tea mug next to him and rest on another couch.")
	time.sleep(3)
	print()
	print("1. Start over again.")
	print()
	inputprompte()

def room2_2_1_1saved():
	clear()
	print("You wear it and go deeper. Then you find someone, thinking -I know who this is.")
	time.sleep(3)
	print("You grab him up and go back to the moonlight. He's still breathing, but he's uncouscious.")
	time.sleep(3)
	print("What are you going to do?")
	print()
	print("1. Take both of them through the snow.")
	print("2. Go back to the cave and investigate.")
	print()
	inputprompt9()

def inputprompt0():
	input8 = input("Enter: ")
	if input8 == "1":
		ending8()
	elif input8 == "2":
		ending4()
	else:
		print("Sorry, try again.")
		inputprompt9()

def ending8():
	clear()
	print("You decide to go with both of them through the snow.")
	time.sleep(3)
	print("You find a little house in the middle of the snow. You go and open the door.")
	time.sleep(3)
	print("You put both of them to rest on a couch inside the house. In the house there's a kitchen. Maybe you could make a tea for them... if you find tea, obviously.")
	time.sleep(3)
	print("You find a tea box inside a little door. You put water to boil and grab two mugs.")
	time.sleep(3)
	print("You put the tea mugs next to them and rest on another couch.")
	time.sleep(3)
	print()
	print("1. Start over again.")
	print()
	inputprompte()

startup()
