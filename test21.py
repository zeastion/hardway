from sys import exit

def dead(why):
	print why, "Good job!"
	exit(0)

def gold_room():
	print "This room is full of gold.How much do you take?"
	
	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print """There is a bear here.\nThe bear has a bunch of honey.\nThe fat bear is in front of another door.\nHow are you going to move the bear?\n\t1- Take the honey\n\t2- Taunt bear"""
	bear_moved = False

	while True:
		next = raw_input("> ")
		if next == "1":
			dead("The bear looks at you then slaps your face off.")
		elif next == "2" and not bear_moved:
			print "The bear has moved from the door.You can go through it now.\n\t1- Taunt bear\n\t2- Open door"
			bear_moved = True
		elif next == "1" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "2" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "Here you see the great evil Cthulhu.\nHe, it, whatever stares at you and you go insane.\nDo you flee for your life or eat your head?"
	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def start():
	print "You are in a dark room.\nThere is adoor to your right and left.\nWhich one do you take?"
	
	next = raw_input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()
